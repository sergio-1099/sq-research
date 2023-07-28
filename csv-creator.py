import csv

header = ["Unit", "File Name Y/M/D", "File Time", "Initials", "Date", "Species", "No. Ind.", "Second/Offset Detected", "TMTC", "VT", "TBC", "Comment", "Verified"]

with open('new_cluster.csv', 'w') as new_file:
    csv_writer = csv.writer(new_file)
    csv_writer.writerow(header)

    with open('cluster.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        