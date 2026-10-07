# Month 1: Algorithmic Thinking

## Objectives
Design an algorithm before coding, trace changing state by hand, define ambiguous requirements, test edge cases, debug with counterexamples, and compare the work and memory used by different correct algorithms. Practice Python functions, loops, comparisons, lists, and introductory sets and dictionaries.

## Getting started
Use Python 3. No external packages are needed. Work from the repository root; for example, run `python3 exercise_1/solution.py`.

## Trainee workflow
1. Open the exercise README and challenge; leave the reference closed initially.
2. Define inputs and outputs, write steps in English, and trace a small example.
3. Write your attempt in solution.py. Exercises 3–15 start with comments only; add your own functions and checks.
4. Check normal inputs, boundaries, duplicates, negative values where relevant, and empty inputs. Predict answers before running code. A file running without output does not prove it is correct.
5. Explain your reasoning to the coach, compare with the reference after discussion, and revise your code.
6. Record what you learned. Optionally make your own Git commit when ready; this setup does not create any commits.

## Folder contents
- README.md: learning goal, workflow, coaching prompt, and reflection.
- challenge.md: problem, interface, rules, examples, hint, and stretch.
- solution.py: trainee work only.
- reference_solution.md: separate example answer and feedback guidance.
- stretch_solution.py: preserved existing stretch attempts in Exercises 1 and 2.

The existing main and stretch files in Exercises 1 and 2 were renamed without changing their contents. Their original function names and print behavior are preserved; the challenge contracts describe targets for the trainee’s next revision.

## Four-week pacing
- Week 1: Exercises 1–4 — scan, track state, and build output.
- Week 2: Exercises 5–8 — reuse ideas, define ties, and manage multiple positions.
- Week 3: Exercises 9–12 — move data, generalize, and decompose problems.
- Week 4: Exercises 13–15 — compare algorithms, debug, and explain efficiency.

Allow time for discussion and revision instead of treating this as a speed test.

## Exercises
| Number | Exercise |
| --- | --- |
| 1 | [Find the Largest Number](exercise_1/README.md) |
| 2 | [Find the Smallest Number](exercise_2/README.md) |
| 3 | [Count Occurrences](exercise_3/README.md) |
| 4 | [Reverse a List](exercise_4/README.md) |
| 5 | [Palindrome Detector](exercise_5/README.md) |
| 6 | [Second Largest Number](exercise_6/README.md) |
| 7 | [Remove Duplicates](exercise_7/README.md) |
| 8 | [Merge Two Sorted Lists](exercise_8/README.md) |
| 9 | [Rotate a List Once](exercise_9/README.md) |
| 10 | [Rotate by K Positions](exercise_10/README.md) |
| 11 | [Two Numbers That Add to a Target](exercise_11/README.md) |
| 12 | [Most Frequent Number](exercise_12/README.md) |
| 13 | [Same Problem, Different Algorithms](exercise_13/README.md) |
| 14 | [Trace and Debug an Algorithm](exercise_14/README.md) |
| 15 | [Algorithm Race](exercise_15/README.md) |

## Coach guidance
Ask “What are you remembering?”, “Can you show a counterexample?”, and “How much work happens as the input grows?” Give progressively smaller prompts before showing an answer. Feedback on Exercises 1 and 2 refers to their actual preserved code; later feedback is a review guide, not an evaluation of work that has not been submitted.

The available conversation preview supplied the sequence through Exercise 13 and identified an algorithm-race finale. Exercises 14 and 15 here complete that progression with tracing/debugging and a linear-versus-binary search race; the original PDF was not available for exact reproduction.

## End-of-month mastery check
Choose an unfamiliar input and explain a solution without reading a reference. Trace each variable, justify initialization and stopping conditions, name an edge case, fix a deliberate bug, and compare two methods by correctness, work, and extra memory.
