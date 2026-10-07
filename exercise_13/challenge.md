# Challenge 13: Same Problem, Different Algorithms

## Problem and interface
Write two functions that return whether a list of integers contains a duplicate: pair search and a seen set.

Implement `has_duplicate_pairs(numbers); has_duplicate_seen(numbers)`. Return the answer so callers can check it; printing examples is optional.

## Rules
Return Boolean results. Leave input unchanged. Count pair comparisons for A and membership checks for B separately.

## Examples to check
| Arguments | Expected result |
| --- | --- |
| `[3, 1, 3]` | `True` |
| `[1, 2, 3]` | `False` |
| `[]` | `False` |

## Before coding
Write three to six steps in English. Trace an example with a small table of changing variables. Add one test of your own and predict its answer.

## Hint
A compares later positions. B checks whether a value was seen before adding it.

## Stretch challenge
Discuss extra memory and why list membership differs from set membership.

## Done when
Your function meets the contract, passes the listed cases and your additional case, and you can explain why it works. For functions accepting lists, confirm the input is unchanged unless the stretch explicitly asks for in-place changes.
