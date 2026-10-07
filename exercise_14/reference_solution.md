# Reference and feedback: Trace and Debug an Algorithm

Coach resource: review after the trainee has made and explained an attempt. This is one example, not the only valid approach.

## Example solution
```python
def find_largest_fixed(numbers):
    if not numbers:
        return None
    best = numbers[0]
    for number in numbers:
        if number > best:
            best = number
    return best
```

## Feedback guidance (no attempt submitted yet)
Praise a counterexample and a trace with columns for current number, old best, comparison, and new best. Ask why changing only < to > still fails for all-negative input initialized at zero. This exercise revisits the observed Exercise 1 mistake without editing that original attempt.

## Review conversation
- Ask the trainee to trace a listed example and an edge case through their own code.
- Identify one specific strength before suggesting one concrete improvement.
- Compare the returned result with the challenge contract; do not require identical code.
- Have the trainee make the revision and explain why it fixes the issue.

## Validation
Use every example in [challenge.md](challenge.md), including empty input. Add a case that would expose a plausible mistake. Keep validation in the trainee’s own words and code.
