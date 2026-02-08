"""Get actors that have worked at least in N movies of the data provided."""
import csv
from collections import defaultdict
import os
import pathlib

ACTOR_MIN_N_MOVIES = 10

ROOT_FOLDER = pathlib.Path(__file__).parent.parent
DATA_FILE_PATH = os.path.join(
    ROOT_FOLDER, 'res', 'data', 'movies_jap_list.csv')


def main():
    movies_data = None
    with open(DATA_FILE_PATH) as file:
        reader = csv.DictReader(file)
        movies_data = list(reader)

    actor_movies_count = defaultdict(int)
    actor_movies = defaultdict(list)
    for row in movies_data:
        for actor in row['cast'].split(','):
            actor = actor.strip()
            actor_movies_count[actor] += 1
            actor_movies[actor].append(row['title'])

    actor_movies_count = dict(sorted(
        actor_movies_count.items(), key=lambda x: (-x[1], x[0])
        ))

    for actor, count in actor_movies_count.items():
        if count >= ACTOR_MIN_N_MOVIES:
            movies_titles = ' || '.join(actor_movies[actor])
            print(f"{actor:22} --> {count:3} --> {movies_titles:22}")


if __name__ == '__main__':
    main()
