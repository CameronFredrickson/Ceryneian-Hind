import sys, requests
import simplejson as json

def check_connection_status(status):
  if status.status_code == 200:
	return True
  else:
    print "Connection Failed."
    sys.exit(1)


def print_user_locations(user_locations):
  for k,v in user_locations:
    print k, ">", v


def get_locations(response_args, f_users):
  with open(f_users) as f:
    users = f.readlines()
  user_locations = {}
  for user in users:
    status = requests.get("https://api.intra.42.fr/v2/users/" + user.strip() + "/locations?" + "&".join(response_args))
    if check_connection_status(status):
	  response = status.json()
	  print response
	  sys.exit(1)
	  user_locations[user] = response[u'location']
    else:
	  user_location[user] = 'N/A'
  return user_locations



def get_token(client_id, secret_id, args, f_users):
  status = requests.post("https://api.intra.42.fr/oauth/token?%s" % ("&".join(args)))
  if check_connection_status(status): 
    print "+++++++++++++++++++++++++++++++++++"
    print "Connected to the 42 API."
    print "+++++++++++++++++++++++++++++++++++"
  response = status.json()
  response_args = [
                   'access_token=%s' %  response[u'access_token'],
                   'token_type=%s' %  response[u'token_type'],
				   'filter[active]=true'
                  ]
  return response_args


def main():
  try:
    f_users = sys.argv[1]
    client_id = sys.argv[2]
    secret_id = sys.argv[3]
  except IndexError:
    print "A text file must be passed in as an argument when script.py is run, as well as a client_id and a secret_id."
    print "\n\tusage: python script.py [--user file] [client_id] [secret_id]\n"
    sys.exit(1)

  args = [
          'grant_type=client_credentials',
		  'client_id=' + client_id,
		  'client_secret=' + secret_id
		 ]

  response_args = get_token(client_id, secret_id, args, f_users)
  locations = get_locations(response_args, f_users)
  print_user_locations(user_locations)

if __name__ == '__main__':
  main()
