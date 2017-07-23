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
						"https://image.tmdb.org/t/p/w640/tcqb9NHdw9SWs2a88KCDD4V8sVR.jpg",
						"https://www.youtube.com/watch?v=d1_JBMrrYw8")
movies.append(avatar)

negotiator = media.Movie("The Negotiator",
						"Samuel L Jackson and Kevin Spacey Square off in this cop thriller",
						"https://image.tmdb.org/t/p/w640/uA1zKgJVoO0ljbSbKXyek5YbLwv.jpg",
						"https://www.youtube.com/watch?v=LJ1pS1W0XXg")
movies.append(negotiator)

def main():
	fresh_tomatoes.open_movies_page(movies)

if __name__ == '__main__':
	main()

