import csv

class Data:
    zero_min = ''
    one_min = ''
    two_min = ''
    three_min = ''
    four_min = ''

    def __init__(self, filename, offset, species):
        self.filename = filename
        self.offset = offset
        self.species = species

    def set_offset(self, new_offset):
        self.offset = new_offset

    def label_offset(self):
        self.offset = int(self.offset / 60)
        if self.offset == 0:
            self.zero_min = 'X'
        elif self.offset == 1:
            self.one_min = 'X'
        elif self.offset == 2:
            self.two_min = 'X'
        elif self.offset == 3:
            self.three_min = 'X'
        elif self.offset == 4:
            self.four_min = 'X'

    def create_data_row(self):
        new_row_array = []

        first_columns = self.filename.split("-")

        new_row_array.append(first_columns[0])
        new_row_array.append(first_columns[1])
        new_row_array.append(first_columns[2])

        new_row_array[2] = new_row_array[2][:-4]

        new_row_array.append('')
        new_row_array.append('')
        new_row_array.append(self.species)
        new_row_array.append('')
        new_row_array.append(self.zero_min)
        new_row_array.append(self.one_min)
        new_row_array.append(self.two_min)
        new_row_array.append(self.three_min)
        new_row_array.append(self.four_min)
        new_row_array.append('')
        new_row_array.append('')
        new_row_array.append('')
        new_row_array.append('')
        new_row_array.append('')

        return new_row_array


header = ["Full name", "Unit", "File Name Y/M/D", "File Time", "Initials", "Date", "Species", "No. Ind.", "Second/Offset Detected", "TMTC", "VT", "TBC", "Comment", "Verified"]

final_header = ["Unit", "File Name Y/M/D", "File Time", "Initials", "Date", "Species", "No. Ind.", "0min", "1min", "2min", "3min", "4min", "TMTC", "VT", "TBC", "Comment", "Verified"]


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

                row_array.insert(0, filename)       # insert filename to the beginning of list

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