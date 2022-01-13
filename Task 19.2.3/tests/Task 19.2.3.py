from app.calculator import Calculator
import pytest


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 6) == 12

    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 15, 5) == 3

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 25, 50) == -25

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 8, 8) == 16
