
def sort_numbers(numbers):
  """Sorts a list of numbers from lowest to highest.

  Args:
    numbers: A list of numbers to be sorted.

  Returns:
    A new list containing the numbers sorted from lowest to highest.
  """
  return sorted(numbers)

if __name__ == '__main__':
  numbers = [5, 2, 8, 1, 9, 4]
  sorted_numbers = sort_numbers(numbers)
  print(sorted_numbers)

