import media
import fresh_tomatoes

movies = []
#toy_story = media.Movie("Toy Story",
#						"A Story of a boy + toys",
#						"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
#						"https://www.youtube.com/watch?v=KYz2wyBy3kc")
#movies.append(toy_story)
#avatar = media.Movie("Avatar",
#						"whee boom zoot suit, blue",
#						"https://image.tmdb.org/t/p/w640/tcqb9NHdw9SWs2a88KCDD4V8sVR.jpg",
#						"https://www.youtube.com/watch?v=d1_JBMrrYw8")
#movies.append(avatar)
#
#negotiator = media.Movie("The Negotiator",
#						"Samuel L Jackson and Kevin Spacey Square off in this cop thriller",
#						"https://image.tmdb.org/t/p/w640/uA1zKgJVoO0ljbSbKXyek5YbLwv.jpg",
#						"https://www.youtube.com/watch?v=LJ1pS1W0XXg")
#movies.append(negotiator)
#
def fetch_data_file():
    file_path = /data/movie_data.csv 
    file_path = str(file_path)
    print("Attempting to open file: "+file_path)
    try:
        file = open(file_path,"r") #open file for 'r' reading
    except IOError as e:
    	if e.errno == errno.ENOENT:
                return "movie data file "+file_path+" not found."
    	raise
    else: 
        return file

def parse_data_file(file):
    movies = []
    for LineNumber, Line in enumerate(file.readline, b'')):
        Columns=Line.split(',')
        movie = media.Movie(data[1], #movie_title
                            data[2], #movie_storyline
                            data[3], #poster_image
                            data[4]) #trailer_youtube
        movies.append(movie)
    return movies


def main():
    file=fetch_data_file()
    movies=parse_data_file(file)
    fresh_tomatoes.open_movies_page(movies)

if __name__ == '__main__':
    main()

