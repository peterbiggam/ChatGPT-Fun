PolFax
PolFax is a Python script that monitors tweets from US Congress members and Senators, fact-checks their tweets, and responds with a fact-check tweet followed by a humorous tweet.

Requirements
Python 3.6+
Twitter Developer Account with API access
OpenAI API access
Setup
Clone this repository or download the PolFax.py script.

Replace the placeholders in PolFax.py with your actual Twitter and OpenAI API keys and tokens:

consumer_key = "your_consumer_key"
consumer_secret = "your_consumer_secret"
access_token = "your_access_token"
access_token_secret = "your_access_token_secret"
openai_api_key = "your_openai_api_key"

Create a file named congress_twitter_ids.txt in the same directory as the PolFax.py script. This file should contain the Twitter IDs of the US Congress members and Senators you want to monitor, one ID per line.

To obtain the Twitter IDs, you can use the TweeterID website to convert Twitter handles to IDs or use the Twitter API's users/show endpoint. You can find lists of Congress members and Senators on websites such as GovTrack or C-SPAN.

Example congress_twitter_ids.txt file:

Copy code
1234567890
2345678901
3456789012
The script will automatically install the required dependencies (Tweepy and OpenAI) when it is run. However, you can also install them manually using the following command:

pip install tweepy==3.10.0 openai==0.27.0
Usage
To run the script, open a terminal, navigate to the directory containing the PolFax.py script, and run: python PolFax.py
The script will start monitoring tweets from the specified US Congress members and Senators. When a new tweet is detected, the script will fact-check the tweet, reply with a fact-check tweet, and then reply to the fact-check tweet with a humorous response.
