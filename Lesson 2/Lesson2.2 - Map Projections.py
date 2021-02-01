# Import necessary packages
import geopandas as gpd
import matplotlib.pyplot as plt
from pyproj import CRS

# https://spatialreference.org/
# http://epsg.io/

# Read the file
fp = "/Users/saffron/Desktop/QGIS in Python/L2_data/Europe_borders.shp"
data = gpd.read_file(fp)

# Check the coordinate reference system
print(data.crs)

# Check values in geometry column
print(data["geometry"])

# Re-project the data into EPSG 3035 using epsg
# Let's make a backup copy of our data
data_wgs84 = data.copy()
# Re-project the data
data = data.to_crs(epsg = 3035)

print(data.crs)
print(data.head)

# Make subplots that are next to each other
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(12,12))

# Plot the data in WGS84 CRS
# Original Data
data_wgs84.plot(ax=ax1, facecolor="gray")

# Add title
ax1.set_title("WGS84")

# Plot the one with ETRS-LAEA projection
# Re-Projected Data
data.plot(ax=ax2, facecolor="blue")

# Add title
ax2.set_title("Equal Area")

# Set aspect ratio as 1
ax1.set_aspect(aspect=1)
ax2.set_aspect(aspect=1)

# Remove empty white space around the plot
plt.tight_layout()

plt.show()

# Shows how you need to make sure to have the correct projection for
# visualization and calculating distances!

# Output filepath
outfp = "/Users/saffron/Desktop/QGIS in Python/L2_data/Europe_borders_epsg3035.shp"

# Save to disk
#data.to_file(outfp)

# CRS of the data:
crs_default = data_wgs84.crs
# Pyproj CRS object:
crs_object = CRS(data_wgs84.crs)
# EPSG code (here, the input crs information is a bit vague so we need to lower the confidence threshold)
crs_epsg = CRS(data_wgs84.crs).to_epsg(min_confidence=25)
# PROJ string
crs_proj4 = CRS(data_wgs84.crs).to_proj4()
# Well-Known Text (WKT)
crs_wkt = CRS(data_wgs84.crs).to_wkt()

print("PROJ dictionary:\n",crs_default)
print("\nCRS object:\n",crs_object)
print("\nEPSG code:\n",crs_epsg)
print("\nPROJ string:\n",crs_proj4)
print("\nWell-Known Text:\n",crs_wkt)


# Let's see the current CRS of our data
print(type(data.crs))

# Initialize the CRS class for epsg code 3035
# with this, you can create a new CRS object just based off of the epsg data
# can do data.crs = CRS.from_epsg(3035) if you need to define a CRS for the data
CRS.from_epsg(3035)


# We can also easily parse this information individually as follows:
# Name
print(data.crs.name)

# Coordinate system
print(data.crs.coordinate_system)

# Bounds of the area where CRS is used
print(data.crs.area_of_use.bounds)

# Retrieve CRS information in WKT format
print(data.crs.to_wkt())

# Read in Data
fp = "/Users/saffron/Desktop/QGIS in Python/L2_data/ne_110m_admin_0_countries/ne_110m_admin_0_countries.shp"
admin = gpd.read_file(fp)

# Check input crs
print(admin.crs)

# Set fig size
plt.rcParams['figure.figsize'] = [12,6]

# Make a backup copy
data_admin = admin.copy()

# Plot map in original crs:
data_admin.plot()

# Plot map in projection 1:
data_admin.to_crs(epsg = 3035).plot()

# Plot map in projection 2 (web mercator)
web_mercator = CRS.from_epsg(3785)
data_admin.to_crs(web_mercator).plot()

# Plot map in projection 3 (robinson - from epsg.io):
wkt = """PROJCS["World_Robinson",
    GEOGCS["GCS_WGS_1984",
        DATUM["WGS_1984",
            SPHEROID["WGS_1984",6378137,298.257223563]],
        PRIMEM["Greenwich",0],
        UNIT["Degree",0.017453292519943295]],
    PROJECTION["Robinson"],
    PARAMETER["False_Easting",0],
    PARAMETER["False_Northing",0],
    PARAMETER["Central_Meridian",0],
    UNIT["Meter",1],
    AUTHORITY["EPSG","54030"]]
"""
robinson = CRS.from_wkt(wkt)
data_admin.to_crs(robinson).plot()
plt.axis("off")


plt.show()

