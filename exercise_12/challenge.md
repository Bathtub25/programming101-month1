# Challenge 12: Most Frequent Number

## Problem and interface
Return the integer appearing most often.

Implement `most_frequent(numbers)`. Return the answer so callers can check it; printing examples is optional.

## Rules
Return None for empty input. On tied counts, return the value appearing first in the input. Do not use Counter or .count(). First reuse a manual counting scan.

## Examples to check
| Arguments | Expected result |
| --- | --- |
| `[4, 2, 4, 7, 2, 4, 9]` | `4` |
| `[2, 1, 1, 2]` | `2` |
| `[]` | `None` |

## Before coding
Write three to six steps in English. Trace an example with a small table of changing variables. Add one test of your own and predict its answer.

## Hint
Count each candidate, replacing the winner only for a strictly greater count.

## Stretch challenge
Use a dictionary of counts, then scan input order to select the winner.

## Done when
Your function meets the contract, passes the listed cases and your additional case, and you can explain why it works. For functions accepting lists, confirm the input is unchanged unless the stretch explicitly asks for in-place changes.
