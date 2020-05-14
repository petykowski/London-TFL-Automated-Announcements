import os
import wave
import argparse

# Configure argparse
parser = argparse.ArgumentParser(prog='gapminder.py', description='Use your voice to generate station announcements that mimic the Transport for London\'s (TfL) automated announcements.')
parser.add_argument('platform', help='Platform number represented by single digit integer. Ex. 4')
parser.add_argument('destination', help='Destination station name formatted as lowercase with spaces replaced by dashes. Ex. west-kensington')
args = parser.parse_args()

# Set path to repo
repo_directory = os.path.abspath(__file__ + "/../../")

# Set path to station wav files
stations_directory = os.path.join(
  repo_directory,
  "assets/audio/",
  "stations/",
  args.destination + ".wav"
)

messages_directory = os.path.join(
  repo_directory,
  "assets/audio/",
  "messages/",
  "arriving-train.wav"
)

is_for_directory = os.path.join(
  repo_directory,
  "assets/audio/",
  "messages/",
  "is-for.wav"
)

platforms_directory = os.path.join(
  repo_directory,
  "assets/audio/",
  "platforms/",
  args.platform + ".wav"
)

wave_data = []

# Get Message Data
msg = wave.open(messages_directory, 'rb')
wave_data.append([msg.getparams(), msg.readframes(msg.getnframes())])
msg.close()

# Get Station Data
platform = wave.open(platforms_directory, 'rb')
wave_data.append([platform.getparams(), platform.readframes(platform.getnframes())])
platform.close()

# Get is for Data
is_for = wave.open(is_for_directory, 'rb')
wave_data.append([is_for.getparams(), is_for.readframes(is_for.getnframes())])
is_for.close()

# Get Station Data
station = wave.open(stations_directory, 'rb')
wave_data.append([station.getparams(), station.readframes(station.getnframes())])
station.close()

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
output.setparams(wave_data[0][0])
output.writeframes(wave_data[0][1])
output.writeframes(wave_data[1][1])
output.writeframes(wave_data[2][1])
output.writeframes(wave_data[3][1])
output.close()

print("File Generated: " + announcement_file)