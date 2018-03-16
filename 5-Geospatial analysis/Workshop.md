<p align="center"> <b>Geospatial Software Analysis - An Introduction to Google Earth Engine</b> </p>

<br><br><br><br><br><br><br><br>


<p align="center"> <b>TC Chakraborty</b>   </p>


<br><br><br><br>


<p align="center">  <b>March 16, 2018</b>  </p>
<br><br>
<br><br><br><br>


# Agenda

- Introduction to Geospatial Analysis
- Data Types
- The Google Earth Engine platform
- Basic functions
- Variable types
- Geometry declaration
- Operations on Geometries
- Features and Feature Collections
- Operations on Features
- Functions and mapping
- Images and Image Collections
- Filters
- Exporting Data
- Conclusion and resources


# Introduction
Collection, visualization, and analysis of geographical or spatial data.

# Data types

- Vector data represent lat-long coordinates

- Raster data comprises of pixels with associated values

-Points

![Points](https://github.com/datadrivenyale/day-of-data-2.0/blob/master/5-Geospatial%20analysis/images/points-vector.png "Points")

-Lines

![Lines](https://github.com/datadrivenyale/day-of-data-2.0/blob/master/5-Geospatial%20analysis/images/line-vector.png "Lines")

-Polygons

![Polygons](https://github.com/datadrivenyale/day-of-data-2.0/blob/master/5-Geospatial%20analysis/images/polygon-vector.png "Polygons")

-Raster layers/bands

![Raster](https://github.com/datadrivenyale/day-of-data-2.0/blob/master/5-Geospatial%20analysis/images/Map-Algebra.png "Raster")


# Google Earth Engine platform

- [Code Editor](https://code.earthengine.google.com/ "Earth Engine Code Editor")

- Cloud-based platform for planetary scale geospatial analysis
- Uses Google's computational resources to reduce processing time
- Massive archive of remote sensing data 
- 200 public datasets 
- greater than 4000 new images every day 
- greater than 5 million images 
- greater than 5 petabytes of data
Source: Google Earth Engine User summit


![Code Editor](https://github.com/datadrivenyale/day-of-data-2.0/blob/master/5-Geospatial%20analysis/images/EE.png "Code Editor")

# Basic Functions

- Declaring variables 
```javascript
var varname = Containerforvariabletype(variable name); 
```
- Centering map
```javascript
Map.setCenter(long, lat, zoom level);
```
>Zoom level varies from 0 (no zoom) to 20 (highest zoom level)

- Displaying metadata
```javascript
print(variable name) 
```
- Adding a layer to the map
```javascript
Map.addLayer(VARIABLENAME);
```

# Variable types in Earth Engine

- Strings  

```javascript
var var_String = ee.String("This is a string. Or is it? It is."); 
```
- Numbers
```javascript
var var_Numbers = ee.Number(5);
```

- Arrays
```javascript
var var_Array = ee.Array([[5, 2, 3],  [-2, 7, 10],  [6, 6, 9]]); 
```

- Lists
```javascript
var var_List = ee.List([5, "five" , 6, "six"]); 
```
- Dictionaries
```javascript
var var_Dictionary = ee.Dictionary({five: 5 , six: 6}); 
```

### And the fun stuff
- Geometries
- Features
- Feature Collections
- Images
- Image Collections


# Geometries – declaration and types

-Points
```javascript
var var_Point = ee.Geometry.Point(0, 45);
-Multi Points
```javascript
var var_MultiPoint = ee.Geometry.MultiPoint(0, 45, 5,6, 70,-56);
```
-Line String
```javascript
var var_LineString = ee.Geometry.LineString([[0, 45], [5,6], [70,-56]]);
```
-Multi Line String
```javascript
var var_MultiLineString = ee.Geometry.MultiLineString([[[0, 45], [5,6], [70,-56]], [[0, -45], [-5,-6], [-70,56]]]);
```
-Linear Ring
```javascript
var var_LinearRing = ee.Geometry.LinearRing(0, 45, 5,6, 70,-56, 0,45);
```
-Rectangle
```javascript
var var_Rectangle = ee.Geometry.Rectangle(0, 0, 60,30);
```
-Polygon
```javascript
var var_Polygon = ee.Geometry.Polygon([[[0, 0], [6,3], [5, 5], [-30,2], [0,0]]]);
```
-Multi Polygon
```javascript
var var_MultiPolygon = ee.Geometry.MultiPolygon([ee.Geometry.Polygon([[0, 0], [6, 3], [5, 5], [-30, 2], [0,0]]), ee.Geometry.Polygon([[0, 0], [-6, -3], [-5, -5], [30, -2], [0, 0]])]);
```
