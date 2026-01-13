class Library:
    def __init__(self):
        self.__media_items = []
        self.__media_by_genre = {}

    def add_media(self, media):
        self.__media_items.append(media)
        self.__media_by_genre.setdefault(media.genre(), []).append(media)

    def get_media_items(self):
        return self.__media_items

    def get_media_by_genre(self):
        return self.__media_by_genre
