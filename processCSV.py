import csv


# Declare class to make things easier
class entry:
	def __init__(self, BSSID, LAT, LONG):
		self.BSSID = BSSID
		self.LAT = LAT
		self.LONG = LONG

# LIst of entries
entries = []


""" 
Data formatted as id,BSSID,EMPTY,EMPTY,LAT,LONG,openbmap,num,date,date.
Only need three data points, so data needs to be isolated
"""
with open('wifi_zone.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        data = entry(row[1],row[4],row[5])
        entries.append(data)


# Writing processed data to CSV file
with open('processed.csv', mode = 'w') as processedfile:
    writer = csv.writer(processedfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for data in entries:
    	writer.writerow([data.BSSID, data.LAT, data.LONG])
