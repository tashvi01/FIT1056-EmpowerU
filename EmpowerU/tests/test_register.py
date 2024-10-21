"""
This file contains tests for the Register Class

Monday G1

"""

#Standard library imports
import sys



sys.path.append("../GUI")

#third party imports

import pytest


from Register import Register  

def test_is_valid_contact_number():
    """
    test cases for check function in Register class
    
    """

    reg = Register()
    #Valid contact numbers
    assert reg.is_valid_contact_number("0412345678")  == True 
    assert reg.is_valid_contact_number("1234567891") == True

    #invalid contact numbers
    assert reg.is_valid_contact_number("12456789") == False #1 digit not enough, off-point
    assert reg.is_valid_contact_number("abcd") == False #not digits
    assert reg.is_valid_contact_number("-1234") == False #negative number

def test_is_leap_year():
    reg = Register()
    #valid leap years
    assert reg.is_leap_year(2020) == True #Leap year that is divisible by 4 but not 100
    assert reg.is_leap_year(2024) == True # This year, leap year, divisible by 4 but not 100
    assert reg.is_leap_year(2000) == True #Leap year disibile by 100 and 400


    #not leap years
    assert reg.is_leap_year(1900) == False # A non-leap year which is not by 400 but divisble by 100
    assert reg.is_leap_year(2023) == False # Last year, not a leap year and off-point( the value closest to boundary that flips condition)
    assert reg.is_leap_year(2021) == False #non-leap year not divisble by 4
    assert reg.is_leap_year(1800) == False # non-leap year divisble by 100 but not 400 but also divisble by 4

def test_is_date_valid():
    reg = Register()
    assert reg.is_date_valid(29,2,2004) == True #date that only exists in a leap year, test case is leap year
    assert reg.is_date_valid(30,4,2006) == True #On-point, value that flips condition
    assert reg.is_date_valid(29,4,2006) == True #In-point, a valid date
    assert reg.is_date_valid(31,8,2006) == True #valid date in 31 day month
    assert reg.is_date_valid(23,5,1984) == True #random valid date
    assert reg.is_date_valid(1,1,2000) == True #valid date
    assert reg.is_date_valid(13,5,1800) == True #boundary condition for year, on-point

    assert reg.is_date_valid(29,2,2006) == False # date that doesnt exist in 2023 since not a leap year
    assert reg.is_date_valid(31,4,2006) == False #date that is outside month dates
    assert reg.is_date_valid(32,8,2006) == False #invalid date in 31 day month, off-point
    assert reg.is_date_valid(24,13,2006) == False #invalid month
    assert reg.is_date_valid(-23,11,2006) == False #negative date, invalid
    assert reg.is_date_valid (16,-4,2006) == False #negative month, invalid
    assert reg.is_date_valid(13,6,-2006) == False #negative year, invalid
    assert reg.is_date_valid(0,1,1970) == False # 0 date, invalid
    assert reg.is_date_valid(11,0,1970) == False # 0 month, invalid
    assert reg.is_date_valid(12,12,1799) == False # year outside valid range, invalid
    assert reg.is_date_valid(12,12,2007) == False # year outside valid range, invalid

def test_is_valid_date_format():
    reg = Register()
    assert reg.is_valid_date_format("01/01/1800") == True #boundary condition, On-point
    assert reg.is_valid_date_format("31/12/2006") == True #boundary condition, On-point
    assert reg.is_valid_date_format("29/02/2004") == True #leap year in correct format
    assert reg.is_valid_date_format("15/08/2006") == True #random valid date
    assert reg.is_valid_date_format("31/08/2006") == True #valid date, date is boundary value for months date range
    assert reg.is_valid_date_format("30/04/2006") == True #valid date, date is boundary value for months date range
    
    assert reg.is_valid_date_format("29-02-2006") == False #correct leap year date but invalid format
    assert reg.is_valid_date_format ("29/02/2006") == False #invalid date only exists in leap year
    assert reg.is_valid_date_format("30/02/2004") ==  False #date that is outside feburary range in leap year
    assert reg.is_valid_date_format("31/04/2006") == False #date falls outside that months date length
    assert reg.is_valid_date_format("32/08/2006") == False #date falls outside that months date length
    assert reg.is_valid_date_format("12/08/1799") == False # Off-point, outside year range
    assert reg.is_valid_date_format("12/08/2007") == False #off-point, outside year range
    assert reg.is_valid_date_format("13/07.2006") == False #invalid format
    assert reg.is_valid_date_format("12;08;2006") == False #invalid format
    assert reg.is_valid_date_format("asdhhuw") == False #nonsense input
    assert reg.is_valid_date_format("1/2/2006") == False #invalid date input
    assert reg.is_valid_date_format("-29/04/2006") == False #negative date
    assert reg.is_valid_date_format("ab/cd/efgh") == False #invalid dates
