import matplotlib.pyplot as plt

snack_scores = [100,80,60]

slice_labels = ["Chips", "Spicy Peanuts", "Reese's Cups"]

colors = ["#FAFAD2","#B22222","#FFA07A"]

plt.pie(snack_scores, labels=slice_labels, colors=colors)

plt.title("Snack Scores", fontsize=22)

plt.savefig("snack_scores.png")