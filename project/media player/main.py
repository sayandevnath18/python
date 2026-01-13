from audiobook import AudioBook
from freeuser import FreeUser
from library import Library
from music import Music
from premiumuser import PremiumUser
from video import Video


music1 = Music("Music Track 1", "3.45", "Author: Phitron")
music2 = Music("Music Track 2", "5.52", "Author: Phitron")
video1 = Video("Video Track 1", "45.56", "Artist: T-Series")
audio1 = AudioBook("AudioBook Track 1", "30.34", "Author: Programming Hero")

library = Library()
library.add_media(music1)
library.add_media(music2)
library.add_media(video1)
library.add_media(audio1)

free_user = FreeUser("Kamal")
premium_user = PremiumUser("Kamal")
premium_user.set_favourite_genre("Music")

print("\nFree User:")
free_user.play_media(library)

print("\nPremium User:")
premium_user.play_media(library)
