from stats import mean

def test_mean():
	assert mean([2,4]) == 3.0
test_mean()

def test_empty():
	assert mean([]) == 0.0 and mean(()) == 0.0
test_empty()

def test_float():
	assert mean([1,2]) == 1.5
test_float()

