import json
import requests

def create_genre_data():
    genre_data = []


    url = "https://api.themoviedb.org/3/genre/movie/list?api_key=16d1729d729f6d8c5d36bfaba0aee1a6&language=ko-KR"
    res = requests.get(url).json()
    genres = res["genres"]

    for genre in genres:
        tmp = {
            'model': 'movies.genre',
            'pk': genre['id'],
            'fields': {
                'name': genre['name'],
            }
        }
        genre_data.append(tmp)

    file = open("fixtures/genredata.json", "w", encoding="UTF-8") 

    with file as f:
        file.write(json.dump(genre_data, f, indent=4, ensure_ascii=False))


def create_movie_data():
    # with open('fixtures/moviedata.json', 'r+') as f:
    #     movie_data = json.load(f)

    movie_data = []

    for page in range(1, 51):
        url = "https://api.themoviedb.org/3/movie/popular?api_key=16d1729d729f6d8c5d36bfaba0aee1a6&language=ko-KR&page=" + str(page)
        res = requests.get(url).json()
        movies = res["results"]

        for movie in movies:
            if movie.get('release_date') == "" or movie.get('poster_path') == "":
                continue

            movie.pop('adult')
            movie.pop('backdrop_path')
            movie.pop('original_language')
            movie.pop('original_title')
            movie.pop('popularity')
            movie.pop('video')

            tmp = {
                'model': 'movies.movie',
                'pk': movie.pop('id'),
                'fields': movie,
            }
            movie_data.append(tmp)

    file = open("fixtures/moviedata.json", "w", encoding="UTF-8") 

    with file as f:
        file.write(json.dump(movie_data, f, indent=4, ensure_ascii=False))

create_genre_data()
# create_movie_data()