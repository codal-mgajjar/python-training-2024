import csv

# writing in csv

fields = ["name", "branch", "year"]
rows = [["Meshw", "CE", 7], ["Yash", "CE", 5]]
filename = "week-3/22_jan/temp.csv"
with open(filename, "w") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)

# reading csv


fields = []
rows = []

with open("week-3/22_jan/temp.csv", "r") as csvfile:
    csvreader = csv.reader(csvfile)

    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)

    for row in rows[:5]:
        # parsing each column of a row
        for col in row:
            print("%10s" % col, end=" "),
        print("\n")


# reading csv using pandas

import pandas as pd

df = pd.read_csv("week-3/22_jan/temp.csv")
print(df)

# writing csv using pandas

mydict = [
    {"branch": "COE", "cgpa": "9.0", "name": "Nikhil", "year": "2"},
    {"branch": "COE", "cgpa": "9.1", "name": "Sanchit", "year": "2"},
    {"branch": "IT", "cgpa": "9.3", "name": "Aditya", "year": "2"},
    {"branch": "SE", "cgpa": "9.5", "name": "Sagar", "year": "1"},
    {"branch": "MCE", "cgpa": "7.8", "name": "Prateek", "year": "3"},
    {"branch": "EP", "cgpa": "9.1", "name": "Sahil", "year": "2"},
]

df = pd.DataFrame(mydict)

df.to_csv("week-3/22_jan/output.csv", index=False)
