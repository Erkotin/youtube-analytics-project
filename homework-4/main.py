from src.video import Video, PLVideo

if __name__ == '__main__':
    # Создаем два экземпляра класса
    video1 = Video('AWX4JnAnjBE', 'GIL в Python: зачем он нужен и как с этим жить',
                   'https://www.youtube.com/watch?v=AWX4JnAnjBE', 10000, 500)  # 'AWX4JnAnjBE' - это id видео из ютуб
    video2 = PLVideo('4fObz_qw9u4', 'MoscowPython Meetup 78 - вступление',
                     'https://www.youtube.com/watch?v=4fObz_qw9u4', 20000, 1000,
                     'PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC')
    assert str(video1) == 'GIL в Python: зачем он нужен и как с этим жить'
    assert str(video2) == 'MoscowPython Meetup 78 - вступление'


