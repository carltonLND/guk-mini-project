from pytest import raises


def test_invalid_type():
    with raises(TypeError, MyClass(stuff="bad stuff")):
        assert TypeError
