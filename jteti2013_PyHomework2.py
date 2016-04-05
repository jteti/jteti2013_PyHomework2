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
print(arr, '\n')

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
print(states, '\n')
print(shows, '\n')
print(viewers, '\n')

# 7. Convert all 3 lists into NumPy arrays
npStates = np.array(states)
npShows = np.array(shows)
npViewers = np.array(viewers)

# 8. print new NumPy Arrays
print(npStates, '\n')
print(npShows, '\n')
print(npViewers, '\n')

# 9. Sort the States and Shows arrays
npStates = sorted(npStates)
npShows = sorted(npShows)

# 10. Convert the Viewers array from STRINGS into INTS
npViewers = np.asarray(npViewers, dtype=int)

# 11. Sum up viewers list into one variable (you can do this in one line)
sumViewers = sum(npViewers)

# 12. Print: Sorted arrays (states and shows), viewers list (as ints),
# and the variable that is the sum of the viewers list.
print(npStates, '\n')
print(npShows, '\n')
print(npViewers, '\n')
print(sumViewers, '\n')

# 13. Create 2 DataFrames:
import pandas as pd

#(a)show_raw_stats: index = numpy sorted array of SHOWS;
#columns = numpy sorted array of STATES
show_raw_stats = pd.DataFrame(0, index=npShows, columns=npStates)

#(b)show_agg_stats: index = same as above;
# columns= a list with the words Max, Min, Totals and Percent in it
numList = ['Max','Min','Totals','Percent']
show_agg_stats = pd.DataFrame(0, index=npShows, columns= numList )








