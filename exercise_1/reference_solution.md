# Reference and feedback: Find the Largest Number

Coach resource: review after the trainee has made and explained an attempt. This is one example, not the only valid approach.

## Example solution
```python
def find_largest(numbers):
    if not numbers:
        return None
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest
```

## Feedback on the existing attempt
The existing main attempt puts the scan in a function, which is a good start. However, x < maxNum selects smaller values, and starting at 0 returns 0 for the supplied positive list and fails for all-negative maximum searches. The stretch correctly starts with numbers[0] and uses a helper returning the larger value. Both attempts need an empty-input policy. Return the result rather than only printing it; use descriptive snake_case names such as largest and better_of.

## Review conversation
- Ask the trainee to trace a listed example and an edge case through their own code.
- Identify one specific strength before suggesting one concrete improvement.
- Compare the returned result with the challenge contract; do not require identical code.
- Have the trainee make the revision and explain why it fixes the issue.

## Validation
Use every example in [challenge.md](challenge.md), including empty input. Add a case that would expose a plausible mistake. Keep validation in the trainee’s own words and code.
