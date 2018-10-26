"""
8.14 Boolean Evaluation: Given a boolean expression consisting of the symbols 0 (false), 1 (true), &
(AND), I (OR), and /\ (XOR), and a desired boolean result value result, implement a function to
count the number of ways of parenthesizing the expression such that it evaluates to result. The
expression should be fully parenthesized (e.g., ( 0) A( 1)) but not extraneously (e.g., ( ( ( 0)) /\ ( 1)) ).
EXAMPLE
countEval("l/\01011", false) -> 2
countEval("0&0&0&1All0", true)-> 10
"""
