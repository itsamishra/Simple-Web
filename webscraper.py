import bs4 as bs
import urllib.request

# Returns a numpy array with last x (amount tbd) tweets from specified handle
def twitterScraper(twitterHandles):
	# TODO figure out if I should use BS4, Twitter API, or Scrapy
	for handle in twitterHandles:
		url = "https://twitter.com/" + str(handle)
		pageHTML = urllib.request.urlopen(url).read()