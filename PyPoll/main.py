import os
import csv

input_path = os.path.join("election_data.csv")
with open(input_path, 'r', newline='', encoding='UTF-8') as input_csv:
	reader = csv.reader(input_csv, delimiter=',')
	next(reader, None)

	candidate_votes = {}

	for row in reader:
		if row[2] not in candidate_votes:
			candidate_votes[row[2]] = 1
		else:
			candidate_votes[row[2]] += 1

	total_votes = sum(candidate_votes.values())
	winner = max(candidate_votes, key=candidate_votes.get)

	print("Election Results")
	print("-------------------------")
	print(f"Total Votes: {total_votes}")
	print("-------------------------")
	for k,v in candidate_votes.items():
		print(f"{k}: {(v/total_votes*100):.3f}% ({v})")
	print("-------------------------")
	print(f"Winner: {winner}")
	print("-------------------------")

output_path = os.path.join("election_results.txt")
with open(output_path, 'w') as output_txt:
	output_txt.write("Election Results")
	output_txt.write("\n-------------------------")
	output_txt.write(f"\nTotal Votes: {total_votes}")
	output_txt.write("\n-------------------------")
	for k,v in candidate_votes.items():
		output_txt.write(f"\n{k}: {(v/total_votes*100):.3f}% ({v})")
	output_txt.write("\n-------------------------")
	output_txt.write(f"\nWinner: {winner}")
	output_txt.write("\n-------------------------")