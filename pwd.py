# Imports.
from string import ascii_letters, digits, punctuation
from random import choice

# Initialize variables.
c = ''.join([ascii_letters, digits])
pwd = ''

"""
# Entropy:
print(len(c))
"""

# Settings! :D
_len = 64

# The auto-magic:
for i in range(_len):
  pwd += choice(c)

# Return.
print(pwd)