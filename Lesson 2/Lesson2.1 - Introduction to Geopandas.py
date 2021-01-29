import geopandas as gpd
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Define path to folder
input_folder = r"/Users/saffron/Desktop/QGIS in Python/L2_data/NLS/2018/L4/L41/L4132R.shp"
file_name = "m_L4132R_p.shp"

# Join folder path and filename
fp = os.path.join(input_folder, file_name)

# Print out the full file path
print(fp)

# Read file using gpd.read_file()
data = gpd.read_file(fp)

print(type(data))

print(data.head())

print(data.columns.values)

#Saving only columns that are necessary
data = data[['RYHMA','LUOKKA','geometry']]

print(data.head())

print(data.columns.values)

# Define new column names in a dictionary:
colnames = {'RYHMA':'GROUP','LUOKKA':'CLASS'}

# Rename
data.rename(columns=colnames, inplace=True)

print(data.head())

print(data.columns.values)

# Check your understanding
# Figure out: number of rows, number of classes, number of groups

# Number of rows
print("Number of rows: ",len(data))

# Number of classes
print("Number of classes: ",data["CLASS"].nunique())

# Number of Groups
print("Number of groups: ",data["GROUP"].nunique())


data.plot()
plt.show()


print(data["geometry"].head())

# Access the geometry on the first row of data
print(type(data.at[0,"geometry"]))
poly1 = data.at[0,"geometry"]

# Print information about the area
print("Area: ",round(poly1.area,2)," square meters")

# Iterate through to get the areas of each row
for index, row in data[0:5].iterrows():
    # Get the area from the shapely-object stores in the geometry-column
    poly_area = row['geometry'].area
    print("Polygon area at index {index} is: {area:.0f} square meters".format(index=index,area=poly_area))

# Or ...
print(data.area)

data["area"] = data.area
print(data.head())

print("Max area: ",data["area"].max())
print("Min area: ",data["area"].min())
print("Median area: ",data["area"].median())
print("Average area: ",data["area"].mean())



# Writing data into a shapefile
# Class number = 36200, "Lake water"
selection = data.loc[data["CLASS"]==36200]

selection.plot()
plt.show()

# Write this layer into a new Shapefile using the gpd.to_file() function

output_folder = r"/Users/saffron/Desktop/QGIS in Python/L2_data"
filename = "Class_32600.shp"
output_fp = os.path.join(output_folder,filename)

# Write those rows into a new file (the default output file format is Shapefile)
selection.to_file(output_fp)

# Read the output Shapefile in a new geodataframe and check the data looks okay
temp = gpd.read_file(output_fp)
print(temp.head)
temp.plot()
plt.show()


# Goal is to divide the data into files of each class

# Print all the unique values in the CLASS column
print(data["CLASS"].unique())

# Group the data by class
grouped = data.groupby(by="CLASS")
print(grouped)

# Check group keys (same as unique values in data
print(grouped.groups.keys())

# Check how many rows of data each group has
# Iterate over the grouped object
for key, group in grouped:
    # Let's check how many rows each group has
    print("Terrain class: ",key)
    print("Number of rows: ",len(group),"\n")

# The last variable is in memory from the iteration
print(group.head())

print(type(group))

"""
String formatting
There are different approaches for formatting strings in Python.
Here are a couple ways to put together file names using variables:

basename = "terrain"
key = 36200

# Option 1. Concatenating using the + operator
out_fp = basename + "-" + str(key) + ".shp"

# Option 2. Positional formatting using % operator
out_fp = "%s_%s.shp" %(basename, key)

# Option 3. Positional formatting using .format()
out_fp = "{}_{}.shp".format(basename, key)
"""

# Determine output directory
output_folder = r"/Users/saffron/Desktop/QGIS in Python/L2_data"

# Create a new folder called 'Results'
result_folder = os.path.join(output_folder,"Results")

# Check if the folder exists already
if not os.path.exists(result_folder):
    # if it does not exist, create one
    print("Creating a folder for the results...")
    os.makedirs(result_folder)
else:
    print("Results folder exists already.")

# Iterate over the groups, create a file name, and save group to file

# Iterate over the groups
for key, group in grouped:
    # Format the filename
    output_name = "terrain_{}.shp".format(key)
    # Print information about the process
    print("Saving file", output_name)
    # Create an output path
    outpath = os.path.join(result_folder,output_name)
    # Export the data
    group.to_file(outpath)

# Save data to csv

# Summarize the total area of each group
area_info = grouped.area.sum().round()
print(area_info)

# Create an output path
area_info.to_csv(os.path.join(result_folder,"terrain_class_areas.csv"),header=True)

