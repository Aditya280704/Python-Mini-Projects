import pandas

data = pandas.read_csv("weather_data.csv")
print(data)
print(type(data))
# # Get hold of single column
print(data["temp"])
print(type(data["temp"]))

# Conversion to dictionary
data_to_dict = data.to_dict()
print(data_to_dict)

temp_list = data["temp"].to_list()
print(temp_list)

# Calculate average temperatures
print(sum(temp_list)/len(temp_list))

# From pandas method
print(data["temp"].mean())

# Max value
print(data["temp"].max())

# Get data in columns
print(data["condition"])  # Method-1
print(data.condition)   # Method-2


# Get data in row
print(data[data.day == "Monday"])

print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)

# Convert temp to fahrenheit
monday_temp = monday.temp[0]
monday_temp_f = monday_temp * 9/5 +32
print(monday_temp_f)


# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")
