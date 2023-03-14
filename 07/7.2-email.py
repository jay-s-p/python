"""
7.2 Regular expression for email like. [a-z].[az]@[a-z].domainname ("@" not
be repeated and last "." not repeated). Extract email from text
"""

import re

txt = 'My email is a.b@mail.com and c.d@mail.com'
myemail = re.findall('[\w\.-]+@[\w\.-]+', txt)
print(myemail)

""" O/P :-
['a.b@mail.com', 'c.d@mail.com']
"""