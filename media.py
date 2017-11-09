import webbrowser
class Movie():
    def __init__(self,mov_title,mov_storyline,poster_image,trailer_yt):
        self.title = mov_title
        self.storyline = mov_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_yt
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
