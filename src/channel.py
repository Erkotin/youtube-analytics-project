from helper.youtube_api_manual import youtube, printj
import json



class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.title = ''
        self.description = ''
        self.url = ''
        self.subscriber_count = 0
        self.video_count = 0
        self.view_count = 0
        self._fetch_channel_data()

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        printj(channel)

    def _fetch_channel_data(self) -> None:
        """Заполняет атрибуты экземпляра реальными данными канала."""
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        channel_info = channel['items'][0]

        self.title = channel_info['snippet']['title']
        self.description = channel_info['snippet']['description']
        self.url = f"https://www.youtube.com/channel/{self.channel_id}"
        self.subscriber_count = int(channel_info['statistics']['subscriberCount'])
        self.video_count = int(channel_info['statistics']['videoCount'])
        self.view_count = int(channel_info['statistics']['viewCount'])

    @classmethod
    def get_service(cls):
        """Возвращает объект для работы с YouTube API."""
        return youtube

    def to_json(self, file_name: str) -> None:
        """Сохраняет значения атрибутов экземпляра в JSON-файл."""
        data = {
            'channel_id': self.channel_id,
            'title': self.title,
            'description': self.description,
            'url': self.url,
            'subscriber_count': self.subscriber_count,
            'video_count': self.video_count,
            'view_count': self.view_count
        }

        with open(file_name, 'w') as file:
            json.dump(data, file, indent=4)
