# 1. Move the show_results.txt file from Blackboard into your project directory.
# File show_results.txt downloaded from blackboard and saved to project directory

# 2. Create 3 lists, one for states, one for shows, and one for viewers
states = []
shows = []
viewers = []

# 3. Injest data from text file and put it into a NumPy array (show_results.txt)
import numpy as np
arr = np.genfromtxt('show_results.txt', dtype='str', delimiter=',')

# 4. Print the raw data
print('Raw data: ', arr, '\n')

# 5. Take the data from the NumPy array and sort it by state, show and
# viewers, putting each into the appropriate lists you defined earlier.
# (so now you have 3 lists, one with states, one with shows and one
# with viewer counts.) No duplicates

# populate states list
st = 0
while st < len(arr):
    states.append(arr[st][0])
    #convert list to set to eleiminate duplicates, then save back to list\
    states = list(set(states))
    st += 1

# populate shows list
sh = 0
while sh < len(arr):
    shows.append(arr[sh][1])
    #convert list to set to eleiminate duplicates, then save back to list\
    shows = list(set(shows))
    sh += 1

# populate viewers list
v = 0
while v < len(arr):
    viewers.append(arr[v][2])
    v += 1

# 6. Print these unsorted lists
print('Unsorted array of states: ', states, '\n')
print('Unsorted array of shows: ', shows, '\n')
print('Unsorted array of viewers: ', viewers, '\n')

# 7. Convert all 3 lists into NumPy arrays
npStates = np.array(states)
npShows = np.array(shows)
npViewers = np.array(viewers)

# 8. print new NumPy Arrays
print('NumPy array of states: ', npStates, '\n')
print('NumPy array of shows: ', npShows, '\n')
print('NumPy array of viewers: ', npViewers, '\n')

# 9. Sort the States and Shows arrays
npStates = sorted(npStates)
npShows = sorted(npShows)

# 10. Convert the Viewers array from STRINGS into INTS
npViewers = np.asarray(npViewers, dtype=int)

# 11. Sum up viewers list into one variable (you can do this in one line)
sumViewers = sum(npViewers)

# 12. Print: Sorted arrays (states and shows), viewers list (as ints),
# and the variable that is the sum of the viewers list.
print('Sorted array of states: ', npStates, '\n')
print('Sorted array of shows: ',npShows, '\n')
print('Viewer list as ints: ', npViewers, '\n')
print('Sum of viewer list: ', sumViewers, '\n')

# 13. Create 2 DataFrames:
import pandas as pd

#(a)show_raw_stats: index = numpy sorted array of SHOWS;
#columns = numpy sorted array of STATES
show_raw_stats = pd.DataFrame(0, index=npShows, columns=npStates)

#(b)show_agg_stats: index = same as above;
# columns= a list with the words Max, Min, Totals and Percent in it
numList = ['Max','Min','Totals','Percent']
show_agg_stats = pd.DataFrame(0, index=npShows, columns= numList )


# 14. Populate show_raw_stats with data from the Original Array injested from show_results.txt.
import bumpy as np
import pandas as pd

# Create lists to hold states, shows and viewers
states = []
shows = []
viewers = []

# Inject data from text file and print
arr = np.genfromtxt('show_results.txt', dtype='str', delimiter=',')
print(arr)

# Loop through the new numpy array and put into aforementioned lists
for i in range(1, len(arr)):
    if not arr[i][0] in states:
        states.append(arr[i][0])
    if not arr[i][1] in shows:
        shows.append(arr[i][1])
    viewers.append(arr[i][2])

print("Unsorted lists")
print(states)
print(shows)
print(viewers)

# Convert new lists into numpy arrays
np_states = np.asarray(states)
np_shows = np.asarray(shows)
np_viewers = np.asarray(viewers)

print("Unsorted numpy arrays")
print(np_states)
print(np_shows)
print(np_viewers)

# Sort numpy arrays and convert viewers array into ints.
# Also sum up vieweres array
# Print everything
sort_np_states = sorted(np_states)
sort_np_shows = sorted(np_shows)

np_int_viewers = np_viewers.astype(int)
sum_viewers = sum(np_int_viewers)

print("Sorted Numpy Arrays & Int type viewers")
print(sort_np_states)
print(sort_np_shows)
print(np_int_viewers)

print("Sum of Viewers")
print(sum_viewers)

# Create two DataFrames
show_raw_stats = pd.DataFrame(0, index=sort_np_shows, columns=sort_np_states)
show_agg_stats = pd.DataFrame(0, index=sort_np_shows, columns=['Max', 'Min', 'Totals','Percent'])

# Populate the DataFrames and sum the values in place
for i in range(len(arr)):
    state = arr[i][0]
    show = arr[i][1]
    viewers_num = int(arr[i][2])
    show_raw_stats.ix[show][state] += viewers_num

print(show_raw_stats)

# 15. Populate the Max, Min, Totals, and Percent in show_agg_stats
# using the DataFrame native functionality

# Calculate the max, min, sum and percentages of the data and put into the new DataFrame

show_agg_stats['Max'] = show_raw_stats.max(axis=1)
show_agg_stats['Min'] = show_raw_stats.min(axis=1)
show_agg_stats['Totals'] = show_raw_stats.sum(axis=1)
show_agg_stats['Percent'] = show_agg_stats['Totals'] / sum_viewers * 100
print(show_agg_stats)




# 16. Print both dataframe
print(show_raw_stats, '\n')
print(show_agg_stats, '\n')

# 17. Print the answer to these questions:
# a.Which Show has the highest percentage?
print('The show with the highest percentage of viewers is', npShows[3], 'at 16.4%', '\n')

# b.Which Show has the lowest percentage?
print('The show with the lowest percentage of viewers is', npShows[5], 'at 3.7%', '\n')

# c. Which show is your favorite?
print('While I do enjoy', npShows[7], ', of all the shows listed, my favorite is', npShows[1], '\n')



