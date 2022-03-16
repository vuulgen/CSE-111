from tips import compute_tip

def test_compute_tip():
    assert compute_tip(100, 50) == 50
    assert compute_tip(1000, 3) == 30