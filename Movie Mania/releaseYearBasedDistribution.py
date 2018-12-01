#task2 extended for release year
#search movies based on releaseYear
import pandas as pd
import re
from datetime import datetime

movieDetailDf = pd.read_csv("MovieDetail.csv")

releaseYear = input("Enter the releaseYear(yyyy): ")
if re.match("\\d{4}", releaseYear):
    releaseYear = int(releaseYear)
    df = movieDetailDf.loc[movieDetailDf['releaseYear'] == releaseYear][['title','releaseDate']]
    if not df.empty:
        print("Here's the list of movies released in year", releaseYear)
        print(df)
    else:
        print("No Details available for movies released in year", releaseYear)
else:
    print("Enter release year in specified format!")