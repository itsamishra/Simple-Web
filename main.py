import pandas as pd
import numpy as np
import webscraper

# Number of tweets from each handle allowed
tweetLimit = 5

# Gets Twitter data and converts it to text
def getTweets(twitterContent):
	twitterHandles = twitterContent.Content
	tweets = np.array(webscraper.twitterScraper(twitterHandles, tweetLimit))

	return tweets

def writeTweets(file, tweets, handles):
	tweetsPerHandle = int(len(tweets)/len(handles))

	file.write("TWEETS\n")
	for i in range(len(tweets)):
		if(i%tweetsPerHandle==0):
			file.write("@" + handles[i/tweetsPerHandle] + "\n")
		file.write("-" + tweets[i] + "\n")


def main():
	# File in which everything will be written
	outputFile = open("output.txt", "w")

	# Gets content to be scraped
	content = pd.read_csv("content.csv")

	# Passes twitter data
	twitterContent = content[content.Name=="Twitter"]
	tweets = getTweets(twitterContent)

	'''=====FOR=====DEBUGGING=====
	for i in range(len(tweets)):
		print(str(i+1) + ". " + tweets[i])
	'''

	writeTweets(outputFile, tweets, twitterContent.Content)

	outputFile.close()

if __name__ == '__main__':
	main()