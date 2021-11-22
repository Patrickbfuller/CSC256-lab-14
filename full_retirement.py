"""
Filename: full_retirement.py
Author: Patrick Fuller
Date: 08/16/21
Class: CSC 256
Instructor: Professor Enkema

This program calculates the full retirement age for a user based on their
birthday.
"""

from re import fullmatch

INVALID_BIRTH_YEAR_ERROR = Exception("Invalid Birth Year: Year should be 1900 - 2021")
INVALID_BIRTH_MONTH_ERROR = Exception("Invalid Birth Month: Month should be 1 - 12")

class InvalidInputException(Exception):
    def __init__(self, message):
        super().__init__(message)

month_strings = ["January", "February", "March", "April", "May", "June",
                 "July", "August", "September", "October", "November",
                 "December"]


def main():
    """
    This main driver handles user interaction.
    """
    # Display title
    print("Social Security Full Retirement Age Calculator")

    # Loop menu
    while True:
        calculator = RetirementCalculator()
        try:
            # Get valid birth year or empty string for exiting
            user_birth_year = get_user_year()
            # exit if Falsey
            if user_birth_year == None:
                break

            calculator.set_birth_year(user_birth_year)
        except InvalidInputException as e:
            print(e)
            continue

        try:
            # Get valid month
            user_birth_month = get_user_month()
            if user_birth_month == None:
                continue
            calculator.set_birth_month(user_birth_month)
        except InvalidInputException as e:
            print(e)
            print("Returning to year...")
            continue

        # Get age
        years, months = calculator.calculate_retirement_age()

        # Display retirement age
        print(F"--Your full retirement age is {years} and {months} months")

        # Calculate and display date
        # retirement_year = birth_year + years + (birth_month + months) // 12
        # retirement_month = (birth_month + months) % 12
        ret_year, ret_month = calculator.calculate_retirement_date()

        month_str = month_strings[ret_month - 1]

        print(F"--This will be in {month_str} of {ret_year}")

    # Announce exit
    print("*Goodbye*")


def get_user_year():
    """
    Retrieve valid year between 1900 and 2021 inclusive or empty string from
    user.
    """
    year = input("Enter the year of birth or leave blank and [ENTER] to "
                 "exit: ").strip()
    # loop if year is not empty and invalid
    while year and not fullmatch("\d{4}", year):
        year = input("Year should be numeral in format YYYY or "
                     "leave empty and [ENTER] to exit: ").strip()

    # if empty string, return None
    if not year:
        year = None
    else:
        year = int(year)
    return year


def get_user_month():
    """
    Retrieve valid month between 1 and 12 inclusive from user.
    """
    month = input("Enter the month of birth or "
                  "leave empty to and [ENTER] to restart: ")
    while month and not fullmatch("\d{1,2}", month):
        month = input("Month should be numeral in format MM or "
                      "leave empty to and [ENTER] to restart: ").strip()
    # IF empty string, return None || ELSE return int of month
    if not month:
        month = None
    else:
        month = int(month)
    return month
    



class RetirementCalculator():

    _birth_year = None
    _birth_month = None
    _retirement_age_years = None
    _retirement_age_months = None
 

 
    def set_birth_year(self, birth_year):
        if not self.is_valid_birth_year(birth_year):
            raise InvalidInputException(INVALID_BIRTH_YEAR_ERROR)
        self._birth_year = birth_year
    
    def set_birth_month(self, birth_month):
        if not self.is_valid_birth_month(birth_month):
            raise InvalidInputException(INVALID_BIRTH_MONTH_ERROR)
        self._birth_month = birth_month
    
    def is_valid_birth_year(self, year):
        return 1900 <= year <= 2021

    def is_valid_birth_month(self, month):
        return 1 <= month <= 12

    def calculate_retirement_age(self):
        year = self._birth_year
        if year <= 1937:
            age = (65, 0)
        elif year <= 1938:
            age = (65, 2)
        elif year <= 1939:
            age = (65, 4)
        elif year <= 1940:
            age = (65, 6)
        elif year <= 1941:
            age = (65, 8)
        elif year <= 1942:
            age = (65, 10)
        elif year <= 1954:
            age = (66, 0)
        elif year <= 1955:
            age = (66, 2)
        elif year <= 1956:
            age = (66, 4)
        elif year <= 1957:
            age = (66, 6)
        elif year <= 1958:
            age = (66, 8)
        elif year <= 1959:
            age = (66, 10)
        else:
            age = (67, 0)

        self._retirement_age_years, self._retirement_age_months = age
        return age

    def calculate_retirement_date(self):
        """Return tuple of (year, month)"""

        if not self._retirement_age_years and self._retirement_age_months:
            self.calculate_retirement_age()

        return self.add_years_months(
            base_year=self._birth_year,
            base_month=self._birth_month,
            delta_years=self._retirement_age_years,
            delta_months=self._retirement_age_months
        )

    def add_years_months(self, base_year: int, base_month: int, delta_years: int,
                     delta_months: int):
        """
        Calculate new date from base year and month with change in years and
        months.
        :return: A tuple containing year, month
        """

        final_year = base_year + delta_years + (base_month + delta_months) // 13
        final_month = base_month + delta_months
        if final_month > 12:
            final_month -= 12
        return final_year, final_month

if __name__ == "__main__":
    main()
