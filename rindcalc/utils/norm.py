def norm(array, max_value, min_value):
    array_min, array_max = array.min(), array.max()
    return ((max_value - min_value) * ((array - array_min) /
            (array_max - array_min))) + min_value