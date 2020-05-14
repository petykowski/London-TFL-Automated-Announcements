import os
import argparse
from constant import *
from pydub import AudioSegment, silence


def validate_audio_file(segments, fileType):
  '''
  Returns True when the number of audio segments found matches the number of
  items for the given fileType
  '''

  if len(segments) == len(fileType.value):
    return True
  else:
    raise ValueError("Expected " + str(len(fileType.value)) + ". Received " + str(len(segments)))


def set_output_directory(fileType):
  '''
  Returns the output directory for the given fileType
  '''

  base_dir = os.path.abspath(__file__ + "/../../assets/audio/")
  output_dir = os.path.join(
    base_dir,
    EXPORT_DIRS.get(fileType.name)
  )
  if not os.path.exists(output_dir):
      os.makedirs(output_dir)

  return output_dir


def export_audio_segments(segments, outputDirectory, outputFormat="wav"):
  '''
  Exports segments as .wav files at the given output directory
  '''

  for index, segment in enumerate(segments):
    segment.export(
      # define file path and name
      output_dir + announcementCategories[args.category].value[index] + ".wav",
      format=outputFormat
    )


try:
  # Configure argparse
  parser = argparse.ArgumentParser(prog='segmenter.py', description='Generate TfL announcement segments from audio')
  parser.add_argument('category', choices=[e.name for e in announcementCategories], help='Category')
  parser.add_argument('file', help='.wav audio file to process')
  parser.add_argument('-t', '--threshold', nargs=1, help='Adjust the silence threshold. Default: -60', default=-60)
  parser.add_argument('-l', '--min_length', nargs=1, help='Minimum silence length in ms. Default: 500', default=500)
  args = parser.parse_args()

  # Set Audio File Type and Output Directory
  audio_file_type = announcementCategories[args.category]
  audio_file = AudioSegment.from_wav(args.file)

  # Detect Audio Segments and Validate
  found_audio_segments = silence.split_on_silence(audio_file, min_silence_len=500, silence_thresh=args.threshold)
  validate_audio_file(found_audio_segments, audio_file_type)

  # Export
  output_dir = set_output_directory(audio_file_type)
  export_audio_segments(found_audio_segments, output_dir)

except Exception as e:
  raise e