from user import User


class FreeUser(User):
    def play_media(self, library):
        for media in library.get_media_items():
            media.play()
