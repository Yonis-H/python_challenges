import csv
import os

csvpath = os.path.join('Resources', 'election_data.csv')

#setting variables to hold candidates and vote count
vote_counter = 0
candidate_correy = 0
candidate_khan =0
candidate_otooley = 0
candidate_li = 0

with open(csvpath, newline='') as csvfile:

    csvreader =csv.reader(csvfile, delimiter=',')

    #skip header row
    header_row = next(csvreader)

    #loop through the data 
    for row in csvreader:
        vote_counter = vote_counter + 1
        #print(vote_counter)

    #calculate each candiates total votes

        if (row[2] == "Correy"):
            candidate_correy += 1
        elif (row[2] == "Khan"):
            candidate_khan += 1
        elif (row[2] == "O'Tooley"):
            candidate_otooley += 1
        else:
            candidate_li += 1

    #calculating the percentage of the votes each candidate got
    correy_percent = candidate_correy / vote_counter
    khan_percent = candidate_khan / vote_counter
    otooley_percent = candidate_otooley / vote_counter
    li_percent = candidate_li / vote_counter
    print(candidate_correy,candidate_khan,candidate_otooley,candidate_li)

    poll_winner = max(candidate_correy,candidate_khan,candidate_otooley,candidate_li )
    print(poll_winner)


    if poll_winner == candidate_correy:
        winner_name = "Correy"
    elif poll_winner == candidate_khan:
        winner_name = "Khan"
    elif poll_winner == candidate_otooley:
        winner_name = "O'Tooley"
    else:
        winner_name = "Li"

print
print(f"Election Results")
print(f"---------------------------")
print(f"Total Votes: {vote_counter}")
print(f"---------------------------")
print(f"Correy: {correy_percent:.3%}({candidate_correy})")
print(f"Kahn: {khan_percent:.3%}({candidate_khan})")
print(f"O'Tooley: {otooley_percent:.3%}({candidate_otooley})")
print(f"Li: {li_percent:.3%}({candidate_li})")
print(f"---------------------------")
print(f"Winner: {winner_name}")
print(f"---------------------------")


# Specify File To Write To
output_file = os.path.join('Resources', 'election_results.text')



# Open File Using "Write" Mode. Specify The Variable To Hold The Contents
with open(output_file, 'w',) as txtfile:

# Write New Data
    txtfile.write(f"Election Results\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Votes: {vote_counter}\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Correy: {correy_percent:.3%}({candidate_correy})\n")
    txtfile.write(f"Kahn: {khan_percent:.3%}({candidate_khan})\n")
    txtfile.write(f"O'Tooley: {otooley_percent:.3%}({candidate_otooley})\n")
    txtfile.write(f"Li: {li_percent:.3%}({candidate_li})\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Winner: {winner_name}\n")
    txtfile.write(f"---------------------------\n")










