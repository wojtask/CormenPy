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
* The arithmetic, comparison, logical, and membership operators translate to equivalent Python operators.
* The basic mathematical functions for computing maximum, minimum, absolute value, floor, ceiling, etc. translate 
to appropriate Python built-in functions. The print instruction translates to `print` function.<br />
The constants $\const{true}$, $\const{false}$, $\const{nil}$ translate to `True`, `False`, `None`, respectively.
* Single and multiple assignments, $a \gets b$, $a \gets b \gets c$, translate to `a = b`, `a = b = c`, respectively.
* The swap instruction $\text{exchange } a \leftrightarrow b$ translates to `a, b = b, a`.
* Accessing and modifying array's cell via square brackets $A[i] \gets A[j]$ is realized with the same notation thanks
to redefined `__getitem__` and `__setitem__` methods in the implementation of Array data structure: `A[i] = A[j]`.
Accessing array's range of values, or subarray $A[i\twodots j]$, translates to `A[i:j]`.
* Accessing and modifying object's attribute $\id{heap-size}[A] \gets \id{length}[A]$ translate to
`A.heap_size = A.length`.
* The conditional statement
\begin{codebox}
\zi \If $\langle\id{condition1}\rangle$
\zi     \Then $\langle\id{statements1}\rangle$
\zi     \ElseIf $\langle\id{condition2}\rangle$
\zi         \Then $\langle\id{statements2}\rangle$
\zi     \ElseNoIf $\langle\id{statements3}\rangle$
        \End
\end{codebox}
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
\begin{codebox}
\zi \While $\langle\id{condition}\rangle$
\zi     \Do $\langle\id{statements}\rangle$
        \End
\end{codebox}
translates to

```Python
while <condition>:
    <statements>
```

* The looping statement
\begin{codebox}
\zi \Repeat $\langle\id{statements}\rangle$
\zi     \Until $\langle\id{condition}\rangle$
        \End
\end{codebox}
translates to the following Python construct:

```Python
while True:
    <statements>
    if <condition>:
        break
```

* The looping statements
\begin{codebox}
\zi \For $i \gets a$ \To $b$
\zi     \Do $\langle\id{statements}\rangle$
        \End
\end{codebox}
and 
\begin{codebox}
\zi \For $i \gets a$ \Downto $b$
\zi     \Do $\langle\id{statements}\rangle$
        \End
\end{codebox}
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

* Signaling an error by $\Error\ ``\text{message}"$ translates to
```Python
raise ValueError('message')
```

* Other constructs including plain English descriptions instead of formally written pseudocode instructions translate
to the most appropriate Python code, often moved to a separate protected function.

The Array data structure is a wrapper on plain Python list that adds length attribute and redefines square brackets
operators to access elements by its indexes from 1 instead of 0.
Array is used in implementations whenever an array is needed, instead of plain Python lists.