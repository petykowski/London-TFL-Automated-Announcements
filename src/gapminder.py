import os
import wave
import argparse


def generate_announcement(platform, destination):

  # Set path to repo
  repo_directory = os.path.abspath(__file__ + "/../../")

  files = []
  files.append(os.path.join(
      repo_directory,
      "assets/audio/",
      "messages/",
      "arriving-train.wav"
    )
  )
  files.append(os.path.join(
      repo_directory,
      "assets/audio/",
      "platforms/",
    platform + ".wav"
    )
  )
  files.append(os.path.join(
      repo_directory,
      "assets/audio/",
      "messages/",
    "is-for.wav"
    )
  )
  files.append(os.path.join(
      repo_directory,
      "assets/audio/",
      "stations/",
    args.destination + ".wav"
    )
  )

  data = write_wave_data(files)

  return export_file(data)


def write_wave_data(files):

  wave_data = []

  for file in files:
    data = wave.open(file, 'rb')
    wave_data.append([data.getparams(), data.readframes(data.getnframes())])
    data.close()

  return wave_data


def export_file(data):

  announcement_file = "".join([
    'announcement',
    '-',
    args.platform,
    '-',
    args.destination,
    '.wav'
    ]
  )

  # Write Announcement File
  output = wave.open(announcement_file, 'wb')
  output.setparams(data[0][0])
  output.writeframes(data[0][1])
  output.writeframes(data[1][1])
  output.writeframes(data[2][1])
  output.writeframes(data[3][1])
  output.close()

  print("File Generated: " + announcement_file)


try:
  # Configure argparse
  parser = argparse.ArgumentParser(prog='gapminder.py', description='Use your voice to generate station announcements that mimic the Transport for London\'s (TfL) automated announcements.')
  parser.add_argument('platform', help='Platform number represented by single digit integer. Ex. 4')
  parser.add_argument('destination', help='Destination station name formatted as lowercase with spaces replaced by dashes. Ex. west-kensington')
  args = parser.parse_args()

  generate_announcement(args.platform, args.destination)

except Exception as e:
  raise e