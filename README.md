# gdal-examples
GDAL's  2 Python interface examples
These are sample scripts intended to give an idea how GDAL's
Python interface may be used in your applications.

Script list:
------------------------------------------------------------------------------

assemblepoly.py		Script demonstrates how to assemble polygons from
			arcs.  Demonstrates various aspects of OGR Python API.

attachpct.py		Simple command line program for copying the color table of a
                        raster into another raster.

fft.py			Script to perform forward and inverse two-dimensional
			fast Fourier transform.

gdal2grd.py		Script to write out ASCII GRD rasters (used in Golden
			Software Surfer) from any source supported by GDAL.

gdal_vrtmerge.py	Similar to gdal_merge.py, but produces a VRT file.

gdalcopyproj.py		Duplicate the geotransform, projection and/or GCPs from
			one raster dataset to another, which can be useful after
			performing image manipulations with other software that
			ignores or discards georeferencing metadata.

gdalfilter.py		Example script for applying kernel based filters to
			an image using GDAL.  Demonstrates use of virtual
			files as an intermediate representation.

gdal_retile.py          Script for restructuring data in a tree of regular tiles.
                        (transferred in swig/python/scripts)

get_soundg.py		Script to copy the SOUNDG layer from an S-57 file to
			a Shapefile, splitting up features with MULTIPOINT
			geometries into many POINT feature, and appending
			the point elevations as an attribute.

histrep.py		Module to extract data from many rasters into one output.

load2odbc.py		Load ODBC table to an ODBC datastore.  Uses direct SQL
			since the ODBC driver is read-only for OGR.

rel.py			Script to produce a shaded relief image from the
			elevation data. (similar functionality in gdaldem now)

tigerpoly.py		Script demonstrating how to assemble polygons from
			arcs in TIGER/Line datasource, writing results to
			a newly created shapefile.

tolatlong.py		Script to read coordinate system and geotransformation
			matrix from input file and report latitude/longitude
			coordinates for the specified pixel.

val_repl.py		Script to replace specified values from the input
			raster file with the new ones. May be useful in cases
			when you don't like value, used for NoData indication
			and want replace it with other value. Input file
			remains unchanged, results stored in other file.

vec_tr.py		Example of applying some algorithm to all the
			geometries in the file, such as a fixed offset.

vec_tr_spat.py		Example of using Intersect() to filter based on
			only those features that truly intersect a given
			rectangle.  Easily extended to general polygon!

classify.py             Demonstrates using numpy for simple range based
                        classification of an image.  This is only an example
                        that has stuff hardcoded.

gdal_lut.py             Read a LUT from a text file, and apply it to an image.
                        Sort of a '1 band' version of pct2rgb.py.

magphase.py             Example script computing magnitude and phase images
                        from a complex image.

hsv_merge.py            Merge greyscale image into RGB image as intensity
                        in HSV space.

val_at_coord.py         Outputs the value of the raster bands at a given
                        (longitude, latitude) or (X, Y) location.

gdal_ls.py              Display the list of files in a virtual directory,
                        like /vsicurl or /vsizip

gdal_cp.py              Copy a virtual file

crs2crs2grid.py 	A script to produce PROJ.4 grid shift files from HTDP program.
			http://trac.osgeo.org/proj/wiki/HTDPGrids

ogrupdate.py            Update a target datasource with the features of a source datasource. Contrary to ogr2ogr,
                        this script tries to match features between the datasources,
                        to decide whether to create a new feature, or to update an existing one.

ogr_layer_algebra.py    Application for executing OGR layer algebra operations.

gdalpythonserver.py     A Python script that can be used as the value of GDAL_API_PROXY_SERVER config. option
                        Redirects on GDAL implementation, but could be used to implement a Python GDAL driver.

ogr_dispatch.py         Dispatch features into layers according to the value of
                        some fields or the geometry type.

wcs_virtds_params.py    Generates MapServer WCS layer definition from a tileindex with mixed SRS

ogr_build_junction_table.py Create junction tables for layers coming from GML datasources
                            that reference other objects in _href fields

gcps2ogr.py             Outputs GDAL GCPs as OGR points

------------------------------------------------------------------------------
Ports of .c/.cpp utilities
------------------------------------------------------------------------------

gdalinfo.py             A direct port of apps/gdalinfo.c

ogrinfo.py              A direct port of apps/ogrinfo.cpp

ogr2ogr.py              A direct port of apps/ogr2ogr.cpp
