import sys

from sayings import hello
from sayings import goodbye

if len(sys.argv) == 2:
    hello(sys.argv[1])

if len(sys.argv) == 2:
    goodbye(sys.argv[1])
