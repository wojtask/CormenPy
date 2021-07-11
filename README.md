# CormenPy
![Build & test](https://github.com/wojtask/CormenPy/actions/workflows/build.yml/badge.svg)

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
The constants <img alt="$\const{true}$" src="png//3c5ed3be14e4cf84ccac9388335c001f.png?invert_in_darkmode" align=middle width="38.357054999999995pt" height="16.831979999999998pt"/>, <img alt="$\const{false}$" src="png//f8508725a2f790482ec9cca9f4c65056.png?invert_in_darkmode" align=middle width="42.392625pt" height="16.831979999999998pt"/>, <img alt="$\const{nil}$" src="png//32a55e72e2051e842edd1675e4954db4.png?invert_in_darkmode" align=middle width="23.400795000000002pt" height="16.831979999999998pt"/> translate to `True`, `False`, `None`, respectively.
* Single and multiple assignments, <img alt="$a \gets b$" src="png//f15bb8038eea7497e46fb6acb023e1a4.png?invert_in_darkmode" align=middle width="41.194395pt" height="22.745910000000016pt"/>, <img alt="$a \gets b \gets c$" src="png//adab01d6245e93e1a45931b0f617d1bb.png?invert_in_darkmode" align=middle width="73.79080499999999pt" height="22.745910000000016pt"/>, translate to
`a = b`, `a = b = c`, respectively.
* The swap instruction <img alt="$\text{exchange } a \leftrightarrow b$" src="png//fdb7458cccb070fd7c8de8b985a63d2f.png?invert_in_darkmode" align=middle width="111.514095pt" height="22.745910000000016pt"/> translates to `a, b = b, a`.
* Accessing and modifying array's cell via square brackets <img alt="$A[i] \gets A[j]$" src="png//bdceb931d688fb5f4895588646c4314c.png?invert_in_darkmode" align=middle width="81.598605pt" height="24.56552999999997pt"/> is realized with the same notation thanks
to redefined `__getitem__` and `__setitem__` methods in the implementation of Array data structure: `A[i] = A[j]`.
Accessing array's range of values, or subarray <img alt="$A[i\twodots j]$" src="png//129a38cee7d24de477b0ad2733611804.png?invert_in_darkmode" align=middle width="52.05981pt" height="24.56552999999997pt"/>, translates to `A[i:j]`.
* Accessing and modifying object's attribute <img alt="$\id{heap-size}[A] \gets \id{length}[A]$" src="png//9b3b3829fee56a3c0246b4cc5af4c9e8.png?invert_in_darkmode" align=middle width="177.68569499999998pt" height="24.56552999999997pt"/> translate to
`A.heap_size = A.length`.
* The conditional statement
   <p align="center"><img alt="\begin{codebox}&#10;\zi \If $\langle\id{condition1}\rangle$&#10;\zi     \Then $\langle\id{statements1}\rangle$&#10;\zi     \ElseIf $\langle\id{condition2}\rangle$&#10;\zi         \Then $\langle\id{statements2}\rangle$&#10;\zi     \ElseNoIf $\langle\id{statements3}\rangle$&#10;        \End&#10;\end{codebox}" src="png//f59b0cdfdd0514fbed7a6647c90c23d0.png?invert_in_darkmode" align=middle width="165.5445pt" height="95.281065pt"/></p>
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
   <p align="center"><img alt="\begin{codebox}&#10;\zi \While $\langle\id{condition}\rangle$&#10;\zi     \Do $\langle\id{statements}\rangle$&#10;        \End&#10;\end{codebox}" src="png//98d81bd5edbe3b9ab27fd10030ec4106.png?invert_in_darkmode" align=middle width="156.40118999999999pt" height="36.10299pt"/></p>
   translates to

   ```Python
   while <condition>:
       <statements>
   ```

* The looping statement
   <p align="center"><img alt="\begin{codebox}&#10;\zi \Repeat $\langle\id{statements}\rangle$&#10;\zi     \Until $\langle\id{condition}\rangle$&#10;        \End&#10;\end{codebox}" src="png//d10be6e209929fb5987c1a73147405d7.png?invert_in_darkmode" align=middle width="156.206325pt" height="36.10299pt"/></p>
   translates to the following Python construct:

   ```Python
   while True:
       <statements>
       if <condition>:
           break
   ```

* The looping statements
   <p align="center"><img alt="\begin{codebox}&#10;\zi \For $i \gets a$ \To $b$&#10;\zi     \Do $\langle\id{statements}\rangle$&#10;        \End&#10;\end{codebox}" src="png//e2a1894b60048740af01cd7951acdc41.png?invert_in_darkmode" align=middle width="156.40118999999999pt" height="35.19318pt"/></p>
   and 
   <p align="center"><img alt="\begin{codebox}&#10;\zi \For $i \gets a$ \Downto $b$&#10;\zi     \Do $\langle\id{statements}\rangle$&#10;        \End&#10;\end{codebox}" src="png//4ee8b336893edad66d424904aa2ce086.png?invert_in_darkmode" align=middle width="156.40118999999999pt" height="35.19318pt"/></p>
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
   respectively, where `between(a, b)` is an alias for `range(a, b + 1)`, i.e., it returns the range from `a` to `b` inclusive, and `rbetween(a, b)` is an alias for `range(a, b - 1, -1)`.

* Signaling an error by <img alt='$\Error\ ``\text{message}"$' src="png//bdd898b1996e7a9d8e11de1b1077db19.png?invert_in_darkmode" align=middle width="121.04597999999999pt" height="22.745910000000016pt"/> translates to
   ```Python
   raise RuntimeError('message')
   ```

* Other constructs including plain English descriptions instead of formally written pseudocode instructions translate
to the most appropriate Python code, often moved to a separate protected function.

The Array data structure is a wrapper on plain Python list that adds length attribute and redefines square brackets
operators to access elements by its indexes from 1 instead of 0.
Array is used in implementations whenever an array is needed, instead of plain Python lists.