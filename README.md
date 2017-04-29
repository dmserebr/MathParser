# MathParser
Math expression parser and evaluator in Python

Usage:
`evaluate(str)` - parses the string, evaluates it and returns the value

Example:
```
#!/usr/bin/python
import expression_parser as parser
print(parser.evaluate('(sin(1 - 3/2*exp(2)) + 1) / 2'))

----------------
0.806086656397
```
Supported expressions:
* arithmetic operations (+-*/^)
* logical operations (&& ||), avalilable also by aliases (and, or)
* comparison operations (== != > < >= <=)
* mathematical functions (sin cos exp log)
* brackets ()

Under the hood, the parser converts the expression to the [reverse Polish notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation) and then evaluates it step-by-step.
