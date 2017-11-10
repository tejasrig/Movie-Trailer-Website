import webbrowser
<<<<<<< HEAD


# Class to hold Movie instances
class Movie():
    """This class holds the attributes needed for a movie"""
    def __init__(self, mov_title, mov_storyline, poster_image, trailer_yt):
=======
class Movie(): # Class to hold Movie instances
    """This class holds the attributes needed for a movie"""
    def __init__(self,mov_title,mov_storyline,poster_image,trailer_yt):
>>>>>>> 74a448043698713b661723b7cc17341f4c4d2f25
        self.title = mov_title
        self.storyline = mov_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_yt

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
