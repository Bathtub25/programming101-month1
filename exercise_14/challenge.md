# Challenge 14: Trace and Debug an Algorithm

## Problem and interface
Diagnose the faulty largest-value algorithm below, write a trace table, and implement a corrected function.

Implement `find_largest_fixed(numbers)`. Return the answer so callers can check it; printing examples is optional.

## Rules
Faulty algorithm: best = 0; for each number, if number < best, set best = number; return best. Do not use max() or sorting. Return None for empty input.

## Examples to check
| Arguments | Expected result |
| --- | --- |
| `[8, 3, 17]` | `17` |
| `[-8, -3, -17]` | `-3` |
| `[0]` | `0` |
| `[]` | `None` |

## Before coding
Write three to six steps in English. Trace an example with a small table of changing variables. Add one test of your own and predict its answer.

## Hint
Separate initialization errors from comparison errors. Change one idea at a time.

## Stretch challenge
Explain the invariant: best is the largest value examined so far.

## Done when
Your function meets the contract, passes the listed cases and your additional case, and you can explain why it works. For functions accepting lists, confirm the input is unchanged unless the stretch explicitly asks for in-place changes.
