# Submission TODO

### Features

  * Create segmentation with raster/raster local statistics
	* Biggest issue at the moment is speed.
	* PROPOSED ALGORITHM:
		1. Read index output by rindcalc as array
		2. Segmentation (scikit-image atm)
		3. Create list of indvidual unique values within segmented
		   array
		4. Where segmented NumPy array i,j == unique value: 
			take i,j  value of index array and add to a list
		5. Take avg of index value list for unique value.
		6. Assign avg for all values in segmented array that equals
		   the unique value in same i,j in new array.
		7. Iterate to next unique value in the 
  * Explore vectorization of the segmented raster for local statistics
	* create virtual layer for the vector to minimize hardrive space used?

### Automated tests

  * Travis or create own testing? 
	* I believe github student provides access to travis.

### Documentation

  * Minimalize it. 
  * Better page structure. 
  * Standardize .rst formatting


