import media

toy_story = media.Movie("Toy Story",
						"A Story of a boy + toys",
						"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
						"https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
						"whee boom zoot suit, blue",
						"http://www.joblo.com/movie-posters/2009/avatar#image-27654",
						"https://www.youtube.com/watch?v=d1_JBMrrYw8")

def main():
	print(avatar.storyline)
	avatar.showtrailer()

if __name__ == '__main__':
	main()

