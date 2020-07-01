from enum import Enum

class announcementCategories(Enum):
  STATIONS = [
    'acton_town', 'barons_court', 'ealing_broadway',
    'ealing_common', 'earls_court', 'hammersmith',
    'ravenscourt_park', 'stamford_brook', 'turnham_green',
    'west_kensington', 'chiswick_park', 'gloucester_road',
    'south_kensington', 'sloane_square', 'victoria',
    'st._jamess_park', 'westminster', 'embankment',
    'temple', 'blackfriars', 'mansion_house',
    'cannon_street', 'monument', 'tower_hill',
    'aldgate_east', 'whitechapel', 'stepney_green',
    'mile_end', 'bow_road', 'bromley-by-bow',
    'west_ham', 'plaistow', 'upton_park',
    'east_ham', 'barking', 'upney',
    'becontree', 'dagenham_heathway',
    'dagenham_east', 'elm_park', 'hornchurch',
    'upminster_bridge', 'upminster'
  ]
  PLATFORMS = [
    '1', '2', '3', '4'
  ]
  MESSAGES = [
    'arriving-train', 'is-for'
  ]

EXPORT_DIRS = {
  'STATIONS': 'stations/',
  'PLATFORMS': 'platforms/',
  'MESSAGES': 'messages/'
}