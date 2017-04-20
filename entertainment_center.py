import media
import fresh_tomatoes

# Create the first instance of movie class
the_shawshank_redemption = media.Movie("The Shawshank Redemption", '''Two imprisoned men bond over a number of years,
                                        finding solace and eventual redemption through acts of common decency.''',
                                       "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
                                       "https://www.youtube.com/watch?v=NmzuHjWmXOc")

# Create the second instance of movie class
twelve_angry_men = media.Movie("12 Angry Men",'''A story of a jury made up of 12 men as they deliberate the guilt or acquittal
                           of a defendant on the basis of reasonable doubt.''',
                           "https://upload.wikimedia.org/wikipedia/en/9/91/12_angry_men.jpg",
                           "https://www.youtube.com/watch?v=A7CBKT0PWFA")

# Create the third instance of movie class
pulp_fiction = media.Movie("Pulp Fiction",'''The lives of two mob hit men, a boxer, a gangster's wife, and a pair of diner bandits
                           intertwine in four tales of violence and redemption.''',
                           "https://upload.wikimedia.org/wikipedia/en/3/3b/Pulp_Fiction_%281994%29_poster.jpg",
                           "https://www.youtube.com/watch?v=s7EdQ4FqbhY")

# Create the fourth instance of movie class
goodfellas = media.Movie("Goodfellas", '''The rise and fall of mob associate Henry Hill and his friends over a period from
                         1955 to 1980.''', "https://upload.wikimedia.org/wikipedia/en/7/7b/Goodfellas.jpg",
                         "https://www.youtube.com/watch?v=qo5jJpHtI1Y")

# Create the fifth instance of movie class
it_is_a_wonderful_life = media.Movie("It's a Wonderful Life", '''An angel is sent from Heaven to help a desperately frustrated
                                     businessman by showing him what life would have been like if he had never existed.''',
                                     "https://upload.wikimedia.org/wikipedia/en/9/95/Its_A_Wonderful_Life_Movie_Poster.jpg",
                                     "https://www.youtube.com/watch?v=ewe4lg8zTYA")

# Create the sixth instance of movie class
life_is_beautiful = media.Movie("Life Is Beautiful", '''When an open-minded Jewish librarian and his son become victims of the
                                Holocaust, he uses a perfect mixture of will, humor and imagination to protect his son from
                                the dangers around their camp.''',
                                "https://vignette1.wikia.nocookie.net/disney/images/b/bb/Life_is_Beautiful.jpg/revision/latest?cb=20121111011203",
                                "https://www.youtube.com/watch?v=pAYEQP8gx3w")


# Create a list to store all the movie instances
movies = [the_shawshank_redemption, twelve_angry_men, pulp_fiction, goodfellas, it_is_a_wonderful_life, life_is_beautiful]

# Open the movie trailer website based on the data served by the movie instances list
fresh_tomatoes.open_movies_page(movies)

