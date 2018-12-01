#not adding check for whether two movie names are same
#check if both the movies present in dataframe then only proceed
#fetch the name of actors from movie 1 and 2 and display common
#fetch the names of directors from movie 1 and 2 and display common

import pandas as pd


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


#returns common elements from two lists
def findCommon(l1, l2):
    s1 = set(l1)
    s2 = set(l2)
    return list(s1.intersection(s2))


print("Enter two movie names..")
movie1 = input("1st movie title plz..: ").lower()
movie2 = input("2nd movie title plz..: ").lower()

all_titles = list(movieDetailDf['title'].str.lower().values)

if movie1 in all_titles and movie2 in all_titles:
    #for common actors
    actorsMovie1 = getActors(movie1)
    actorsMovie2 = getActors(movie2)
    commonActors = findCommon(actorsMovie1, actorsMovie2)
    if len(commonActors) != 0:
        print("Common actors in "+movie1+" and "+movie2)
        for actor in commonActors:
            print("  " + actor)
    else:
        print(movie1+" and "+movie2+" dont have common actors.")

    #for common directors
    directorsMovie1 = getDirectors(movie1)
    directorsMovie2 = getDirectors(movie2)
    commonDirectors = findCommon(directorsMovie1, directorsMovie2)
    if len(commonDirectors) != 0:
        print("Common directors in "+movie1.capitalize()+" and "+movie2.capitalize())
        for director in commonDirectors:
            print("  " + director)
    else:
        print(movie1+" and "+movie2+" dont have common directors.")
else:
    print("Seems like i dont have details of these movies.Please enter different movie names..!")
