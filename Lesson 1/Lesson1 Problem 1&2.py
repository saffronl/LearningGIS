# Course: https://autogis-site.readthedocs.io/en/latest/lessons/L1/overview.html
# Problems from : https://github.com/AutoGIS-2020/exercise-1/blob/main/Exercise-1-problem-1-2.ipynb

from shapely.geometry import Point, LineString

#1: Create a function called create_point_geom() that has two parameters (x_coord, y_coord).
# Function should create a shapely Point geometry object and return that.

# 1. Create a function called create_point_geom() that has two parameters (x_coord, y_coord).g
def create_point_geom(x_coord, y_coord):
    # 2. Function should create a shapely Point geometry object and return that.
    point = Point(x_coord,y_coord)
    return point

# NON-EDITABLE CODE CELL FOR TESTING YOUR SOLUTION
# Demonstrate the usage of the function
point1 = create_point_geom(0.0, 1.1)

# NON-EDITABLE CODE CELL FOR TESTING YOUR SOLUTION
print(point1)

# NON-EDITABLE CODE CELL FOR TESTING YOUR SOLUTION
print(point1.geom_type)





# 2: Create a function called create_line_geom() that takes a
# list of Shapely Point objects as parameter called points and
# returns a LineString object of those input points.
# In addition, you should take care that the function is used as it should:
#
#    Inside the function, you should first check with assert
#    -functionality that the input is a list (see lesson 6 from the Geo-Python course and hints for this exercise).
#    If something else than a list is passed for the function,
#    you should return an Error message: "Input should be a list!"
#
#    You should also check with assert that the input list contains at least two values.
#    If not, return an Error message: "LineString object requires at least two Points!"
#
#    Optional: Finally, you should check with assert that all values in the input list are truly Shapely Points.
#    If not, return an Error message: "All list values should be Shapely Point objects!"

print(type([Point(45.2, 22.34),Point(100.22, -3.20)]))
pointsss = [Point(45.2, 22.34),Point(100.22, -3.20)]
for i in pointsss:
    print(type(i))

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

# Demonstrate the usage of your function;
# For example, create a line object with two points:
# Point(45.2, 22.34) & Point(100.22, -3.20)
# and store the result in a variable called line1:

line1 =  create_line_geom([Point(45.2, 22.34),Point(100.22, -3.20)])

#Run these code cells to check your solution:

# NON-EDITABLE CODE CELL FOR TESTING YOUR SOLUTION
print(line1)

# NON-EDITABLE CODE CELL FOR TESTING YOUR SOLUTION
print(line1.geom_type)

# Check if your function checks the input correctly by running this code cell:

# NON-EDITABLE CODE CELL FOR TESTING YOUR SOLUTION
try:
    # Pass something else than a list
    create_line_geom("Give me a line!")
except AssertionError:
    print("Found an assertion error. List check works correctly.")
except Exception as e:
    raise e

