import pandas as pd
import numpy as np
import webscraper
import sys

# Number of tweets from each handle allowed
tweetLimit = 5

# Gets Twitter data and converts it to text
def getTweets(twitterContent):
	# Gets twitter handle
	twitterHandles = twitterContent.Content

	# Gets all tweets
	tweets = np.array(webscraper.twitterScraper(twitterHandles, tweetLimit))

	return tweets

# Writes tweets to text file
def writeTweets(file, tweets, handles):
	tweetsPerHandle = int(len(tweets)/len(handles))

	file.write("TWEETS------------------------\n")
	for i in range(len(tweets)):
		# Writes twitter handle
		if(i%tweetsPerHandle==0):
			file.write("@" + handles[i/tweetsPerHandle] + "\n")
		file.write("-" + tweets[i] + "\n")

def getHN():
	headlines = webscraper.hackerNewsScraper()

	return headlines

def writeHeadlines(file, headlines):
	file.write("\nHACKER NEWS HEADLINES---------\n")
	for i in range(len(headlines)):
		file.write(str(i+1) + " " + headlines[i][0] + " (" + headlines[i][1] + ")" + "\n")

def main():
	# Gets content to be scraped
	content = pd.read_csv("content.csv")

	# Gets twitter content if requested in command line arugment
	if "twitter" in sys.argv:
		twitterOutput = open("./Content/twitterOutput.txt", "w")

		# Gets tweets and writes them to .txt file
		twitterContent = content[content.Name=="Twitter"]
		tweets = getTweets(twitterContent)
		writeTweets(twitterOutput, tweets, twitterContent.Content)

		twitterOutput.close()

	# Gets Hacker News content if requested in command line arugment
	if "hackerNews" in sys.argv:
		hackerNewsOutput = open("./Content/hackerNewsOutput.txt", "w")

		# Gets Hacker News headlines and writes it to .txt file
		headlines = getHN()
		writeHeadlines(hackerNewsOutput, headlines)

		hackerNewsOutput.close()


if __name__ == '__main__':
	main()