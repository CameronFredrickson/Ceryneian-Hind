from urllib2 import urlopen, Request
import sys
import json

def store_users(f_users):
  with open(f_users) as f:
    data = f.readlines()
  user_locations = {}
  for user in data:
    user_locations[user.strip()] = 'N/A'
  return user_locations

def print_user_locations(user_locations):
  for k, v in user_locations.items():
    print k, '>', v

def api_call(uid, secret, auth_url):
  hind = urlopen(auth_url)
  # hind = Request('https://api.intra.42.fr/v2/users/:cfredric/locations', headers={'Authorization: Bearer': uid})
  # result = urlopen(hind)
  response = hind.read()
  print response

def main():
  UID = '45d33b9302c364a2130aa74e735459e64cfc4da181b37e9bb66160d7b09fed47'
  SECRET = '03a5508f94b6a7eb05ebec96642598f22001a35ca0f3959f9903bef194187519'
  REDIRECT = 'https://api.intra.42.fr/oauth/authorize?client_id=45d33b9302c364a2130aa74e735459e64cfc4da181b37e9bb66160d7b09fed47&redirect_uri=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FOAuth&response_type=code'
  AUTHORIZE_URL = 'https://api.intra.42.fr/oauth/authorize?client_id=45d33b9302c364a2130aa74e735459e64cfc4da181b37e9bb66160d7b09fed47&redirect_uri=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FOAuth&scope=public&state=a_very_long_random_string_witchmust_be_unguessable'

  f_user = sys.argv[1]
  if not f_user:
    print "A text file must be passed in as an argument when script.py is run."
    print "usage: python script.py [--user file]"
    sys.exit(1)
  api_call(UID, SECRET, AUTHORIZE_URL)
  # print_user_locations(store_users(f_user))

if __name__ == '__main__':
  main()
