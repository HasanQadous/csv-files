import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
colors = data["Primary Fur Color"]
gray = []
black = []
cinnamon = []
for color in colors:
    if color == "Gray":
        gray.append(color)
    elif color == "Black":
        black.append(color)
    elif color == "Cinnamon":
        cinnamon.append(color)

dic = {
    "color": ["gray", "black", "cinnamon"],
    "count": [len(gray), len(black), len(cinnamon)]
}
color_data = pandas.DataFrame(dic)
color_data.to_csv("color_data.csv")






