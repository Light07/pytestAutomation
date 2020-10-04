import pytest


if __name__ == "__main__":
    pytest.main(["-m", "smoke", "--alluredir=./allure_reports"])