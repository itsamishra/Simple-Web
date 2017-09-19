import bs4 as bs
import urllib.request

# Returns an array with last x (amount tbd) tweets from specified handle
def twitterScraper(twitterHandles, tweetLimit=5):
	tweets = []

	for handle in twitterHandles:
		url = "https://twitter.com/" + str(handle)
		pageHTML = urllib.request.urlopen(url)

		soup = bs.BeautifulSoup(pageHTML, "html.parser")

		'''=====FOR=====DEBUGGING=====
		print("@"+str(handle) + "'s timeline:")
		print("===============================")
		'''
		twitterTimeline = soup.findAll("p", {"class":"TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"})

		numTweets = 0
		for tweet in twitterTimeline:
			numTweets+=1

			'''=====FOR=====DEBUGGING=====
			print(str(numTweets) + ". " + tweet.text)
			'''

			tweets.append(tweet.text)

			if numTweets==tweetLimit:
				break

	return tweets