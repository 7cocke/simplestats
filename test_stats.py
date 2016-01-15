from stats import mean
from nose.tools import assert_equal

def test_mean():
	assert_equal (mean([2,4]),3.0) #previously assert mean([2,4]) == 3.0
#test_mean()

def test_empty():
	assert mean([]) == 0.0 and mean(()) == 0.0
#test_empty()

def test_float():
	assert_equal(mean([1,2]),1.5)
#test_float()

#assert_almost_equals(mean([.5,.5,1]),.666666666666)
