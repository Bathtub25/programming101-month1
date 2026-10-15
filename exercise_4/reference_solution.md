# Reference and feedback: Reverse a List

Coach resource: review after the trainee has made and explained an attempt. This is one example, not the only valid approach.

## Main solution: strengths

The trainee's reverse traversal is correct:

```python
length = len(list_of_numbers) - 1
for i in range(length, -1, -1):
    print(list_of_numbers[i])
```

They correctly identify the last valid index as `len(list_of_numbers) - 1` and walk backward to index `0`. This shows very good understanding of list indexes, reverse iteration, `range(start, stop, step)`, and the exclusive stop boundary. The stop is `-1` so that index `0` is included. Duplicate values, such as the two `5`s in the test list, are handled naturally because the traversal visits positions rather than searching by value.

## Main improvement: build and return the answer

The challenge asks for `reverse_list(items)` to return a new reversed list while leaving the input unchanged. Printing each item in reverse order does not construct that list.

For `[1, 5, 5, 6, 7, 4]`, the submitted program displays:

```text
4
7
6
5
5
1
```

It never creates `[4, 7, 6, 5, 5, 1]`. Ask the trainee:

> After your program finishes, where is the reversed list stored?

The answer is nowhere. Introduce `result = []`, append each item during the backward traversal, and return the completed list. Printing, constructing a data structure, and returning it to a caller are different operations. The caller can then decide how to display the result.

## Move the logic into a function

The main attempt has its logic at the top level. Move it into the requested `reverse_list(items)` interface so the algorithm can be reused with different inputs, including numbers, strings, an empty list, and a single-item list. Functions are not new here; the design habit to reinforce is that an algorithm should work beyond the one test list written at the top of a file.

### Example solution

```python
def reverse_list(items):
    result = []
    for index in range(len(items) - 1, -1, -1):
        result.append(items[index])
    return result


answer = reverse_list([1, 5, 5, 6, 7, 4])
print(answer)
```

This preserves the trainee's algorithm and leaves the original list unchanged. It is a coach reference, not a requirement to copy this exact code.

## Edge cases and validation

The existing traversal already handles empty input without crashing: `len([]) - 1` is `-1`, and `range(-1, -1, -1)` contains no indexes. With an output list, the function therefore returns `[]`. For a single item, the loop visits index `0` exactly once.

Test these cases explicitly after introducing a return value:

```python
assert reverse_list([]) == []
assert reverse_list([5]) == [5]
assert reverse_list([1, 2]) == [2, 1]
assert reverse_list([1, 5, 5, 6, 7, 4]) == [4, 7, 6, 5, 5, 1]
assert reverse_list(["a", "b", "c"]) == ["c", "b", "a"]

items = [1, 2, 3, 4, 5]
result = reverse_list(items)
assert result == [5, 4, 3, 2, 1]
assert items == [1, 2, 3, 4, 5]
assert result is not items
assert reverse_list([9]) == [9]
```

Use every example in [challenge.md](challenge.md), including empty input. Have the trainee add a case that would expose a plausible mistake, predict its answer, and explain validation in their own words and code.

## Stretch solution: reuse and decomposition

In `stretch_challenge.py`, the trainee moves the reverse traversal into `reverselist(numbers)`. That improves reusability. They also discover slicing:

```python
reverselist(numbers[startindex-1:endindex])
```

This decomposes the problem into two useful steps: choose part of the list, then reverse that part. That is very good exploratory thinking and problem decomposition.

The helper still prints individual values rather than returning a reversed list, and `find_conditionedreverse()` also has no return statement. Both therefore return `None`. Carry the main lesson through the helper and its caller: build the list in `reverse_list`, then return the result from the wrapper.

This review evaluates the submitted range-reversal experiment. The current stretch prompt in [challenge.md](challenge.md) instead asks for manual string reversal and a comparison of front insertion with appending; the experiment does not by itself complete that prompt. Front insertion is valid, but shifts existing items repeatedly. Discuss how the amount of work changes as the sequence grows compared with appending.

## Human positions, Python indexes, and slice boundaries

The expression `numbers[startindex-1:endindex]` appears to treat the arguments as human positions starting at 1, with both endpoints included. For example, `find_conditionedreverse(list_of_numbers, 2, 4)` selects `numbers[1:4]`: human positions 2, 3, and 4.

That conversion works for a deliberately 1-based, inclusive interface. Python's usual convention is different: indexes start at `0`, the slice start is included, and the slice end is excluded.

Ask:

> When we say start index 2, do we mean the second item or Python index 2?

For `["A", "B", "C", "D"]`, the second item is `"B"`, but Python index `2` refers to `"C"`. A slice `[1:4]` includes indexes `1`, `2`, and `3`, not index `4`. Agree on the interface and document the convention before changing boundaries. This understanding will matter in searching, sorting, and algorithms that track positions.

## Cleanup and naming

Inside `find_conditionedreverse`, `length`, `inrange`, and `rangelist` are unused. The large commented-out earlier approach shows useful experimentation, but once the trainee settles on an approach, remove abandoned code and unused variables. Code should contain what the program currently needs; Git preserves earlier versions.

Introduce Python's underscore-separated naming gradually:

| Current name | Suggested name |
| --- | --- |
| `reverselist` | `reverse_list` |
| `find_conditionedreverse` | `reverse_range` |
| `startindex` | `start_index` |
| `endindex` | `end_index` |

Good names make more complex algorithms easier to reason about. If the API deliberately accepts human positions, names such as `start_position` and `end_position` would make that choice clearer. Also, `length` in the traversal stores the last index rather than the length; `last_index` would describe it more accurately.

## Shortcuts intentionally avoided

Python offers `items[::-1]`, `reversed(items)`, and `items.reverse()`, but the lesson intentionally avoids reverse slicing and built-in reversal methods so the trainee learns the algorithm. Their reverse-index traversal is appropriate for this lesson. The forward slice used to select a subsection in the experiment is not reverse slicing; it selects the input for the manual traversal.

## Overall assessment

| Area | Assessment |
| --- | --- |
| Understanding reverse traversal | Excellent |
| Index/range understanding | Very good |
| Decomposing the stretch experiment | Very good |
| Producing the requested data structure | Needs improvement |
| Function design | Improved in stretch |
| Edge cases | Good implicitly; should test explicitly |
| Naming/readability | Needs gradual improvement |
| Cleaning unused code | Good next habit |

Exercise 4 is **conceptually successful but not yet complete**. The trainee understands how to traverse backward. The next step is to understand that printing an answer and building/returning an answer are different operations.

## Three teaching points before Exercise 5

1. **Build and return a new reversed list instead of printing each element.**
2. **Put the algorithm inside `reverse_list(items)` and test it against several inputs.**
3. **Clarify zero-based indexing and inclusive/exclusive slice boundaries**, especially in the stretch experiment.

Once those are understood, move on to Exercise 5.

## Review conversation

- Ask the trainee to trace a listed example and an edge case through their own code.
- Identify one specific strength before suggesting one concrete improvement.
- Compare the returned result with the challenge contract; do not require identical code.
- Have the trainee make the revision and explain why it fixes the issue.
