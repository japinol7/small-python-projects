from hiker import global_answer, Hiker


def test_global_function():
    assert global_answer() == 42


def test_instance_method():
    assert Hiker().instance_answer() == 42
