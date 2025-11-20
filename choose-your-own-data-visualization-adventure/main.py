import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

with open("books.csv","r", encoding="utf-8") as datafile:
    data = pd.read_csv(datafile,delimiter=",", on_bad_lines='skip')

data["rating_rounded"] = data["average_rating"].round()

data_pivoted = data.pivot_table(values="ratings_count", index=["language_code"], columns=["rating_rounded"])

fig = sns.heatmap(data_pivoted, annot=True, cmap="coolwarm", fmt='g')


plt.xlabel("Language")
plt.ylabel("Average Rating(Rounded)")
plt.title("Popularity (Ratings Count) by Language & Rating")
plt.savefig("books_heatmap.png")