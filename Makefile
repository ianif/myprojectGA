# calculate_sum.py lalalalall
def calculate_sum(numbers):
    """
    Calculate the sum of numbers in a list.
    
    Args:
        numbers (list): A list of numbers.
        
    Returns:
        float: The sum of the numbers.
    """
    result = 0
    for num in numbers:
        result += num
    return result
```

The main performance issue is using a manual loop to calculate the sum. Python's built-in `sum()` function is more efficient. Here's the optimized version:

```python
# calculate_sum.py
def calculate_sum(numbers):
    """
    Calculate the sum of numbers in a list.
    
    Args:
        numbers (list): A list of numbers.
        
    Returns:
        float: The sum of the numbers.
    """
    return sum(numbers)
