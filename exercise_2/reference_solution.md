# Reference and feedback: Find the Smallest Number

Coach resource: review after the trainee has made and explained an attempt. This is one example, not the only valid approach.

## Example solution
```python
def find_smallest(numbers):
    if not numbers:
        return None
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest
```

## Feedback on the existing attempt
The main attempt correctly initializes from the first item and compares with <. Rename find_max_from_list_of and maxNum to match their minimum purpose. Its unused betterOf returns a Boolean indicating b > a; remove it or give a helper a clear purpose. The stretch uses appropriate minimum logic and function naming. Improve minNum/betterOf to snake_case, return the answer, and handle empty input.

## Review conversation
- Ask the trainee to trace a listed example and an edge case through their own code.
- Identify one specific strength before suggesting one concrete improvement.
- Compare the returned result with the challenge contract; do not require identical code.
- Have the trainee make the revision and explain why it fixes the issue.

## Validation
Use every example in [challenge.md](challenge.md), including empty input. Add a case that would expose a plausible mistake. Keep validation in the trainee’s own words and code.
