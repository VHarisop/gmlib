__author__ = "Vassilis Harisopulos <https://github.com/VHarisop>"
__version__ = 0.1


# a simple test client for a generic site and API 

import httplib2
BASE_URL = "http://127.0.0.1:8000/" #the base URL for testing on localhost
API_URL = "http://127.0.0.1:8000/api/v1/" #the base URL for testing a localhost API

 
POST_CONTENT_TYPE_HEADER = "application/json" #the content-type header for POSTs


def simple_GET(url):

	''' 	a simple GET request to a url.
		returns a tuple with the response
		and the content.
	'''

	http = httplib2.Http()
	_url = BASE_URL + url

	response, content = http.request(_url)

	return response, content


def authenticated_GET(url, username, password):

	'''	a GET request to a url 
		that uses authentication.
		returns a tuple with the
		response and the content.
	'''

	http = httplib2.Http()

	http.add_credentials(username, password)

	_url = BASE_URL + url
	response, content = http.request(_url)


	return response, content


def simple_POST(url, context, query):

	''' a simple POST request to a url '''


	http = httplib2.Http()
	
	_url = BASE_URL + url
	appid = 'MyApp'

	import urllib
	params = urllib.urlencode({
		'appid': appid,
		'context': context,
		'query': query
		})

	response, content = http.request(_url, 'POST', params, 
			headers = {'Content-type': POST_CONTENT_TYPE_HEADER }
			)

	return response, content


def authenticated_POST(url, context, sub, username, password):

	''' an authenticated POST request to a url 
	    useful for API testing
	'''

	http = httplib2.Http()
	http.add_credentials(username, password)
	_url = API_URL + url

	appid = 'MyApp'

	import urllib
	params = urllib.urlencode({
		'appid': appid,
		'context': context,
		'sub': sub
		})

	response, content = http.request(_url, 'POST', params, 
			headers = {'Content-type': POST_CONTENT_TYPE_HEADER }
			)

	return response, content


