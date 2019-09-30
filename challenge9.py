import csv
# 1

content = []
f = open("idea.txt", "r")
content.append(f.read())
f.close()
print(content)

# 2
ans = input("世界で一番人口の多い国はどこですか？：")
fi = open("ans.txt", "w")
fi.write(ans)
fi.close()

# 3
movies = [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]
with open("movie.csv", "w") as f:
    w = csv.writer(f, delimiter=",")
    for i, item in enumerate(movies):
        w.writerow(movies[i])