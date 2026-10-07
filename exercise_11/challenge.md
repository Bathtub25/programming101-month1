# Challenge 11: Two Numbers That Add to a Target

## Problem and interface
Return a tuple of two values whose sum is target, or None if no pair exists.

Implement `two_sum(numbers, target)`. Return the answer so callers can check it; printing examples is optional.

## Rules
Use two different list positions. Any valid pair is accepted. Start with trying pairs; do not reuse a single item.

## Examples to check
| Arguments | Expected result |
| --- | --- |
| `[4, 7, 1, 9, 3], 10` | `(7, 3)` |
| `[5], 10` | `None` |
| `[5, 5], 10` | `(5, 5)` |
| `[], 1` | `None` |

For pair search, any pair meeting the rules is correct.

## Before coding
Write three to six steps in English. Trace an example with a small table of changing variables. Add one test of your own and predict its answer.

## Hint
For each first index, start the second index after it.

## Stretch challenge
Use a seen set and the complement target - current; compare growth.

## Done when
Your function meets the contract, passes the listed cases and your additional case, and you can explain why it works. For functions accepting lists, confirm the input is unchanged unless the stretch explicitly asks for in-place changes.
