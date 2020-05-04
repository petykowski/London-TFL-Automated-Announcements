import os
import wave

# Set path to repo
repo_directory = os.path.abspath(__file__ + "/../../")

# Set path to station wav files
station_directory = os.path.join(
  repo_directory,
  "assets/audio/stations/"
)

# Set path to arriving message file
message_file = os.path.join(
  repo_directory,
  "assets/audio/",
  "message-arriving-train.wav"
)


# Generate message for each station
for filename in os.listdir(station_directory):
  # Filter for .wav files
  if filename.endswith(".wav"):
    print('Processing station: ' + filename)

    announcement_file = 'announcement-' + filename
    wave_data = []

    # Get Message Data
    msg = wave.open(message_file, 'rb')
    wave_data.append([msg.getparams(), msg.readframes(msg.getnframes())])
    msg.close()

    # Get Station Data
    station = wave.open(station_directory + filename, 'rb')
    wave_data.append([station.getparams(), station.readframes(station.getnframes())])
    station.close()

    # Write Announcement File
    output = wave.open(announcement_file, 'wb')
    output.setparams(wave_data[0][0])
    output.writeframes(wave_data[0][1])
    output.writeframes(wave_data[1][1])
    output.close()