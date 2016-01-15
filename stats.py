def mean(vals):
    """Calculate the arithmetic mean of a list of numbers in vals."""
    assert type(vals) is list or type(vals) is tuple, 'Wrong input format.'
    	 
    total = sum(vals)
    length = len(vals)
    if length == 0:
    	return 0.0
    return total/length

def test_mean():
	assert mean([2,4]) == 3.0
test_mean()

def test_empty():
	assert mean([]) == 0.0 and mean(()) == 0.0
test_empty()

#print(mean([2,4]))
#print(mean('2,3'))



