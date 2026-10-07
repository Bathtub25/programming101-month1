# Challenge 8: Merge Two Sorted Lists

## Problem and interface
Merge two ascending lists of integers into a new ascending list, retaining duplicates.

Implement `merge_sorted(a, b)`. Return the answer so callers can check it; printing examples is optional.

## Rules
Inputs are already sorted. Do not use sorting; leave both inputs unchanged.

## Examples to check
| Arguments | Expected result |
| --- | --- |
| `[1, 4, 7, 12], [2, 3, 8, 10]` | `[1, 2, 3, 4, 7, 8, 10, 12]` |
| `[], [2]` | `[2]` |
| `[1, 2], [2, 3]` | `[1, 2, 2, 3]` |

## Before coding
Write three to six steps in English. Trace an example with a small table of changing variables. Add one test of your own and predict its answer.

## Hint
Track one position in each list and remember to copy leftovers.

## Stretch challenge
Merge three sorted lists by reusing your function.

## Done when
Your function meets the contract, passes the listed cases and your additional case, and you can explain why it works. For functions accepting lists, confirm the input is unchanged unless the stretch explicitly asks for in-place changes.
