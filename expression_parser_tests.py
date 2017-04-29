#!/usr/bin/env python

import expression_parser as parser

print(parser.evaluate('2.54E2 + 8/3 * (23 * (38.23*2/7)) - 2 * exp(2)', True))
print(parser.evaluate('2 * exp(2)', True))
print(parser.evaluate('(sin(1 - 2*(1+1)/2*cos(0)) + 1) / 3 + cos(0)', True))
print(parser.evaluate('3-5.1e-6', True))
print(parser.evaluate('sin(0) >= 0', True))