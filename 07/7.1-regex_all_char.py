"""
Write following programs using regular expressions:-
    All character
"""

import re as re

str = "He1lo W0rld"
x = re.findall('\D+', str)
print(x)

""" O/P :-
['He', 'lo W', 'rld']
"""