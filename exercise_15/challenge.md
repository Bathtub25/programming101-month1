# Challenge 15: Algorithm Race

## Problem and interface
Search an ascending list of integers using a linear scan and a binary search. Return whether target is present.

Implement `linear_contains(numbers, target); binary_contains(numbers, target)`. Return the answer so callers can check it; printing examples is optional.

## Rules
Inputs are already sorted. Do not use in, .index(), bisect, or sorting for search. Count inspected positions separately from elapsed time.

## Examples to check
| Arguments | Expected result |
| --- | --- |
| `[1, 3, 5, 7, 9], 7` | `True` |
| `[1, 3, 5, 7, 9], 2` | `False` |
| `[], 4` | `False` |
| `[4], 4` | `True` |

## Before coding
Write three to six steps in English. Trace an example with a small table of changing variables. Add one test of your own and predict its answer.

## Hint
Use inclusive lower and upper indices; after checking the middle, exclude it from the next search interval.

## Stretch challenge
Measure inspected positions for sizes 8, 32, 128, and 512; include absent targets.

## Done when
Your function meets the contract, passes the listed cases and your additional case, and you can explain why it works. For functions accepting lists, confirm the input is unchanged unless the stretch explicitly asks for in-place changes.
