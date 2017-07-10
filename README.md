# CormenPy

**CormenPy** provides implementations of algorithms and data structures from *Introduction to Algorithms*, ed. 2
by Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest and Clifford Stein.
It also contains implementations from *Introduction to Algorithms – Solutions to exercises and problems*
by Krzysztof Wojtas, that can be found [here](https://github.com/wojtask/CormenSol) (in Polish).

### Project objectives

The main **CormenPy** objectives are:
 * rewriting pseudocodes from the textbook and from the solutions to a real programming language,
 * implementing algorithms and data structures with no pseudocodes but precisely described,
 * providing tests for the implementations, effectively testing the solutions,
 * building foundation for a more sophisticated library of algorithms and data structures for real use.

The project was originally written in Java, but due to increasing complexity of data structures in later chapters
and difficulties in maintaining  similarities to the pseudocode notation, it was decided to migrate the code to another
language.
**Python 3** was chosen for a number of reasons:
 * it is widely known and used,
 * its syntax is very similar to the pseudocode syntax in the textbook,
 * it does not force to use any particular programming paradigm,
 * it's duck typed which is the concept that pseudocodes in the textbook rely on.

The implementations are written in a way to be as close as possible to the algorithms in the textbook or in the
solutions.
This implies using the procedural paradigm whenever possible and translating pseudocode notations to the most
appropriate Python statements by following the rules described in the next section.
The implementations of algorithms with no pseudocode provided are written in more concise way making use of Python
comprehensions and syntactic sugar, and are often divided into several functions to increase readability.

### Pseudocode translation rules

* All variable, attribute and procedure names translate to the most appropriate valid Python names with dashes and
apostrophes changed to underscores. All function names in the code are lowercase.
* Block structures indicated by indentations translate to the block structures indicated by indentations in Python.
* Single and multiple assignments
> a ← b
> a ← b ← c

translate to single and multiple assignments, `a = b`, `a = b = c`.
* The arithmetic, comparison, logical, and membership operators translate to equivalent Python operators.
* The basic mathematical functions for computing maximum, minimum, absolute value, floor, ceiling, etc. translate 
to appropriate Python built-in functions. The print instruction translates to `print` function.
* The constants
> TRUE
> FALSE
> NIL

translate to `True`, `False`, `None`, respectively.
* The swap instruction
> exchange a ↔ b

translates to `a, b = b, a`.
* Accessing and modifying array's cell via square brackets
> A[i] ← A[j]

is realized with the same notation thanks to redefined `__getitem__` and `__setitem__` functions in the implementation
of Array data structure:
```Python
A[i] = A[j]
```
Accessing array's range of values, or subarray
> A[i..j]

translates to
```Python
A[i:j]
```
* Accessing and modifying object's attribute
> heap-size[A] ← length[A]

translates to
```Python
A.heap_size = A.length
```
* The conditional statement
> if _condition1_
>     then _statements1_
> elseif _condition2_
>     then _statements2_
> else _statements3_

translates to
```Python
if <condition1>:
    <statements1>
elif <condition2>:
    <statements2>
else:
    <statements3>
```
* The looping statement
> while _condition_
>     do _statements_

translates to
```Python
while <condition>:
    <statements>
```
The looping statements
> for i ← a to b
>     do _statements_

and 
> for i ← a downto b
    do _statements_

translate to
```Python
for i in between(a, b):
    <statements>
```
and
```Python
for i in rbetween(a, b):
    <statements>
```
respectively, where `between(a, b)` is an alias for `range(a, b + 1)`, i.e., it returns the range from `a` to `b`
inclusive, and `rbetween(a, b)` is an alias for `range(a, b - 1, -1)`.
Finally, the looping statement
> repeat _statements_
>     until _condition_

translates to the following Python construct:
```Python
while True:
    <statements>
    if <condition>:
        break
```
* Signaling an error
> error _message_

translates to
```Python
raise RuntimeError(<message>)
```
* Other constructs including plain English descriptions instead of formally written pseudocode instructions translate
to the most appropriate Python code, often moved to a separate protected function.

The Array data structure is a wrapper on plain Python list that adds length attribute and redefines square brackets
operators to access elements by its indexes from 1 instead of 0.
Array is used in implementations whenever an array is needed, instead of plain Python lists.