from src.math_opretion import add ,sub

def test_add():
    assert add(3,5)==8
    assert add(4,7)==11

def test_sub():
    assert sub(3,4)==-1
    assert sub(4,5)==-1
    