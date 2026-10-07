# Reference and feedback: Count Occurrences

Coach resource: review after the trainee has made and explained an attempt. This is one example, not the only valid approach.

## Example solution
```python
def count_value(numbers, target):
    count = 0
    for number in numbers:
        if number == target:
            count += 1
    return count
```

## Feedback guidance (no attempt submitted yet)
Praise a correctly initialized counter and a reusable target parameter. Check that the counter is not reset inside the loop and changes only on matches.

## Review conversation
- Ask the trainee to trace a listed example and an edge case through their own code.
- Identify one specific strength before suggesting one concrete improvement.
- Compare the returned result with the challenge contract; do not require identical code.
- Have the trainee make the revision and explain why it fixes the issue.

## Validation
Use every example in [challenge.md](challenge.md), including empty input. Add a case that would expose a plausible mistake. Keep validation in the trainee’s own words and code.
