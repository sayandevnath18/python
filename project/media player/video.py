from media import Media


class Video(Media):
    def play(self):
        print(f"Playing Video: {self.title}")

    def genre(self):
        return "Video"
