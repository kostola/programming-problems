Celebrity
=========

Description
-----------

Consider a group of `n` people at a party.
You have a `n x n` boolean matrix `M` that tells you who knows who. The main diagonal is `null` and `M[i,j] = 1` means that person `i` knows person `j`.
This is not symmetrical, because `i` may know `j` but `j` may not know `i`. 

You must determine if in the group there is a CELEBRITY, that is a person that everybody knows but that knows nobody, and, if found, you must tell who he/she is.

You must do it WITHOUT recursion and WITHOUT nested cycles and you must produce a `O(n)` solution.

How to run the solution
-----------------------

The solution is written in Python 3. You simply have to launch the `main.py` script and it will tell you how to use it.
I developed both a linear and a quadratic solution, which are contained in the `celebrity.py` module.
