import os
import csv

def average(numlist):
	return sum(numlist)/len(numlist)
	
input_path = os.path.join("budget_data.csv")
with open(input_path, 'r', newline='', encoding='utf-8') as input_csv:
	reader = csv.reader(input_csv, delimiter=',')
	#skip header row
	next(reader, None)
	
	total_months = 0
	net_profit = 0
	changes = []

	#will store all rows of csv for later use
	csv_contents = []

	for row in reader:
		csv_contents.append(row)
		total_months += 1
		net_profit += int(row[1])

		#calculate monthly change and add to "changes" list, but skip first month because N/A
		if total_months != 1:
			changes.append(int(row[1])-previous_profit)

		#set previous_profit to this month's profit, for next calculation
		previous_profit = int(row[1])

	average_change = average(changes)
	greatest_increase = max(changes)
	greatest_decrease = min(changes)

	#get GI,GD months using stored contents. Add +1 because "csv_contents" starts at 1st month but "changes" starts at 2nd month
	month_of_GI = csv_contents[changes.index(greatest_increase)+1][0]
	month_of_GD = csv_contents[changes.index(greatest_decrease)+1][0]

	print("Financial Analysis")
	print("--------------------------")
	print(f"Total Months: {total_months}")
	print(f"Total: ${net_profit}")
	print(f"Average Change: ${average_change:.2f}")
	print(f"Greatest Increase in Profits: {month_of_GI} (${greatest_increase})")
	print(f"Greatest Decrease in Profits: {month_of_GD} (${greatest_decrease})")

output_path = os.path.join("budget_results.txt")
with open(output_path, 'w') as output_txt:
	output_txt.write("Financial Analysis")
	output_txt.write("\n--------------------------")
	output_txt.write(f"\nTotal Months: {total_months}")
	output_txt.write(f"\nTotal: ${net_profit}")
	output_txt.write(f"\nAverage Change: ${average_change:.2f}")
	output_txt.write(f"\nGreatest Increase in Profits: {month_of_GI} (${greatest_increase})")
	output_txt.write(f"\nGreatest Decrease in Profits: {month_of_GD} (${greatest_decrease})")

