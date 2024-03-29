import argparse
import json
import pprint
import sys
import urllib, urllib2
import oauth2

API_HOST= 'api.yelp.com'
DEFAULT_TERM = 'dinner'
DEFAULT_LOCATION = 'San Francisco, CA'
SEARCH_LIMIT = 3
SEARCH_PATH = '/v2/search/'
BUSINESS_PATH = '/v2/business/'

# OAuth credential placeholders that must be filled in by users.
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
TOKEN = ''
TOKEN_SECRET = ''

def request(host, path, url_params=None):
    """Prepares for OAuth authentication and sends request to API

    Args:
        host (str): The domain host of the API
        path (str): The path of the API after the domain
        url_params (dict): An optional set of query parameters in the request

    Returns:
        dict: JSON response

    Raises: 
        urllib2.HTTPError: An error occurs from the HTTP request
    """
    url_params = url_params or {}
    url = 'http://{0}{1}?'.format(host, path)

    consumer = oauth2.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
    oauth_request = oauth2.Request(method="GET", url=url, parameters=url_params)

    oauth_request.update(
            {
                'oauth_nonce': oauth2.generate_nonce(),
                'oauth_timestamp': oauth2.generate_timestamp(),
                'oauth_token': TOKEN,
                'oauth_consumer_key': CONSUMER_KEY
                }
            )
    token = oauth2.Token(TOKEN, TOKEN_SECRET)
    oauth_request.sign_request(oauth2.SignatureMethod_HMAC_SHA1(), consumer, token)
    signed_url = oauth_request.to_url()

    print 'Querying {0} ... '.format(url)

    conn = urllib2.urlopen(signed_url, None)
    try:
        response = json.loads(conn.read())
    finally:
        conn.close()

    return response

def search(term, location):
    """Query the SEARCH API by a search term and location
    Args:
        term (str): The search term passed to the API
        location (str): The search location passed to the API

    Returns:
        dict: The JSON response from the request
    """

    url_params = {
            'term': term.replace(' ', '+'),
            'location': location.replace(' ', '+'),
            'limit': SEARCH_LIMIT
            }
    return request(API_HOST, SEARCH_PATH, url_params=url_params)

def get_business(business_id):
    """Query the Business API by a business ID

        Args:
            business_id (str): The ID of the business to query

        Returns:
            dict: The JSON response
    """
    business_path = BUSINESS_PATH + business_id

    return request(API_HOST, business_path)

def query_api(term, location):
    """ Queries from the API by the input values from the user

        Args:
            term (str): The search term to query
            location (str): The location of the business to query
    """
    response = search(term, location)

    businesses = response.get('businesses')

    if not businesses:
        print 'No businesses for {0} in {1} found'.format(term, location)
        return

    business_id = businesses[0]['id']

    print '{0} businesses found, querying business info for the top result "{1}" ... '.format(
            len(businesses),
            business_id
            )

    response = get_business(business_id)

    print 'Result for business "{0}" found:'.format(business_id)
    pprint.pprint(response, indent=2)
