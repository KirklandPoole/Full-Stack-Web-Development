import media
import fresh_tomatoes


# Author: Kirk Poole
# Project 1 for the Full Stack Web Development Nanodegree at Udacity.
# Display information about favorite movies and will show the movie trailer.
#
# class constructor: media.Movie() required parameters are:
#        movie title
#        movie storyline
#        movie poster image (url)
#        movie trailer (youtube url)
#        movie director
#        movie rating
#        movie release date (year)
# Create instances using the class constructor media.Movie()
live_die_repeat = media.Movie("Edge Of Tomorrow",
                              "Live. Die. Repeat",
                              "http://upload.wikimedia.org/wikipedia/en/f/f9/Edge_of_Tomorrow_Poster.jpg",
                              "https://www.youtube.com/watch?v=vw61gCe2oqI",
                              "Doug Liman",
                              "PG-13",
                              "2014")
dark_knight = media.Movie("The Dark Knight", "Batman meets a different kind of criminal",
                          "http://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
                          "https://www.youtube.com/watch?v=EXeTwQWrcwY",
                          "Christopher Nolan",
                          "PG-13",
                          "2008")
enders_game = media.Movie("Ender's Game",
                          "A boy must save the world",
                          "http://upload.wikimedia.org/wikipedia/en/8/8c/Ender%27s_Game_poster.jpg",
                          "https://www.youtube.com/watch?v=2UNWLgY-wuo",
                          "Gavin Hood",
                          "PG-13",
                          "2013")
avatar = media.Movie("Avatar Story",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ",
                     "James Cameron",
                     "PG-13",
                     "2009")
dangerous_liaisons = media.Movie("Dangerous Liaisons",
                                 "Pre-Revolution French at play, ...and war",
                                 "http://upload.wikimedia.org/wikipedia/en/6/6d/DangerousLiaisonsPoster.jpg",
                                 "https://www.youtube.com/watch?v=zUCvWG86-tM",
                                 "Stephen Frears",
                                 "R",
                                 "1988")
space_Odyssey_2001 = media.Movie("2001: A Space Odyssey",
                                 "My God, it's full of stars...",
                                 "http://upload.wikimedia.org/wikipedia/en/e/ef/2001_A_Space_Odyssey_Style_B.jpg",
                                 "https://www.youtube.com/watch?v=UqOOZux5sPE",
                                 "Stanley Kubrick",
                                 "G",
                                 "1968")
# Put instances into an array
movies = [live_die_repeat,
          dark_knight,
          enders_game,
          avatar,
          dangerous_liaisons,
          space_Odyssey_2001]
# Call fresh_tomatoes.open_movies_page and pass in the array of movies to be displayed in the web page.
fresh_tomatoes.open_movies_page(movies)
