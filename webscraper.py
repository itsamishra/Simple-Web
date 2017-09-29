import bs4 as bs
import urllib.request

# Returns an array with last x (amount tbd) tweets from specified handle
def twitterScraper(twitterHandles, tweetLimit=5):
	tweets = []

	# Iterates over twitter handles to scrape
	for handle in twitterHandles:
		# Grabs HTML from twitter.com
		url = "https://twitter.com/" + str(handle)
		pageHTML = urllib.request.urlopen(url)
		soup = bs.BeautifulSoup(pageHTML, "html.parser")

		# Finds tweets
		twitterTimeline = soup.findAll("p", {"class":"TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"})


		numTweets = 0
		for tweet in twitterTimeline:
			numTweets+=1

			# Gets tweet from account page
			tweets.append(tweet.text)

			if numTweets==tweetLimit:
				break

	return tweets

def hackerNewsScraper(itemLimit=10):
	# Item will contain [title, URL], and headlines will contain item
	headlines = []
	item = []

	# Grabs HTML from hacker news
	url = "https://news.ycombinator.com/"
	pageHTML = urllib.request.urlopen(url)
	soup = bs.BeautifulSoup(pageHTML, "html.parser")

	hnItems = soup.findAll("a", {"class":"storylink"})

	print(len(hnItems))


	counter = 0
	for i in hnItems:
		print(i)

		counter+=1
		if counter==10:
			break



if __name__ == '__main__':
	hackerNewsScraper()