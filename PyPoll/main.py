import os
import csv

pypoll_csv = os.path.join("..", "Resources", "election_data.csv")

total_votes = 0
candidate_list = []
candidate_dict = {}

with open(pypoll_csv, newline='') as csvfile:

   csvreader = csv.reader(csvfile, delimiter =',')
   csv_header = next(csvreader)

   for row in csvreader:

       total_votes = total_votes + 1

       candidate_name = (row[2])
       if candidate_name not in candidate_list:
           candidate_list.append(candidate_name)
           candidate_dict[candidate_name] = 0
       else:
           candidate_dict[candidate_name] += 1

print("Election Results")
print("----------------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------------")
for candidate in candidate_dict:
    print(candidate + ": " + str(round(candidate_dict[candidate]/total_votes * 100,2)) + "% (" + str(candidate_dict[candidate]) + ")")
print("----------------------------------")
print(f"Winner: {(list(candidate_dict.keys())[0])}")
print("----------------------------------")

with open("pypoll.txt", "w", newline='') as f:
    f.write("Election Results\n")
    f.write("----------------------------------\n")
    f.write(f"Total Votes: {total_votes}\n")
    f.write("----------------------------------\n")
    for candidate in candidate_dict:
        f.write(candidate + ": " + str(round(candidate_dict[candidate] / total_votes * 100, 2)) + "% (" + str(
            candidate_dict[candidate]) + ")\n")
    f.write("----------------------------------\n")
    f.write(f"Winner: {(list(candidate_dict.keys())[0])}\n")
    f.write("----------------------------------")