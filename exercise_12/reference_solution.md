# Reference and feedback: Most Frequent Number

Coach resource: review after the trainee has made and explained an attempt. This is one example, not the only valid approach.

## Example solution
```python
def most_frequent(numbers):
    winner = None
    best_count = 0
    for candidate in numbers:
        count = 0
        for number in numbers:
            if number == candidate:
                count += 1
        if count > best_count:
            winner = candidate
            best_count = count
    return winner
```

## Feedback guidance (no attempt submitted yet)
Praise decomposition into counting and choosing. Check that ties retain the first appearance. This beginner version recounts candidates; a dictionary can reduce repeated work.

## Review conversation
- Ask the trainee to trace a listed example and an edge case through their own code.
- Identify one specific strength before suggesting one concrete improvement.
- Compare the returned result with the challenge contract; do not require identical code.
- Have the trainee make the revision and explain why it fixes the issue.

## Validation
Use every example in [challenge.md](challenge.md), including empty input. Add a case that would expose a plausible mistake. Keep validation in the trainee’s own words and code.
