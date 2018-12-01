import pandas as pd
import re
from datetime import datetime

movieDetailDf = pd.read_csv("MovieDetail.csv")


def changeDateFormat(dateString):
    releaseDate = datetime.strptime(dateString,'%m-%d-%Y').strftime("%d") + " "+ datetime.strptime(dateString,'%m-%d-%Y').strftime("%B")[:3] + " "+datetime.strptime(dateString,'%m-%d-%Y').strftime("%Y")
    return releaseDate

releaseDate = input("Enter the releaseDate(mm-dd-yyyy): ")
if re.match("\\d{2}-\\d{2}-\\d{4}", releaseDate):
    releaseDate = changeDateFormat(releaseDate)
    df = movieDetailDf.loc[movieDetailDf['releaseDate'] == releaseDate][['title','releaseDate']]
    if not df.empty:
        print("Here's the list of movies released on", releaseDate)
        print(df)
    else:
        print("No movie released on", releaseDate)
else:
    print("Enter date in specified format!")