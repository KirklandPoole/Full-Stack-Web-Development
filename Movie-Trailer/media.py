
import webbrowser

# Movie class


class Movie():
    # Constructor
    def __init__(self,
                 movie_title,
                 movie_storyline,
                 movie_poster_image,
                 movie_trailer_youtube,
                 movie_director,
                 movie_rating,
                 movie_release_date):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster_image
        self.trailer_youtube_url = movie_trailer_youtube
        self.director = movie_director
        self.rating = movie_rating
        self.releasedate = movie_release_date

    # display movie poster using url provided
    def show_poster(self):
        webbrowser.open(self.poster_image_url)

    # display movie trailer using url provided
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
