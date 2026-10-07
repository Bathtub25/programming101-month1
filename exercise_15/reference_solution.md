# Reference and feedback: Algorithm Race

Coach resource: review after the trainee has made and explained an attempt. This is one example, not the only valid approach.

## Example solution
```python
def linear_contains(numbers, target):
    for number in numbers:
        if number == target:
            return True
    return False


def binary_contains(numbers, target):
    low, high = 0, len(numbers) - 1
    while low <= high:
        middle = (low + high) // 2
        if numbers[middle] == target:
            return True
        if numbers[middle] < target:
            low = middle + 1
        else:
            high = middle - 1
    return False
```

## Feedback guidance (no attempt submitted yet)
Praise correct results before speed claims. Check endpoints, empty input, and absent targets. Linear search inspects at most n positions; binary search halves the interval and needs logarithmic inspections. Its sorted-input requirement matters. Tiny timing differences are noisy; operation counts show the pattern more clearly.

## Review conversation
- Ask the trainee to trace a listed example and an edge case through their own code.
- Identify one specific strength before suggesting one concrete improvement.
- Compare the returned result with the challenge contract; do not require identical code.
- Have the trainee make the revision and explain why it fixes the issue.

## Validation
Use every example in [challenge.md](challenge.md), including empty input. Add a case that would expose a plausible mistake. Keep validation in the trainee’s own words and code.
