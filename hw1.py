import data

# Write your functions for each part in the space below.

# Part 1
def vowel_count(word: str) -> int:
    vowels = 'AaEeIiOoUu'
    count = sum(1 for vowel in word if vowel in vowels)
    return count
#Purpose: Count the vowels in each word that is inputted
# Part 2
def short_lists(lists: list[list[int]]) -> list:
    return [n for n in lists if len(n) == 2]
#Purpose: List only the lists with two items
# Part 3
def ascending_pairs(lists: list[list[int]]) -> list:
    result = []
    for l in lists:
        if len(l) == 2:
            if l[0] > l[1]:
                result.append([l[1],l[0]])
            else:
                result.append(l)
        else:
            result.append(l)
    return result
#Purpose: List all lists and make lists with two items go from lowest to largest number
# Part 4
def add_prices(price1: data.Price, price2: data.Price) -> float:
    total_cents = price1.cents + price2.cents
    total_dollars = price1.dollars + price2.dollars + (total_cents // 100)
    total_cents = total_cents % 100
    total = total_dollars + total_cents / 100.0
    return total
#Purpose: Add two prices together and display exact total
# Part 5
def rectangle_area(rectangle: data.Rectangle) -> float:
    width = rectangle.bottom_right.x - rectangle.top_left.x
    height = rectangle.bottom_right.y - rectangle.top_left.y
    return width * height
#Purpose: Determine area of rectangle with two given points
# Part 6
def books_by_author(author: str, books: list[data.Book]) -> list[data.Book]:
    return [book for book in books if author in book.authors]
#Purpose: Find the book written by the inputted author
# Part 7
def circle_bound(rectangle: data.Rectangle) -> data.Circle:
    center_x = (rectangle.top_left.x + rectangle.bottom_right.x) / 2
    center_y = (rectangle.top_left.y + rectangle.bottom_right.y) / 2
    center = data.Point(center_x, center_y)
    corner_x = rectangle.top_left.x
    corner_y = rectangle.top_left.y
    radius = ((center.x - corner_x) ** 2 + (center.y - corner_y) ** 2)*(1/2)
    return data.Circle(center, radius)
#Create the smallest circle that can enclose the inputted rectangle points
# Part 8
def below_pay_average(employees: list[data.Employee]) -> list[str]:
    if not employees:
        return []
    total_pay = sum(employee.pay_rate for employee in employees)
    average_pay = total_pay / len(employees)
    below_average_employees = [employee.name for employee in employees if employee.pay_rate < average_pay]
    return below_average_employees
# Determines which employee is under the average pay rate by comparing every inputted employee's pay rate


