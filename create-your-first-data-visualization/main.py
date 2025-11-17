import matplotlib.pyplot as plt

# Let's rank some of our favorite snacks
snack_scores = [100, 80, 60]
slice_labels = ["Chips", "Spicy Peanuts", "Reese's Cups"]

# Let's make a pie chart!
plt.pie(snack_scores, labels=slice_labels)

# Give your pie chart a title in the quotes
plt.title("Cat's Favorite Snacks")

# Put the name of your file in the quotes and give it a .png extension
plt.savefig("Cats_Favorite_Snacks.png")