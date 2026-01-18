# examples
run_length_encoding("hello world!")
# =>      [[1,'h'],[1,'e'],[2,'l'],[1,'o'],[1,' '],[1,'w'],[1,'o'],[1,'r'],
#          [1,'l'],[1,'d'],[1,'!']]
run_length_encoding("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbb")
# =>      [[34,'a'], [3,'b']]

# my solution
import itertools
def run_length_encoding(s):
    groups = []
    for k, g in itertools.groupby(s):
        groups.append([len(list(g)), k])
    return groups

# others
from itertools import groupby
def run_length_encoding(s):
    return [[sum(1 for _ in g), c] for c, g in groupby(s)]

from itertools import groupby
def run_length_encoding(s):
    return [[len(list(g)), k] for k, g in groupby(s)]
