import pandas

data = pandas.read_csv("day-25/2018.csv")
grey = data["Primary Fur Color"][data["Primary Fur Color"] == "Gray"].count()
red = data["Primary Fur Color"][data["Primary Fur Color"] == "Cinnamon"].count()
black = data["Primary Fur Color"][data["Primary Fur Color"] == "Black"].count()

counter = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [grey, red, black]
}
df = pandas.DataFrame(counter)
df.to_csv("day-25/squirrel_count.csv")