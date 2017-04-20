import webbrowser


# Define the class of Movie()
class Movie():
    "This class provides a way to store"
    "movie related information"

    # Define __init__. When a new instance of Movie() is created,
    # this function will be called
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        # Four attributes of the instance are defined by the
        # parameters in the parentheses
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # Define the instance method show_trailer, which opens the
    # webbrowser to show the trailer of the instance when called
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

