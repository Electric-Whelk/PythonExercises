import os
import csv


with open("caterwaul.csv", "w", newline='') as f:
    q = csv.writer(f,
                   delimiter = ",")
    q.writerow(["one",
                "two",
                "three"])
    q.writerow(["four",
                "five",
                "six"])

with open("caterwaul.csv", "r") as f:
    r = csv.reader(f, delimiter=",")
    for squiggle in r:
        print(",".join(squiggle))
