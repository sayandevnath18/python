from media import Media


class Music(Media):
    def play(self):
        print(f"Playing Music: {self.title}")

    def genre(self):
        return "Music"
