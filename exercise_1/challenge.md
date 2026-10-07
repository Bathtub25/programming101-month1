# Challenge 1: Find the Largest Number

## Problem and interface
Return the largest number in a list of integers.

Implement `find_largest(numbers)`. Return the answer so callers can check it; printing examples is optional.

## Rules
Do not use max(), sorting, or min(). Return None for an empty list.

## Examples to check
| Arguments | Expected result |
| --- | --- |
| `[8, 3, 17, 4, 12, 9]` | `17` |
| `[-8, -3, -17]` | `-3` |
| `[5, 5]` | `5` |
| `[]` | `None` |

## Before coding
Write three to six steps in English. Trace an example with a small table of changing variables. Add one test of your own and predict its answer.

## Hint
Choose an initial candidate from the input, then compare each item.

## Stretch challenge
Use a helper that returns the larger of two numbers.

## Done when
Your function meets the contract, passes the listed cases and your additional case, and you can explain why it works. For functions accepting lists, confirm the input is unchanged unless the stretch explicitly asks for in-place changes.
