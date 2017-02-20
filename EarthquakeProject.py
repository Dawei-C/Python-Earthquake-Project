import requests
import csv
from operator import itemgetter

fp = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/"
fn = "all_week.csv"
r = requests.get(fp + fn)
f = open(fn, "wb")
f.write(r.text.encode("UTF-8"))
f.close()

with open(fn) as csvfile:
    reader = csv.DictReader(csvfile)
    magnitudeList = []
    placeList = []
    noInformation = []

    for row in reader:
        # skip rows that have no data on magnitude
        if row['mag'] == "":
            noInformation.append(row['place'])
            continue

        placeList.append(row['place'])
        magnitudeList.append(float(row['mag']))
        print("Location: " + row['place'] + " | Magnitude: " + row['mag'] + " | Time: " + row['time'])

    print()
    for i in noInformation:
        print(i + "'s magnitude has not been disclosed yet.")

    placeMag = list(zip(placeList, magnitudeList))
    placeMag = sorted(placeMag, key=itemgetter(1))
    topMag = placeMag[-1]
    averageMag = sum(magnitudeList)/len(magnitudeList)
    totalEQ = len(magnitudeList)
    documentedEQ = totalEQ - len(noInformation)

print()
print("There were " + str(totalEQ) + " earthquakes within the past 7 days.")
print(str(documentedEQ) + " had magnitude values that have been documented.")
print("The average magnitude was " + '{0:.2f}'.format(averageMag) + ".")
print("The location with the highest magnitude is " + str(topMag[0] + " at " + str(topMag[1]) + "."))
