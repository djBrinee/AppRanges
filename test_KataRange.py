import pytest
#from KataRangePack import RangeClass

obj1 = RangeClass("(2,3)")
obj2 = RangeClass("[2,5)")
obj3 = RangeClass("[3,6]")
obj4 = RangeClass("[4,8)")
obj5 = RangeClass("[3,6]")
obj6 = RangeClass("(2,3)")

def test_range_Validationobj1():
    assert obj1.range_validation() == True

def test_splitobj1():
    assert obj1.split() == ['(', '2', '3', ')']

def test_range_Validationobj2():
    assert obj2.range_validation() == True

def test_splitobj2():
    assert obj2.split() == ['[', '2', '5', ')']

def test_LenghtRange():
    assert obj2.LenghtRange() == range(2,5)
    
def test_LenghtRange2():
    assert obj3.LenghtRange() == range(3,7)

def test_allPoints():
    assert obj4.allPoints() == '{4,5,6,7}'

def test_allPoints2():
    assert obj2.allPoints() == '{2,3,4}'

def test_EndPoints():
    assert obj2.EndPoints() == '{2,4}' 

def test_EndPoints2():
    assert obj3.EndPoints() == '{3,6}' 

def test_Equals1():
    assert obj3.Equals(obj5) == True

def test_Equals2():
    assert obj6.Equals(obj1) == True
    
def test_Overlap1():
    assert obj2.overlapsRange(obj3) == True
