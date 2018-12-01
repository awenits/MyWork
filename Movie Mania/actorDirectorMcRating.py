import pandas as pd


actorRankingDf = pd.read_csv("ActorRanking.csv")
directorRankingDf = pd.read_csv("DirectorRanking.csv")
movieDetailDf = pd.read_csv("MovieDetail.csv")


def getDirectors(movie):
    directors = movieDetailDf.loc[movieDetailDf['title'].str.lower() == movie]['directors'].values[0]
    if len(directors) != 0:
        return directors.split(" | ")
    else:
        print("Details of directors for "+ movie +" are not present.")


def getActors(movie):
    actors = movieDetailDf.loc[movieDetailDf['title'].str.lower() == movie]['actors'].values[0]
    if len(actors) != 0:
        return actors.split(" | ")
    else:
        print("Details of actors for "+ movie +" are not present.")


def getActorMovieCount(name):
    count = actorRankingDf.loc[actorRankingDf['actorName'] == name]['movieCount'].values[0]
    return count


def getDirectorMovieCount(name):
    count = directorRankingDf.loc[directorRankingDf['directorName'] == name]['movieCount'].values[0]
    return count


def getActorRating(name):
    rating = actorRankingDf.loc[actorRankingDf['actorName'] == name]['normalizedRating'].values[0]
    return rating


def getDirectorRating(name):
    rating = directorRankingDf.loc[directorRankingDf['directorName'] == name]['normalizedRating'].values[0]
    return rating


movie = input("Enter title of movie: ").lower()
all_titles = list(movieDetailDf['title'].str.lower().values)
all_actors = list(actorRankingDf['actorName'].str.lower().values)
all_directors = list(directorRankingDf['directorName'].str.lower().values)


if movie in all_titles:
    print("Title:       ",movie.capitalize())
    print()
    movieDirectors = getDirectors(movie)
    print("########Details of directors(Number of movies and Rating)########")
    for director in movieDirectors:
        if director.lower() in all_directors:
            print(director,"directed", getDirectorMovieCount(director),"movies and rating is", "{0:.2f}".format(getDirectorRating(director)))
        else:
            print("No details available for", director)
    print()
    movieActors = getActors(movie)
    print("########Details of actors(Number of movies and Rating)########")
    for actor in movieActors:
        if actor.lower() in all_actors:
            print(actor,"worked in", getActorMovieCount(actor),"movies and rating is", "{0:.2f}".format(getActorRating(actor)))
        else:
            print("No details available for", actor)
else:
    print("Sorry! No details available for", movie.capitalize())