import csv

def main():
    with open('budget_data.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader)
        total_months = 0
        total_profit = 0
        previous_profit = 0
        change_profit = 0
        change_list = []
        for row in csvreader:
            total_months += 1
            total_profit += int(row[1])
            change_profit = int(row[1]) - previous_profit
            change_list.append(change_profit)
            previous_profit = int(row[1])
        average_change = sum(change_list) / len(change_list)
        max_change = max(change_list)
        min_change = min(change_list)
        max_change_date = change_list.index(max_change) + 1
        min_change_date = change_list.index(min_change) + 1
        print('Financial Analysis')
        print('----------------------------')
        print('Total Months: ' + str(total_months))
        print('Total: $' + str(total_profit))
        print('Average Change: $' + str(round(average_change, 2)))
        print('Greatest Increase in Profits: ' + str(max_change_date) + ' ($' + str(max_change) + ')')
        print('Greatest Decrease in Profits: ' + str(min_change_date) + ' ($' + str(min_change) + ')')