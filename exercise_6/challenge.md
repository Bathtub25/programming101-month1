# Challenge 6: Second Largest Number

## Problem and interface
Return the second-largest distinct integer.

Implement `second_largest(numbers)`. Return the answer so callers can check it; printing examples is optional.

## Rules
Do not sort or use set(), max(), or min(). Return None if fewer than two distinct values exist.

## Examples to check
| Arguments | Expected result |
| --- | --- |
| `[9, 4, 15, 2, 11, 7]` | `11` |
| `[10, 10, 8]` | `8` |
| `[5, 5]` | `None` |
| `[-3, -8, -5]` | `-5` |

## Before coding
Write three to six steps in English. Trace an example with a small table of changing variables. Add one test of your own and predict its answer.

## Hint
Track first and second place; ignore values equal to first place.

## Stretch challenge
Explain how the result would differ if duplicate positions counted.

## Done when
Your function meets the contract, passes the listed cases and your additional case, and you can explain why it works. For functions accepting lists, confirm the input is unchanged unless the stretch explicitly asks for in-place changes.
