import media
import index

avengers = media.Movie("Avengers","Super Hero","https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg","https://www.youtube.com/watch?v=eOrNdBpGMv8")

#print(avengers.storyline)
#avengers.show_trailer()

avatar = media.Movie("Avatar","alien planet","https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg","https://www.youtube.com/watch?v=5PSNL1qE6VY")

#print(avatar.storyline)
#avatar.show_trailer()

school_of_rock = media.Movie("School of Rock","Using rock music to learn","https://upload.wikimedia.org/wikipedia/en/thumb/1/11/School_of_Rock_Poster.jpg/220px-School_of_Rock_Poster.jpg","https://www.youtube.com/watch?v=3PsUJFEBC74")

mi5 = media.Movie("Mission impossible","mi","https://upload.wikimedia.org/wikipedia/en/f/fb/Mission_Impossible_Rogue_Nation_poster.jpg","https://www.youtube.com/watch?v=gOW_azQbOjw")

ff5 = media.Movie("fast and furious","ff5","https://upload.wikimedia.org/wikipedia/en/thumb/0/0c/Fast_Five_poster.jpg/220px-Fast_Five_poster.jpg","https://www.youtube.com/watch?v=mw2AqdB5EVA")

ff7 = media.Movie("fate of the furious","fate of the furious","https://upload.wikimedia.org/wikipedia/en/2/2d/The_Fate_of_The_Furious_Theatrical_Poster.jpg","https://www.youtube.com/watch?v=9GvX2uexGkA")

movies = [avengers,avatar,school_of_rock,mi5,ff5,ff7]
index.open_movies_page(movies)
