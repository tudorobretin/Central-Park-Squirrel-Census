import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey = len(data[data["Primary Fur Color"] == "Gray"])
red = len(data[data["Primary Fur Color"] == "Cinnamon"])
black = len(data[data["Primary Fur Color"] == "Black"])

colors = {
    "Fur color": ["Grey", "Red", "Black"],
    "Number": [grey, red, black]
}

colors_df = pandas.DataFrame(colors)

colors_df.to_csv("squirrel_count.csv")