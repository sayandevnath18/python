from user import User


class PremiumUser(User):
    def __init__(self, name):
        super().__init__(name)
        self.__favourite_genre = None

    def set_favourite_genre(self, genre):
        self.__favourite_genre = genre

    def play_media(self, library):
        if self.__favourite_genre not in library.get_media_by_genre():
            print("No media available for this genre.")
            return

        for media in library.get_media_by_genre()[self.__favourite_genre]:
            media.play()
