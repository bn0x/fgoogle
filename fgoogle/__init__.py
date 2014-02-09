import requests
import sys


class query:
	def __init__(self):
		return None


	def search(self, query):
		googleRequest = requests.get("http://ajax.googleapis.com/ajax/services/search/web", params={'v': "1.0", 'q': query})
		return googleRequest.json()['responseData']['results']