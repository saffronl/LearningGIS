from shapely.geometry import Point, LineString
import pandas as pd

# 1: Read the data/travelTimes_2015_Helsinki.txt file into a variable data using pandas.

# REPLACE THE ERROR BELOW WITH YOUR OWN CODE
data = pd.read_csv('/Users/saffron/Downloads/travelTimes_2015_Helsinki.txt', sep=";")

#Check how many rows and columns there are:

# NON-EDITABLE CODE CELL FOR TESTING YOUR SOLUTION
# This test print should print first five rows in the data (if not, something is incorrect):
print(data.head())

#2: Select the 4 columns that contain coordinate information ('from_x', 'from_y', 'to_x', 'to_y')
# and store them in variable data (i.e. update the data -variable to contain only these four columns).

# REPLACE THE ERROR BELOW WITH YOUR OWN CODE
data = data[['from_x', 'from_y', 'to_x', 'to_y']]

# NON-EDITABLE CODE CELL FOR TESTING YOUR SOLUTION
print(list(data.columns))

#3: Create two empty lists called orig_points and dest_points.
# We will store the shapely points in these lists in the next step.

# REPLACE THE ERROR BELOW WITH YOUR OWN CODE
orig_points = []
dest_points = []
# NON-EDITABLE CODE CELL FOR TESTING YOUR SOLUTION
# List length should be zero at this point:
print('orig_points length:', len(orig_points))
print('dest_points length:', len(dest_points))

#4: Create shapely points for each origin and destination and add origin points to orig_points list
# and destination points to dest_points list.
#    Create origin points based on columns from_x and from_y
#    Create destination points based on columns to_x and to_y

i=0
while i < len(data['from_x']+1):
    point = Point(data['from_x'][i], data['from_y'][i])
    orig_points.append(point)
    i += 1

i=0
while i < len(data['to_x']+1):
    point = Point(data['to_x'][i], data['to_y'][i])
    dest_points.append(point)
    i += 1


print('orig_points length:', len(orig_points))
print('dest_points length:', len(dest_points))



# NON-EDITABLE CODE CELL FOR TESTING YOUR SOLUTION

# This test print should print out the first origin and destination coordinates in the two lists:
print("ORIGIN X Y:", orig_points[0].x, orig_points[0].y)
print("DESTINATION X Y:", dest_points[0].x, dest_points[0].y)

#Check that you created a correct amount of points:
assert len(orig_points) == len(data), "Number of origin points must be the same as number of rows in the original file"
assert len(dest_points) == len(data), "Number of destination points must be the same as number of rows in the original file"


########################
# Problem 4: Creating LineStrings that represent the movements (5 points):

#######
# 1: Create a list called lines

# REPLACE THE ERROR BELOW WITH YOUR OWN CODE
lines = []

# NON-EDITABLE CODE CELL FOR TESTING YOUR SOLUTION

# Lines length should be zero at this stage:
print('lines length:', len(lines))

#######
# 2a: Create a Shapely LineString -object for each origin and destination pair

# 2b: Add each LineString object into the lines -list you created before.

# REPLACE THE ERROR BELOW WITH YOUR OWN CODE
def  create_line_geom(points):
    # you should first check with assert
    if type(points) == list:
        for i in points:
            if type(i) != 'shapely.geometry.point.Point':
                assert "All list values should be Shapely Point objects!"
    else:
        assert type(points) != list, "Input should be a list!"
    # You should also check with assert that the input list contains at least two values
    assert len(points) > 1, "LineString object requires at least two Points!"
    # you should check with assert that all values in the input list are truly Shapely Points
    # returns a LineString object of those input points.
    line = LineString(points)
    return line

lines = []
i=0
while i < len(orig_points):
    line = create_line_geom([orig_points[i], dest_points[i]])
    lines.append(line)
    i += 1
print('lines length:', len(lines))
print('line:', lines[0].length)
# NOTE: After you have solved this problem, we recommend that you restart the kernel
# and run all cells again! There is a risk that you append the same points to the lists many
# times if you run the cell multiple times without restarting the kernel.

# NON-EDITABLE CODE CELL FOR TESTING YOUR SOLUTION

#Test that the list has correct number of LineStrings
assert len(lines) == len(data), "There should be as many lines as there are rows in the original data"

#######
# 3: Create a variable called total_length,
# and store the total (Euclidian) distance of all the origin-destination
# LineStrings that we just created into that variable.

# REPLACE THE ERROR BELOW WITH YOUR OWN CODE

i=0
total_length = 0
while i < len(lines):
    total_length = total_length + lines[i].length
    i += 1

# NON-EDITABLE CODE CELL FOR TESTING YOUR SOLUTION

# This test print should print the total length of all lines
print("Total length of all lines is", round(total_length, 2))

#######
# 4: write the previous parts, i.e. the creation of the LineString
# and calculating the total distance, into dedicated functions:

#    create_od_lines(): Takes two lists of Shapely Point -objects as input
#    and returns a list of LineStrings
#    calculate_total_distance(): Takes a list of LineString geometries as input
#    and returns their total length

# You can copy and paste the codes you have written earlier into the functions.
# Below, you can find a code cell for testing your functions
# (you should get the same result as earler).

# Note: avoid using the same variable names as earlier inside your functions!
# Functions are often defined at the top of the script file (or jupyter notebook),
# and now that we have them here at the very end you might accidentally alter
# an existing variable inside your functions.
# To avoid this, alter the variable names inside your own functions
# if you re-use code from this notebook.

# REPLACE THE ERROR BELOW WITH YOUR OWN CODE
def create_od_lines(ListofPoints):
    ListofLines = []
    i = 0
    while i < len(ListofPoints[0]):
        oneline = create_line_geom([ListofPoints[0][i],ListofPoints[1][i]])
        ListofLines.append(oneline)
        i += 1
    return ListofLines

def calculate_total_distance(Line_List):
    i = 0
    totallengthlines = 0
    while i < len(Line_List):
        totallengthlines = totallengthlines + Line_List[i].length
        i += 1
    return totallengthlines
# NON-EDITABLE CODE CELL FOR TESTING YOUR SOLUTION

# Use the functions
# -----------------

# Create origin-destination lines
od_lines = create_od_lines([orig_points, dest_points])

# Calculate the total distance
tot_dist = calculate_total_distance(od_lines)

print("Total distance", round(tot_dist,2))



