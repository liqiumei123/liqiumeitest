# coding:utf-8
import pytest
import yaml

from python.calc import Calc


class TestCalc(Calc):
    def setup(self):
        self.calc = Calc()

    @pytest.mark.parametrize(["a", "b","answer"], yaml.safe_load(open("./data/add.yaml")))
    def test_add(self, a, b,answer):
        try:
            result = self.add(a, b)
            print(result(round()))
            assert result == answer
        except TypeError:
           return print("字符串不能相加")


    @pytest.mark.parametrize(["a", "b", "answer"], yaml.safe_load(open("./data/sub.yaml")))
    def test_sub(self, a, b, answer):
        try:
            result = self.sub(a,b)
            print(result(round()))
            assert result == answer
        except TypeError:
            return print("字符串不能相减")




    @pytest.mark.parametrize(["a", "b", "answer"], yaml.safe_load(open("./data/mcl.yaml")))
    def test_mcl(self, a, b, answer):
        try:
            result = self.calc.mcl(a,b)
            print(result(round()))
            assert result == answer
        except TypeError:
            return print("字符串不能相乘")



    @pytest.mark.parametrize(["a", "b", "answer"], yaml.safe_load(open("./data/div.yaml")))
    def test_div(self, a, b, answer):
        try:
            result = self.div(a, b)
            print(result(round(1)))
            assert result == answer
        except ZeroDivisionError:
            return print("除数不能为0")

    if __name__ == "main":
        pytest.main()