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

## Exercise 3 review

### Main solution: strengths

The core counting algorithm is correct: it initializes a counter to `0`, scans the list once, and increments only when the current value matches the target. It also correctly chooses between "time" and "times" in the displayed answer.

The trainee has understood the main learning objective: **using an accumulator**.

```python
instances = 0
for x in numbers:
    if x == targetnum:
        instances = instances + 1
```

The invalid-input check also shows thinking beyond the happy path:

```python
if targetnum == None or numbers == None:
```

This was not required by the exercise, but it is a useful sign of edge-case awareness.

### Main solution: improvements

**Name the function for what it does.** The current name, `find_max_from_list_of(numbers, targetnum)`, carries over from Exercises 1 and 2. This function counts occurrences; it does not find a maximum. Rename it to match the requested interface:

```python
def count_value(numbers, target):
```

**Return the answer and let the caller display it.** The current function prints its result:

```python
print("Number occurs", instances, "times")
```

The challenge asks for a returned count. End the function with:

```python
return instances
```

Then the caller can decide how to display or use the result:

```python
count = count_value(list_of_numbers, wantednum)
unit = "time" if count == 1 else "times"
print("Number occurs", count, unit)
```

Returning a value makes the function reusable and lets callers check the answer. This distinction will become increasingly important in later exercises.

**Introduce `is None` gradually.** The current `targetnum == None` check works here, but the usual Python style is an identity check:

```python
if targetnum is None or numbers is None:
```

Treat this as a useful habit to introduce, not a major style lesson at this stage.

### Stretch solution: generalization

The stretch solution shows good algorithmic understanding. The trainee successfully generalized from **counting occurrences of one particular value** to **counting values satisfying a condition**. They created two cases and count matching elements in each case.

The important insight is that the accumulator algorithm stays the same; only the test changes:

```python
num = 0
for x in numbers:
    if ...:
        num = num + 1
```

That pattern appears constantly in programming and is exactly the conceptual leap the stretch challenge is intended to encourage.

### Stretch solution: zero and the specification

The solution uses `x >= 0` for "greaterthanzero" and `x <= 0` for "lessthanzero". Zero therefore satisfies both conditions.

If those names literally mean "greater than zero" and "less than zero", the comparisons should be `x > 0` and `x < 0`. Zero would then count in neither category. If inclusive comparisons are intended, the condition names should describe that instead.

This is a specification and boundary-condition teaching opportunity, not merely a Python issue. Ask the trainee **"Where should zero belong?"** and let them reason it through. Their current all-positive example cannot expose the difference. A useful trace is `[-2, 0, 3]`: strict comparisons produce one match in each category; inclusive comparisons produce two in each category.

### Stretch solution: duplicated loops and refactoring

Representing conditions with strings such as `"greaterthanzero"` and `"lessthanzero"` is acceptable at this stage. However, the branches repeat the same counting loop in the source code. Only one branch runs per call; the duplication is in the code structure.

Ask: **"Why are we repeating the loop in our source code when the process is exactly the same?"** Do not give the answer immediately. Eventually, guide the trainee toward a single loop with a changing test:

```python
for x in numbers:
    if condition == "greaterthanzero" and x > 0:
        num += 1
    elif condition == "lessthanzero" and x < 0:
        num += 1
```

Keep invalid-condition handling outside the loop so it also works for empty input. The strict comparisons above assume the trainee has clarified that zero belongs in neither category.

Much later, this can naturally evolve into passing a function that expresses the condition:

```python
def count_if(numbers, condition):
    count = 0
    for number in numbers:
        if condition(number):
            count += 1
    return count
```

Functions as values are probably too early to require now, but this example can be revisited when that concept is introduced.

### Overall assessment

| Area | Assessment |
| --- | --- |
| Core algorithm | Excellent |
| Understanding the accumulator | Excellent |
| Edge-case thinking | Very good |
| Generalization in the stretch solution | Very good |
| Function naming | Needs improvement |
| Return vs. print | Next concept to reinforce |
| Code duplication | Good future refactoring opportunity |

Overall, this is **a successful Exercise 3**. The trainee appears to understand the underlying idea rather than merely copying syntax. The counting logic is sound, while returning the result is still needed to meet the main challenge's interface.

### Three recommended teaching points

Before moving on, focus the teaching conversation on:

1. **Rename functions based on what they actually do.**
2. **Functions should usually return answers; callers decide how to display them.**
3. **Ask "Does zero count as greater or less than zero?"** Let the trainee discover and explain the boundary-condition issue.

Do not rewrite the trainee's solution for them. These small imperfections provide useful concepts to teach; have the trainee make and explain their own revisions.

## Review conversation
- Ask the trainee to trace a listed example and an edge case through their own code.
- Identify one specific strength before suggesting one concrete improvement.
- Compare the returned result with the challenge contract; do not require identical code.
- Have the trainee make the revision and explain why it fixes the issue.

## Validation
Use every example in [challenge.md](challenge.md), including empty input. Add a case that would expose a plausible mistake. Keep validation in the trainee’s own words and code.
