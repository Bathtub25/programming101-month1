# Reference and feedback: Same Problem, Different Algorithms

Coach resource: review after the trainee has made and explained an attempt. This is one example, not the only valid approach.

## Example solution
```python
def has_duplicate_pairs(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j]:
                return True
    return False


def has_duplicate_seen(numbers):
    seen = set()
    for number in numbers:
        if number in seen:
            return True
        seen.add(number)
    return False
```

## Feedback guidance (no attempt submitted yet)
Praise matching results across methods and honest operation counts. For n unique items, A makes n(n-1)/2 equality comparisons; B makes n membership checks, each expected constant time for a set. B uses extra memory. Do not equate a membership check with exactly one internal comparison.

## Review conversation
- Ask the trainee to trace a listed example and an edge case through their own code.
- Identify one specific strength before suggesting one concrete improvement.
- Compare the returned result with the challenge contract; do not require identical code.
- Have the trainee make the revision and explain why it fixes the issue.

## Validation
Use every example in [challenge.md](challenge.md), including empty input. Add a case that would expose a plausible mistake. Keep validation in the trainee’s own words and code.
