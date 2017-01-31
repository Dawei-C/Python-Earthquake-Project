import requests
import csv

fp = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/"
fn = "all_week.csv"
r = requests.get(fp + fn)
f = open(fn, "wb")
f.write(r.text.encode("UTF-8"))
f.close()

with open(fn) as csvfile:
    reader = csv.DictReader(csvfile)
    magnitudeList = []
    for row in reader:
        magnitudeList.append(float(row['mag']))
        print("Location: " + row['place'] + " | Magnitude: " + row['mag'] + " | Time: " + row['time'])

    averageMag = sum(magnitudeList)/len(magnitudeList)

print()
print("There were " + str(len(magnitudeList)) + " earthquakes this week.")
print("The average magnitude is " + '{0:.2f}'.format(averageMag) + ".")
print("The highest magnitude was " + str(max(magnitudeList)) + ".")
