import requests
import os

class Video:
    def __init__(self, video_id):
        self.video_id = video_id
        self._fetch_video_data()

    def _fetch_video_data(self):
        api_key = os.getenv('API_KEY')  # Replace 'YOUR_API_KEY' with your actual YouTube API key
        url = f'https://www.googleapis.com/youtube/v3/videos?id={self.video_id}&key={api_key}&part=snippet,statistics'
        response = requests.get(url)
        data = response.json()

        if 'items' in data and len(data['items']) > 0:
            item = data['items'][0]
            snippet = item['snippet']
            statistics = item['statistics']

            self.title = snippet['title']
            self.link = f"https://www.youtube.com/watch?v={self.video_id}"
            self.views = int(statistics['viewCount'])
            self.likes = int(statistics['likeCount'])
        else:
            raise ValueError(f"Video with ID '{self.video_id}' not found on YouTube.")

    def __str__(self):
        return self.title


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id

    def __str__(self):
        return self.title
