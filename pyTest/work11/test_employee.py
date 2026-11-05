import pytest
from employee import Employee

@pytest.fixture
def employee():
    emp = Employee('lee','yeung',5000)
    return emp


def test_give_default_raise(employee):
    employee.give_raise()
    assert employee.annul == 10000


def test_give_custom_raise(employee):
    employee.give_raise(6000)
    assert employee.annul == 5000+6000