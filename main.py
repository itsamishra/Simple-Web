import pandas as pd
import numpy as np
import webscraper

# Gets Twitter data and converts it to text
def getTweets(twitterContent):
	twitterHandles = np.array(twitterContent.Content)
	webscraper.twitterScraper(twitterHandles)
	

def main():
	# Gets content to be scraped
	content = pd.read_csv("content.csv")

	# Passes twitter data
	twitterContent = content[content.Name=="Twitter"]
	getTweets(twitterContent)


if __name__ == '__main__':
	main()