from enum import Enum

class announcementCategories(Enum):
  STATIONS = [
    'acton-town', 'barons-court', 'ealing-broadway',
    'ealing-common', 'earls-court', 'hammersmith',
    'ravenscourt-park', 'stamford-brook', 'turnham-green',
    'west-kensington'
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