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
- Example Scripts


# Introduction
Collection, visualization, and analysis of geographical or spatial data.

# Data types

- Vector
Data representing lat-long coordinates

![Points](https://github.com/datadrivenyale/day-of-data-2.0/blob/master/5-Geospatial%20analysis/images/points-vector.png "Points")

![Lines](https://github.com/datadrivenyale/day-of-data-2.0/blob/master/5-Geospatial%20analysis/images/line-vector.png "Lines")

![Polygons](https://github.com/datadrivenyale/day-of-data-2.0/blob/master/5-Geospatial%20analysis/images/polygon-vector.png "Polygons")

- Raster

![Raster](https://github.com/datadrivenyale/day-of-data-2.0/blob/master/5-Geospatial%20analysis/images/Map-Algebra.png "Raster")


## image.select
- Creates a new image containing only those bands of a specified image that have a specified name, index, or RE2-compatible regex.
- Since selections cannot be made from an image collection, such a collection would have to be reduced to an image in order to select bands.

### Syntax

##### Javascript
```
newImage = oldImage.select( bandSelectors, bandOrder )  
```

- *newImage* is the new image.
- *oldImage* is the specified image.
- *bandSelectors* are the specified names, indices, or regexes, given as an array of strings.
- Optional: *bandOrder* is an array of new names to be ascribed to (all of) the bands of the new image, given as an array of strings.


### Example

##### Javascript
```javascript
var RedBandIMAGE   = ee.Image( 'LC8_L1T_TOA/LC80410362015107LGN00' ).select( ['B4'] );   // Los Angeles
var GreenBandIMAGE = ee.Image( 'LC8_L1T_TOA/LC80410362015107LGN00' ).select( ['B3'] );
var BlueBandIMAGE  = ee.Image( 'LC8_L1T_TOA/LC80410362015107LGN00' ).select( ['B2'] );
var MultibandIMAGE = ee.Image( 'LC8_L1T_TOA/LC80410362015107LGN00' ).select( ['B4','B3','B2'] );
Map.setCenter( -118.2733, 34.0942, 12 ); 
Map.addLayer( RedBandIMAGE,   {min:0, max:0.17, palette:'000000,ff5555'},     'RednessImage'   );
Map.addLayer( GreenBandIMAGE, {min:0, max:0.17, palette:'000000,77ff77'},     'Greenness Image');
Map.addLayer( BlueBandIMAGE,  {min:0, max:0.17, palette:'000000,7777ff'},     'Blueness Image' );
Map.addLayer( MultibandIMAGE, {min:0, max:0.17, gamma:0.5, bands:'B4,B3,B2'}, 'Multiband Image');
