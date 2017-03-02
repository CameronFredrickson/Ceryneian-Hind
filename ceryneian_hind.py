import sys, requests
import simplejson as json

def check_connection_status(status):
	"""Checks the status code of an http request.

    Args:
        A response object containing the server;s response to an HTTP request

    Returns:
        True is return if the status code is 200
        False is returned for all other server responses
	"""

    if status.status_code == 200:
        return True
    else:
        return False


def get_locations(response_args, f_users):
	"""Prints the location of the user read from a file.

    Args:
        A list containing the token value, token type, and filter parameter to make the request.
        The name of a file in the form of a string containg the list of userid's to be queried from the api.
	"""

    with open(f_users) as f:
        users = f.readlines()
    user_locations = {}
    for user in users:
        status = requests.get("https://api.intra.42.fr/v2/users/" + user.strip() + "/locations?" + "&".join(response_args))
        connection_status = check_connection_status(status)
        if connection_status:
            response = status.json()
            if response:
                print user.strip() + ' is at computer: ' + response[0]['host']
            else:
                print user.strip() + " is not logged onto a computer."
        else:
            print user.strip() + " is an invalid user."


def get_token(client_id, secret_id, args, f_users):
	"""Fetches a token from the api.

    Args:
        The public key needed to query the api
        The private key needed to query the api
        A list containg the client_credentials needed to make a request
        The name of the file containg the user ids to be queried

    Returns:
        A list containing the access token, token type, and filter to make authorized requests from the api
	"""
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
    get_locations(response_args, f_users)

if __name__ == '__main__':
    main()
