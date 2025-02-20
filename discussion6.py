import unittest
import os
from collections import defaultdict

def load_csv(f):
    '''
    Params: 
        f, name or path or CSV file: string

    Returns:
        nested dict structure from csv
        outer keys are (str) years, values are dicts
        inner keys are (str) months, values are (str) integers
    {
    2020: { jan: NUM, feb: num, etc},
    2021: {},
    2022: {},
    
    }
    Note: Don't strip or otherwise modify strings. Don't change datatypes from strings. 
    '''

    base_path = os.path.abspath(os.path.dirname(__file__))
    full_path = os.path.join(base_path, f)
    # use this 'full_path' variable as the file that you open
    ret_dict = {
        '2020': defaultdict(int),
        '2021': defaultdict(int),
        '2022': defaultdict(int)
    }

    got_first = False
    with open(full_path, 'r') as file:
        for line in file:
            if not got_first:
                got_first = True
                continue
            month, zero, one, two = line.split(",")
            ret_dict['2020'][month] = zero
            ret_dict['2021'][month] = one
            ret_dict['2022'][month] = two
    return ret_dict


def get_annual_max(d):
    '''
    Params:
        d, dict created by load_csv above

    Returns:
        list of tuples, each with 3 items: year (str), month (str), and max (int) 
        max is the maximum value for a month in that year, month is the corresponding month

    Note: Don't strip or otherwise modify strings. Do not change datatypes except where necessary.
        You'll have to change vals to int to compare them. 
    '''
    ret_list = []
    for year, y_d in d.items():
        max = 0
        max_month = ""
        for month, value in y_d.items():
            if int(value) > max:
                max_month = month
                max = int(value)
        ret_list.append((year, max_month, max))
    return ret_list

def get_month_avg(d):
    '''
    Params: 
        d, dict created by load_csv above

    Returns:
        dict where keys are years and vals are floats rounded to nearest whole num or int
        vals are the average vals for months in the year

    Note: Don't strip or otherwise modify strings. Do not change datatypes except where necessary. 
        You'll have to make the vals int or float here and round the avg to pass tests.
    '''
    ret_dict = {}
    for year, y_d in d.items():
        total = 0
        count = 0
        for month, value in y_d.items():
            total += float(value)
            count += 1
        ret_dict[year] = round(total / count)
    return ret_dict

class dis7_test(unittest.TestCase):
    '''
    you should not change these test cases!
    '''
    def setUp(self):
        self.flight_dict = load_csv('daily_visitors.csv')
        self.max_tup_list = get_annual_max(self.flight_dict)
        self.month_avg_dict = get_month_avg(self.flight_dict)

    def test_load_csv(self):
        self.assertIsInstance(self.flight_dict['2021'], dict)
        self.assertEqual(self.flight_dict['2020']['JUN'], '435')

    def test_get_annual_max(self):
        self.assertEqual(self.max_tup_list[2], ('2022', 'AUG', 628))

    def test_month_avg_list(self):
        self.assertAlmostEqual(self.month_avg_dict['2020'], 398, 0)

def main():
    unittest.main(verbosity=2)

if __name__ == '__main__':
    main()
