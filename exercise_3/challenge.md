# Challenge 3: Count Occurrences

## Problem and interface
Count how many times target appears.

Implement `count_value(numbers, target)`. Return the answer so callers can check it; printing examples is optional.

## Rules
Do not use .count(). Return 0 for empty input.

## Examples to check
| Arguments | Expected result |
| --- | --- |
| `[7, 3, 7, 4, 1, 7, 9, 2], 7` | `3` |
| `[1, 2], 7` | `0` |
| `[], 7` | `0` |

## Before coding
Write three to six steps in English. Trace an example with a small table of changing variables. Add one test of your own and predict its answer.

## Hint
Start a counter at zero and update it only for a match.

## Stretch challenge
Count values satisfying a condition, such as even numbers.

## Done when
Your function meets the contract, passes the listed cases and your additional case, and you can explain why it works. For functions accepting lists, confirm the input is unchanged unless the stretch explicitly asks for in-place changes.
