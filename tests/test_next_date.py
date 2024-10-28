import unittest

from next_date import next_date, is_leap_year, days_in_month

class TestNextDate(unittest.TestCase):
    def test_valid_standard_case(self):
        test_cases = [
            ('23-10-2024', '24-10-2024'),
            ('28-02-2024', '29-02-2024'),  # Leap year
            ('29-02-2024', '01-03-2024')   # Leap year February
        ]
        for date, expected in test_cases:
            with self.subTest(date=date):
                self.assertEqual(next_date(date), expected)

    def test_valid_end_of_month(self):
        # Test cases for the end of months transitioning to the next month
        month_end_dates = [
            ('31-01-2024', '01-02-2024'),  # January to February
            ('30-04-2024', '01-05-2024'),  # April to May
            ('31-12-2024', '01-01-2025')   # End of year
        ]
        for date, expected in month_end_dates:
            with self.subTest(date=date):
                self.assertEqual(next_date(date), expected)

    def test_valid_boundary_days_in_month(self):
        # Test all boundary cases for each month, both valid and invalid dates
        for year in [2023, 2024]:  # Non-leap year and leap year
            for month in range(1, 13):
                max_day = days_in_month(month, year)
                
                # Valid boundary date (last valid date of the month)
                valid_date = f'{max_day:02d}-{month:02d}-{year}'
                expected_date = f'01-{month + 1:02d}-{year}' if month < 12 else f'01-01-{year + 1}'
                
                with self.subTest(valid_date=valid_date):
                    self.assertEqual(next_date(valid_date), expected_date)
                
                # Invalid date (one day beyond the month limit)
                invalid_date = f'{max_day + 1:02d}-{month:02d}-{year}'
                with self.subTest(invalid_date=invalid_date):
                    self.assertRaises(ValueError, next_date, invalid_date)

    def test_invalid_day(self):
        # Invalid day values using a for loop
        invalid_days = [0, 32]
        for day in invalid_days:
            for month in range(1, 13):
                invalid_date = f'{day:02d}-{month:02d}-2024'
                with self.subTest(invalid_date=invalid_date):
                    self.assertRaises(ValueError, next_date, invalid_date)
    
    def test_invalid_month(self):
        # Invalid month values
        invalid_months = [0, 13]
        for month in invalid_months:
            invalid_date = f'15-{month:02d}-2024'
            with self.subTest(invalid_date=invalid_date):
                self.assertRaises(ValueError, next_date, invalid_date)
    
    def test_invalid_format(self):
        # Testing invalid date formats
        invalid_formats = ['2024-10-23', '23/10/2024', '10-23-24']
        for date_str in invalid_formats:
            with self.subTest(date_str=date_str):
                self.assertRaises(ValueError, next_date, date_str)

    def test_leap_year(self):
        # Test leap year calculation
        test_years = {
            2024: True,   # Leap year
            2023: False,  # Non-leap year
            2000: True,   # Leap year (divisible by 400)
            1900: False   # Non-leap year (divisible by 100, not 400)
        }
        for year, is_leap in test_years.items():
            with self.subTest(year=year):
                self.assertEqual(is_leap_year(year), is_leap)

    def test_days_in_month(self):
        # Test days in each month for both leap and non-leap years
        test_cases = [
            (1, 2024, 31),  # January
            (2, 2024, 29),  # February, leap year
            (2, 2023, 28),  # February, non-leap year
            (4, 2024, 30),  # April
            (6, 2024, 30),  # June
            (9, 2023, 30),  # September
            (11, 2023, 30), # November
            (12, 2023, 31)  # December
        ]
        for month, year, expected_days in test_cases:
            with self.subTest(month=month, year=year):
                self.assertEqual(days_in_month(month, year), expected_days)

if __name__ == '__main__':
    unittest.main()