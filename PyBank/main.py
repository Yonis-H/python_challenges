
import os
import csv

#input file path
csvpath = os.path.join('Resources', 'budget_data.csv')

#variables
month_counter = []
profit_losses =[]
revenue_change =[]

#open and read csv files
with open(csvpath) as csvfile:
   
    csvreader = csv.reader(csvfile, delimiter=',')

    #skipping header row
    header_row = next(csvreader)
    

   #read each row of data 
    for row in csvreader:

        #add months
        month_counter.append(row[0])

        #add profit
        profit_losses.append(int(row[1]))

    #loop through the values and storing them in the empty list
    for i in range(len(profit_losses)-1):

        revenue_change.append(profit_losses[i+1]-profit_losses[i])
        
#calculate total months  
total_month = (len(month_counter))
#print(total_month)

#calcuate net total amount of profit/losses
net_total = (sum(profit_losses))
#print(net_total)

#calculate avgrage change 
average_change = ({round(sum(revenue_change) / len(revenue_change),2)})
#print(average_change)
        
#calculate max profit
max_profit = max(profit_losses)
#print(f'max_profit = ' + str(max_profit))

#calculate min profit
min_profit = min(profit_losses)
#print(f'min_month = ' + str(min_profit))

#index and min and max 
index_max = profit_losses.index(max_profit)
max_month = month_counter[index_max]
#print(max_month)

index_min = profit_losses.index(min_profit)
min_month = month_counter[index_min]
#print(min_month)

#summary 
financial_analysis = (f'''Financial Analysis
----------------------------------------------------------------
Total Months: {total_month}
Total: ${net_total}
Average Change: {average_change}
Greatest Increase in Profits: {max_month}  {max_profit:.2f}
Greatest Decrease in Profits: {min_month} {min_profit:.2f}
''') 

print(financial_analysis)

#file path for saving the output file
output = os.path.join ('.','output.txt')

#write to output file
with open (output, 'w',) as txtfile:
    
    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"----------------------------------------------------------------\n")
    txtfile.write(f"Total Months: {total_month}\n")
    txtfile.write(f"Total: ${net_total}\n")
    txtfile.write(f"Average Change: ${average_change}\n")
    txtfile.write(f"Greatest Increase in Profits: {max_month} (${max_profit:.2f}))\n")
    txtfile.write(f"Greatest Decrease in Profits: {min_month} (${min_profit:.2f}))\n")
