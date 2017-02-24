from urllib2 import urlopen
import json

def main():
  hind = urlopen('https://api.intra.42.fr/oauth/authorize?client_id=45d33b9302c364a2130aa74e735459e64cfc4da181b37e9bb66160d7b09fed47&redirect_uri=&scope=public&state=a_very_long_random_string_witchmust_be_unguessable')
  response = hind.read()
  print response

if __name__ == '__main__':
  main()
