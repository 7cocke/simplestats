def mean(vals):
    """Calculate the arithmetic mean of a list of numbers in vals."""
    assert type(vals) is list, 'Wrong input format.'
    #vals = list(map(float, vals)) 
    vals = [float(i) for i in vals]
    total = sum(vals)
    length = len(vals)
    if length == 0:
    	return 0.0
    return total/length
