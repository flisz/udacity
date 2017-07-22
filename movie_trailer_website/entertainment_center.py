import media
import fresh_tomatoes

movies = []
toy_story = media.Movie("Toy Story",
						"A Story of a boy + toys",
						"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
						"https://www.youtube.com/watch?v=KYz2wyBy3kc")
movies.append(toy_story)
avatar = media.Movie("Avatar",
						"whee boom zoot suit, blue",
						"http://www.joblo.com/movie-posters/2009/avatar#image-27654",
						"https://www.youtube.com/watch?v=d1_JBMrrYw8")
movies.append(avatar)

negotiator = media.Movie("The Negotiator",
						"Samuel L Jackson and Kevin Spacey Square off in this cop thriller",
						"http://www.imdb.com/title/tt0120768/mediaviewer/rm2723625216",
						"https://www.youtube.com/watch?v=LJ1pS1W0XXg")
movies.append(negotiator)

def main():
	fresh_tomatoes.open_movies_page(movies)

if __name__ == '__main__':
	main()

