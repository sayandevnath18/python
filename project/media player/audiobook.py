from media import Media


class AudioBook(Media):
    def play(self):
        print(f"Playing AudioBook: {self.title}")

    def genre(self):
        return "AudioBook"
