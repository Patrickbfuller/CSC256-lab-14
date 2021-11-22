import pytest
import pytest_bdd
from pytest_bdd.scenario import scenarios
from pytest_bdd.steps import given, when, then
from pytest_bdd import parsers

from full_retirement import RetirementCalculator, InvalidInputException, INVALID_BIRTH_YEAR_ERROR, INVALID_BIRTH_MONTH_ERROR

scenarios('../features/full_retirement_age_calc.feature')


EXTRA_TYPES = {
    'Number': int,
}


@given(parsers.cfparse('a new retirement calculator'), target_fixture='calculator')
def new_calendar_calculator():
    return RetirementCalculator()

@when(parsers.cfparse('an invalid birth year, "{year:Number}" causes an error', extra_types=EXTRA_TYPES))
def enter_invalid_year(calculator:RetirementCalculator, year):
    with pytest.raises(InvalidInputException):
        calculator.set_birth_year(year)

@when(parsers.cfparse('an invalid birth month, "{month:Number}" causes an error', extra_types=EXTRA_TYPES))
def enter_invalid_month(calculator:RetirementCalculator, month):
    with pytest.raises(InvalidInputException):
        calculator.set_birth_month(month)

@when(parsers.cfparse('a valid year, "{year:Number}" is entered', extra_types=EXTRA_TYPES))
def enter_valid_year(calculator:RetirementCalculator, year):
    calculator.set_birth_year(year)

@when(parsers.cfparse('a valid month, "{month:Number}" is entered', extra_types=EXTRA_TYPES))
def enter_valid_month(calculator:RetirementCalculator, month):
    calculator.set_birth_month(month)

@then(parsers.cfparse('the retirement age should be "{years:Number}" years and "{months:Number}" months', extra_types=EXTRA_TYPES))
def return_retirement_age(calculator:RetirementCalculator, years, months):
    assert calculator.calculate_retirement_age() == (years, months)

@then(parsers.cfparse('the retirement date should be month "{ret_month:Number}" of year "{ret_year:Number}"', extra_types=EXTRA_TYPES))
def return_retirement_date(calculator:RetirementCalculator, ret_month, ret_year):
    assert calculator.calculate_retirement_date() == (ret_year, ret_month)