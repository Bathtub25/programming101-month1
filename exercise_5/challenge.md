# Challenge 5: Palindrome Detector

## Problem and interface
Return whether text reads the same forwards and backwards.

Implement `is_palindrome(text)`. Return the answer so callers can check it; printing examples is optional.

## Rules
Compare exact characters: case, spaces, and punctuation matter. Empty text is a palindrome. Avoid reverse helpers and reverse slicing.

## Examples to check
| Arguments | Expected result |
| --- | --- |
| `'racecar'` | `True` |
| `'hello'` | `False` |
| `''` | `True` |
| `'Level'` | `False` |

## Before coding
Write three to six steps in English. Trace an example with a small table of changing variables. Add one test of your own and predict its answer.

## Hint
Move inward from both ends and stop when a mismatch appears.

## Stretch challenge
Normalize case and ignore punctuation in a separate version.

## Done when
Your function meets the contract, passes the listed cases and your additional case, and you can explain why it works. For functions accepting lists, confirm the input is unchanged unless the stretch explicitly asks for in-place changes.
