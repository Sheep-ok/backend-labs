from lab import middle, sum_digits, double_eights

def test_middle():
    assert middle(1, 2, 3) == 2
    assert middle(2, 1, 3) == 2
    assert middle(3, 1, 2) == 2

def test_sum_digits():
    assert sum_digits(0) == 0
    assert sum_digits(1) == 1
    assert sum_digits(123) == 6
    assert sum_digits(1e20) == 1

def test_double_eights():
    assert double_eights(0) == False
    assert double_eights(123) == False
    assert double_eights(2838) == False
    assert double_eights(88) == True
    assert double_eights(888888) == True
    assert double_eights(110088) == True
    assert double_eights(880011) == True