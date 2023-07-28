import csv

header = ["Unit", "File Name Y/M/D", "File Time", "Initials", "Date", "Species", "No. Ind.", "Second/Offset Detected", "TMTC", "VT", "TBC", "Comment", "Verified"]

with open('new_cluster.csv', 'w') as new_file:
    csv_writer = csv.writer(new_file)
    csv_writer.writerow(header)

    with open('cluster.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        for line in csv_reader:
            if line[15] == 'Carolina Wren':
                filename = line[2]
                row_array = filename.split("_")
                
                row_array[2] = row_array[2][:-4]    # remove the .wav extension from the times of the detections

                row_array.append('')
                row_array.append('')
                row_array.append(line[15])
                row_array.append('')
                row_array.append(line[4])
                row_array.append('')
                row_array.append('')
                row_array.append('')
                row_array.append('')
                row_array.append('')
                    
                csv_writer.writerow(row_array)