import pytest

class TestB():
    def test_1(self):
        print("CASE1")

    @pytest.mark.webtest
    def test_2(self):
        print("CASE2")
    @pytest.mark.webtest
    def test_3(self):
        print("CASE3")


