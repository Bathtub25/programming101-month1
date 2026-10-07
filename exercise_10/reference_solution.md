# Reference and feedback: Rotate by K Positions

Coach resource: review after the trainee has made and explained an attempt. This is one example, not the only valid approach.

## Example solution
```python
def rotate_right(items, k):
    if not items:
        return []
    size = len(items)
    k %= size
    result = []
    for index in range(size):
        result.append(items[(index - k) % size])
    return result
```

## Feedback guidance (no attempt submitted yet)
Praise reuse in the first version and modulo reduction. Compare repeated one-step rotation with this direct linear scan. Check k=0 and k greater than the length.

## Review conversation
- Ask the trainee to trace a listed example and an edge case through their own code.
- Identify one specific strength before suggesting one concrete improvement.
- Compare the returned result with the challenge contract; do not require identical code.
- Have the trainee make the revision and explain why it fixes the issue.

## Validation
Use every example in [challenge.md](challenge.md), including empty input. Add a case that would expose a plausible mistake. Keep validation in the trainee’s own words and code.
