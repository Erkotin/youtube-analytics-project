class Video:
    def __init__(self, video_id, title, video_link, views, likes):
        self.video_id = video_id
        self.title = title
        self.video_link = video_link
        self.views = views
        self.likes = likes

    def __str__(self):
        return self.title


class PLVideo(Video):
    def __init__(self, video_id, title, video_link, views, likes, playlist_id):
        super().__init__(video_id, title, video_link, views, likes)
        self.playlist_id = playlist_id

    def __str__(self):
        return self.title