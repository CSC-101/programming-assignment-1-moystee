from unittest import expectedFailure

import data
import hw1
import unittest


# Write your test cases for each part below.
    # Part 1
class TestCases(unittest.TestCase):
    def test_vowel_count_1(self):
        input = 'second'
        result = hw1.vowel_count(input)
        expected = 2
        self.assertEqual(expected, result)
    def test_vowel_count_2(self):
        input = 'third'
        result = hw1.vowel_count(input)
        expected = 1
        self.assertEqual(expected, result)
    # Part 2
    def test_short_lists_1(self):
        input = [[2,3],[1,2,3]]
        result = hw1.short_lists(input)
        expected = [[2,3]]
        self.assertEqual(expected, result)
    def test_short_lists_1(self):
        input = [[1], [3,1], [0,1]]
        result = hw1.short_lists(input)
        expected = [[3, 1], [0,1]]
        self.assertEqual(expected, result)
    # Part 3
    def test_ascending_pairs_1(self):
        input = [[3,1],[1,0],[2,3]]
        result = hw1.ascending_pairs(input)
        expected = [[1,3],[0,1],[2,3]]
        self.assertEqual(expected, result)
    def test_ascending_pairs_2(self):
        input = [[1,3],[0,2,1],[4,3]]
        result = hw1.ascending_pairs(input)
        expected = [[1,3],[0,2,1],[3,4]]
        self.assertEqual(expected, result)
    # Part 4
    def test_add_prices_1(self):
        input1, input2 = data.Price(3,12), data.Price(2,29)
        result = hw1.add_prices(input1, input2)
        expected = 5.41
        self.assertEqual(expected, result)
    def test_add_prices_2(self):
        input1, input2 = data.Price(2,90), data.Price(1,90)
        result = hw1.add_prices(input1, input2)
        expected = 4.80
        self.assertEqual(expected, result)
    # Part 5
    def test_rectangle_area_1(self):
        input = data.Rectangle(data.Point(3, 20), data.Point(5, 40))
        result = hw1.rectangle_area(input)
        expected = 40.0
        self.assertEqual(expected, result)
    def test_rectangle_area_2(self):
        input = data.Rectangle(data.Point(7, 10), data.Point(12, 20))
        result = hw1.rectangle_area(input)
        expected = 50.0
        self.assertEqual(expected, result)
    # Part 6
    def test_books_by_author_1(self):
        library = [data.Book(['Neil Gaiman', 'Terry Pratchett'], 'Good Omens'), data.Book(['Dr. Seuss'], 'The Lorax')]
        result = hw1.books_by_author('Dr. Seuss', library)
        expected = [library[1]]
        self.assertEqual(expected, result)
    def test_books_by_author_2(self):
        library = [data.Book(['William Golding'], 'Lord of the Flies'), data.Book(['George Orwell'], 'Animal Farm')]
        result = hw1.books_by_author('George Orwell', library)
        expected = [library[1]]
        self.assertEqual(expected, result)
    # Part 7
    def test_circle_bound_1(self):
        input = data.Rectangle(data.Point(3, 20), data.Point(5, 40))
        result = hw1.rectangle_area(input)
        expected = 40
        self.assertEqual(expected, result)
    def test_circle_bound_2(self):
        input = data.Rectangle(data.Point(2, 20), data.Point(6, 40))
        result = hw1.rectangle_area(input)
        expected = 80
        self.assertEqual(expected, result)
    # Part 8
    def test_below_pay_average_1(self):
        library = [data.Employee("Jordan",20), data.Employee("Jared",30), data.Employee("Jerry",10)]
        result = hw1.below_pay_average(library)
        expected = ['Jerry']
        self.assertEqual(expected, result)
    def test_below_pay_average_2(self):
        library = [data.Employee("Alex", 40), data.Employee("Gus", 10), data.Employee("Brandon", 25)]
        result = hw1.below_pay_average(library)
        expected = ['Gus']
        self.assertEqual(expected, result)
if __name__ == '__main__':
    unittest.main()
