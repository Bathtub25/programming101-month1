# Challenge 7: Remove Duplicates

## Problem and interface
Return a new list of unique integers, keeping their first appearance order.

Implement `remove_duplicates(items)`. Return the answer so callers can check it; printing examples is optional.

## Rules
Do not use set() or dictionaries for the core attempt. Leave the input unchanged.

## Examples to check
| Arguments | Expected result |
| --- | --- |
| `[3, 7, 3, 2, 7, 9, 2]` | `[3, 7, 2, 9]` |
| `[]` | `[]` |
| `[2, 2]` | `[2]` |

## Before coding
Write three to six steps in English. Trace an example with a small table of changing variables. Add one test of your own and predict its answer.

## Hint
Build a result and ask whether each value is already present.

## Stretch challenge
Use a seen set while preserving order; compare the amount of searching.

## Done when
Your function meets the contract, passes the listed cases and your additional case, and you can explain why it works. For functions accepting lists, confirm the input is unchanged unless the stretch explicitly asks for in-place changes.
