# Challenge 10: Rotate by K Positions

## Problem and interface
Return a new list rotated k positions to the right.

Implement `rotate_right(items, k)`. Return the answer so callers can check it; printing examples is optional.

## Rules
k is a nonnegative integer. Leave input unchanged; return [] for empty input. First try reusing rotation once.

## Examples to check
| Arguments | Expected result |
| --- | --- |
| `[1, 2, 3, 4, 5], 2` | `[4, 5, 1, 2, 3]` |
| `[1, 2, 3], 0` | `[1, 2, 3]` |
| `[1, 2, 3], 7` | `[3, 1, 2]` |
| `[], 9` | `[]` |

## Before coding
Write three to six steps in English. Trace an example with a small table of changing variables. Add one test of your own and predict its answer.

## Hint
Reduce k by the list length before doing work; guard empty input first.

## Stretch challenge
Build the result directly with index arithmetic in one pass.

## Done when
Your function meets the contract, passes the listed cases and your additional case, and you can explain why it works. For functions accepting lists, confirm the input is unchanged unless the stretch explicitly asks for in-place changes.
