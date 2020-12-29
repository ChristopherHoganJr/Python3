import pandas as pd

# read csv with pandas and save to variable
data = pd.read_csv('CPSC.csv')

# Count how many of each are in the "Primary Fur Color" column
grey_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])

# Save findings to a python dictionary
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels, cinnamon_squirrels, black_squirrels]
}

# Convert python dictionary to pandas data frame
df = pd.DataFrame(data_dict)

# Export pandas data frame to a csv file
df.to_csv("squirrel_count.csv")