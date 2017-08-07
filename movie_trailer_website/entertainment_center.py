import media
import fresh_tomatoes
import errno
import csv

def fetch_data_file():
    file_path = "data/movie_data.csv"
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
    reader = csv.reader(file)
    print(reader)
    for RowNumber, Data in enumerate(reader):
        movie = media.Movie(Data[0], #movie_title
                            Data[1], #movie_storyline
                            Data[2], #poster_image
                            Data[3]) #trailer_youtube
        movies.append(movie)
    return movies


def main():
    file=fetch_data_file()
    movies=parse_data_file(file)
    fresh_tomatoes.open_movies_page(movies)

if __name__ == '__main__':
    main()

