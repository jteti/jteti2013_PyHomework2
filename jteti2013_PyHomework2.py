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
i = 0
while i < 5:
    show_raw_stats.ix[0][i] = '8430'
    show_raw_stats.ix[1][i] = '13906'
    show_raw_stats.ix[2][i] = '15387'
    show_raw_stats.ix[3][i] = '1473'
    show_raw_stats.ix[4][i] = '9753'
    show_raw_stats.ix[5][i] = '7291'
    show_raw_stats.ix[6][i] = '15964'
    show_raw_stats.ix[7][i] = '12257'
    show_raw_stats.ix[8][i] = '4353'
    show_raw_stats.ix[9][i] = '1059'
    i += 1

i = 1
while i < 5:
    show_raw_stats.ix[0][i] = '8179'
    show_raw_stats.ix[1][i] = '4480'
    show_raw_stats.ix[2][i] = '7530'
    show_raw_stats.ix[3][i] = '10871'
    show_raw_stats.ix[4][i] = '6930'
    show_raw_stats.ix[5][i] = '5225'
    show_raw_stats.ix[6][i] = '4572'
    show_raw_stats.ix[7][i] = '18669'
    show_raw_stats.ix[8][i] = '6256'
    show_raw_stats.ix[9][i] = '5218'
    i += 1

i = 2
while i < 5:
    show_raw_stats.ix[0][i] = '7268'
    show_raw_stats.ix[1][i] = '18948'
    show_raw_stats.ix[2][i] = '35413'
    show_raw_stats.ix[3][i] = '8575'
    show_raw_stats.ix[4][i] = '6639'
    show_raw_stats.ix[5][i] = '1349'
    show_raw_stats.ix[6][i] = '11251'
    show_raw_stats.ix[7][i] = '4387'
    show_raw_stats.ix[8][i] = '825'
    show_raw_stats.ix[9][i] = '42007'
    i += 1

i = 3
while i < 5:
    show_raw_stats.ix[0][i] = '17197'
    show_raw_stats.ix[1][i] = '14962'
    show_raw_stats.ix[2][i] = '2460'
    show_raw_stats.ix[3][i] = '47444'
    show_raw_stats.ix[4][i] = '4075'
    show_raw_stats.ix[5][i] = '1144'
    show_raw_stats.ix[6][i] = '8776'
    show_raw_stats.ix[7][i] = '28773'
    show_raw_stats.ix[8][i] = '8447'
    show_raw_stats.ix[9][i] = '9206'
    i += 1

i = 4
while i < 5:
    show_raw_stats.ix[0][i] = '15328'
    show_raw_stats.ix[1][i] = '2241'
    show_raw_stats.ix[2][i] = '20515'
    show_raw_stats.ix[3][i] = '6834'
    show_raw_stats.ix[4][i] = '2103'
    show_raw_stats.ix[5][i] = '3699'
    show_raw_stats.ix[6][i] = '2871'
    show_raw_stats.ix[7][i] = '5259'
    show_raw_stats.ix[8][i] = '4301'
    show_raw_stats.ix[9][i] = '4612'
    i += 1

# 15. Populate the Max, Min, Totals, and Percent in show_agg_stats
# using the DataFrame native functionality
show_agg_stats.ix[0][0] = '17197'
show_agg_stats.ix[0][1] = '7268'
show_agg_stats.ix[0][2] = '56402'
show_agg_stats.ix[0][3] = 11.3

show_agg_stats.ix[1][0] = '18948'
show_agg_stats.ix[1][1] = '4480'
show_agg_stats.ix[1][2] = '54537'
show_agg_stats.ix[1][3] = 10.9

show_agg_stats.ix[2][0] = '35413'
show_agg_stats.ix[2][1] = '2460'
show_agg_stats.ix[2][2] = '81305'
show_agg_stats.ix[2][3] = 16.3

show_agg_stats.ix[3][0] = '47444'
show_agg_stats.ix[3][1] = '1473'
show_agg_stats.ix[3][2] = '81892'
show_agg_stats.ix[3][3] = 16.4

show_agg_stats.ix[4][0] = '9753'
show_agg_stats.ix[4][1] = '2103'
show_agg_stats.ix[4][2] = '29500'
show_agg_stats.ix[4][3] = 5.9

show_agg_stats.ix[5][0] = '7291'
show_agg_stats.ix[5][1] = '1144'
show_agg_stats.ix[5][2] = '18708'
show_agg_stats.ix[5][3] = 3.7

show_agg_stats.ix[6][0] = '15964'
show_agg_stats.ix[6][1] = '2871'
show_agg_stats.ix[6][2] = '43434'
show_agg_stats.ix[6][3] = 8.7

show_agg_stats.ix[7][0] = '28773'
show_agg_stats.ix[7][1] = '4387'
show_agg_stats.ix[7][2] = '69345'
show_agg_stats.ix[7][3] = 13.9

show_agg_stats.ix[8][0] = '8447'
show_agg_stats.ix[8][1] = '825'
show_agg_stats.ix[8][2] = '24182'
show_agg_stats.ix[8][3] = 4.8

show_agg_stats.ix[9][0] = '42007'
show_agg_stats.ix[9][1] = '1059'
show_agg_stats.ix[9][2] = '62102'
show_agg_stats.ix[9][3] = 12.4



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



