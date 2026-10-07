# Reference and feedback: Remove Duplicates

Coach resource: review after the trainee has made and explained an attempt. This is one example, not the only valid approach.

## Example solution
```python
def remove_duplicates(items):
    result = []
    for item in items:
        if item not in result:
            result.append(item)
    return result
```

## Feedback guidance (no attempt submitted yet)
Praise stable order and separate output construction. List membership searches can make this quadratic in the worst case. A set alone loses the required order; a seen set plus result list preserves it.

## Review conversation
- Ask the trainee to trace a listed example and an edge case through their own code.
- Identify one specific strength before suggesting one concrete improvement.
- Compare the returned result with the challenge contract; do not require identical code.
- Have the trainee make the revision and explain why it fixes the issue.

## Validation
Use every example in [challenge.md](challenge.md), including empty input. Add a case that would expose a plausible mistake. Keep validation in the trainee’s own words and code.
