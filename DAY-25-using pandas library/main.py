# with open("weather_data.csv")as data_files:
#     data = data_files.readlines()
#     print(data)

import csv

with open("weather_data.csv")as data_file:
    data = csv.reader(data_file)
    temperatures = []
    print(data)
    for row in data:
        # print(row)
        # print(row[1])
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)
