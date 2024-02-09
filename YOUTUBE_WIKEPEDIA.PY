import requests

# Wikipedia API endpoint
wikipedia_api_url = 'https://en.wikipedia.org/w/api.php'

# YouTube Data API key
youtube_api_key = 'AIzaSyA_gkCXEG4sJYAu5BW3cbzeRvVjwsmbPvE'

# Topic you want to search for
topic = input('Enter your topic: ')

# Search Wikipedia for information about the topic
wikipedia_params = {
    'action': 'query',
    'format': 'json',
    'prop': 'extracts',
    'titles': topic,
    'exintro': True,
    'explaintext': True
}
wikipedia_response = requests.get(wikipedia_api_url, params=wikipedia_params)
wikipedia_data = wikipedia_response.json()

# Extract information from Wikipedia response
pages = wikipedia_data['query']['pages']
page_id = list(pages.keys())[0]
topic_summary = pages[page_id]['extract']

# Construct a keyword based on the topic
keyword = topic.lower()

# Make a request to the YouTube API to search for videos based on the keyword
youtube_response = requests.get(f'https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=5&q={keyword}&key={youtube_api_key}')
youtube_data = youtube_response.json()

# Display recommended YouTube videos
print("Wikipedia Summary:")
print(topic_summary)
print("\nRecommended YouTube Videos for", topic, ":")
for item in youtube_data['items']:
    # Print the entire item dictionary for debugging
    print(item)

    # Access video information
    video_title = item['snippet']['title']
    video_channel = item['snippet']['channelTitle']

    # Check if 'id' key exists in the item dictionary
    if 'id' in item and 'videoId' in item['id']:
        video_id = item['id']['videoId']
        video_link = f"https://www.youtube.com/watch?v={video_id}"
        print(video_title, "-", video_link, "-", video_channel)
    else:
        print(f"Skipping item without videoId: {item}")
