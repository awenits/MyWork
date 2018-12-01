import pandas as pd


movieDetailDf = pd.read_csv("MovieDetail.csv")


def searchGenre(genre):
    for idx, row in movieDetailDf.iterrows():
        if isinstance(row['genre'], str):
            if genre in row['genre']:
                print(row['title'])

genre = input("Enter genre: ").capitalize()
searchGenre(genre)