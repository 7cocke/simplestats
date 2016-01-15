def mean(vals):
    """Calculate the arithmetic mean of a list of numbers in vals."""
    assert type(vals) is list or type(vals) is tuple, 'Wrong input format.'
    	 
    total = sum(vals)
    length = len(vals)
    if length == 0:
    	return 0.0
    return total/length


