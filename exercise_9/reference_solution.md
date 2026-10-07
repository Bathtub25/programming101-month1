# Reference and feedback: Rotate a List Once

Coach resource: review after the trainee has made and explained an attempt. This is one example, not the only valid approach.

## Example solution
```python
def rotate_once(items):
    if not items:
        return []
    result = [items[-1]]
    for index in range(len(items) - 1):
        result.append(items[index])
    return result
```

## Feedback guidance (no attempt submitted yet)
Praise preserving the last element and correct movement direction. Check that nothing is dropped or duplicated and that the input is unchanged.

## Review conversation
- Ask the trainee to trace a listed example and an edge case through their own code.
- Identify one specific strength before suggesting one concrete improvement.
- Compare the returned result with the challenge contract; do not require identical code.
- Have the trainee make the revision and explain why it fixes the issue.

## Validation
Use every example in [challenge.md](challenge.md), including empty input. Add a case that would expose a plausible mistake. Keep validation in the trainee’s own words and code.
