import pandas as pd
import numpy as np
import webscraper

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
	# File in which everything will be written
	outputFile = open("output.txt", "w")

	# Gets content to be scraped
	content = pd.read_csv("content.csv")

	# Gets tweets and writes them to .txt file
	twitterContent = content[content.Name=="Twitter"]
	tweets = getTweets(twitterContent)
	writeTweets(outputFile, tweets, twitterContent.Content)

	# Gets Hacker News headlines and writes it to .txt file
	headlines = getHN()
	writeHeadlines(outputFile, headlines)

	outputFile.close()

if __name__ == '__main__':
	main()