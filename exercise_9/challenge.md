# Challenge 9: Rotate a List Once

## Problem and interface
Return a new list rotated one position to the right.

Implement `rotate_once(items)`. Return the answer so callers can check it; printing examples is optional.

## Rules
Leave input unchanged. Handle empty input. Use explicit movement rather than a slicing shortcut.

## Examples to check
| Arguments | Expected result |
| --- | --- |
| `[1, 2, 3, 4, 5]` | `[5, 1, 2, 3, 4]` |
| `[]` | `[]` |
| `[7]` | `[7]` |

## Before coding
Write three to six steps in English. Trace an example with a small table of changing variables. Add one test of your own and predict its answer.

## Hint
Place the last item first, then copy the remaining items in order.

## Stretch challenge
Implement an in-place version, saving the last value before shifting.

## Done when
Your function meets the contract, passes the listed cases and your additional case, and you can explain why it works. For functions accepting lists, confirm the input is unchanged unless the stretch explicitly asks for in-place changes.
