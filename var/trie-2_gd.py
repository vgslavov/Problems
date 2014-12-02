#!/usr/bin/env python 


# Based on code from 
# James Tauber, http://jtauber.com/ 
# http://jtauber.com/2005/02/trie.py
#
# Modified to keep lists of values
# find_all, find_all_key methods added by Gunnar

# the methods additem, removeitem, save and load are closely
# tied to what I needed this for, i.e. auto-completion of wiki-page names.
# these two modules are not needed if you don't use those methods:

import re
import cPickle


# damn unicode and regular expressions
# python's re moduel does not support checking for unicode properties
# this is a rather poor list of upper- and lower-case chars, most
# variations on aeoui's with various marks above are included
unicodeupper=u'\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc8\xc9\xca\xcb\xd2\xd3\xd4\xd5\xd6\xd8\xd9\xda\xdb\xdc\xd1\xcc\xcd\xce\xcf\xc7'
unicodelower=u'\xc3\xa1\xc3\xa0\xc3\xa2\xc3\xa3\xc3\xa4\xc3\xa5\xc3\xa6\xc3\xa8\xc3\xa9\xc3\xaa\xc3\xab\xc3\xb2\xc3\xb3\xc3\xb4\xc3\xb5\xc3\xb6\xc3\xb8\xc3\xb9\xc3\xba\xc3\xbb\xc3\xbc\xc3\xb1\xc3\xac\xc3\xad\xc3\xae\xc3\xaf\xc3\xa7'



class Trie:
    """
    A Trie is like a dictionary in that it maps keys to values. However,
    because of the way keys are stored, it allows look up based on the
    longest prefix that matches.
    """

    def __init__(self):
        self.root = [[], {}]


    def add(self, key, value):
        """
        Add the given value for the given key.
        """
        
        curr_node = self.root
        for ch in key:
            curr_node = curr_node[1].setdefault(ch, [[], {}])
        curr_node[0].append( value )


    def find(self, key):
        """
        Return the values for the given key or None if key not found.
        """
        
        curr_node = self.root
        for ch in key:
            try:
                curr_node = curr_node[1][ch]
            except KeyError:
                return None
        return curr_node[0]


    def find_prefix(self, key):
        """
        Find as much of the key as one can, by using the longest
        prefix that has a value. Return (values, remainder) where
        remainder is the rest of the given string.
        """
        
        curr_node = self.root
        remainder = key
        for ch in key:
            try:
                curr_node = curr_node[1][ch]
            except KeyError:
                return (curr_node[0], remainder)
            remainder = remainder[1:]
        return (curr_node[0], remainder)

    def find_all_prefix(self, key, node=None):
        '''Find all values whose keys are a prefix of this key'''

        if node==None: node=self.root
        
        res=[]

        res+=node[0]

        if key=="": return res

        if key[0] in node[1]:
            res+=self.find_all_prefix(key[1:], node[1][key[0]])
        
        return res            

    def find_all(self, key, limit=-1, node=None, sofar=0):
        '''Find all values who have this key as their prefix'''
        
        if node==None: node=self.root

        if limit!=-1 and sofar>=limit: return []

        res=[]

        if key!="":
            if key[0] in node[1]:
                res+=self.find_all(key[1:], limit, node[1][key[0]], sofar)
        else: 
            if limit==-1:
                res+=node[0]
            else: 
                res+=node[0][:max(limit-sofar,0)]

            for n in node[1].values():
                res+=self.find_all("",limit, n, len(res))
        
        return res            

    def find_all_key(self, key, limit=-1, node=None, sofar=0, keysofar=""):
        '''Find all values who have this key as their prefix
        return both key and value'''
        
        if node==None: node=self.root

        if limit!=-1 and sofar>=limit: return []        

        res=[]
        if key!="":
            if key[0] in node[1]:
                res+=self.find_all_key(key[1:], limit, node[1][key[0]], sofar, keysofar+key[0])
        else: 
            if limit==-1:
                res+=[(keysofar, x) for x in node[0]]
            else: 
                res+=[(keysofar, x) for x in node[0][:max(0,limit-sofar)]]

            for k,n in node[1].iteritems():
                res+=self.find_all_key("",limit,n,len(res),keysofar+k)
        
        return res            


    def remove(self, key,value):
        curr_node = self.root
        for ch in key:
            try:
                curr_node = curr_node[1][ch]
            except KeyError:
                return None
        try:
            curr_node[0].remove(value)
        except ValueError: 
            # just ignore
            pass 

    def additem(self, item): 
        """
        index a CamelCased string
        each Camel-term or space separated word is indexed
        """
        terms=re.split("([A-Z%s][a-z%s]+)| "%(unicodeupper, unicodelower), item)
        for t in filter(None, terms):
            self.add(t.lower(),item)
        self.add(item.lower(),item)
    
    def removeitem(self, item):
        """
        remove a CamelCased string
        """
        terms=re.split("([A-Z%s][a-z%s]+)| "%(unicodeupper, unicodelower), item)
        for t in filter(None, terms):
            self.remove(t.lower(),item)
        self.remove(item.lower(),item)
        
                 

    def save(self, path): 
        f=file(path,"w")
        cPickle.dump(self, f)
        f.close()

    @staticmethod
    def load(path): 
        f=file(path)
        r=cPickle.load(f)
        f.close()
        return r

if __name__ == "__main__":    

    t = Trie()
    t.add("fo", "B")
    t.add("foo", "A")
    t.add("l", "C")
    t.add("folish", "D")

    #import pprint 
    #pprint.pprint(t.root)

    assert t.find("fo") == ["B"]
    assert t.find("fool") == None

    assert t.find_prefix("fo") == (["B"], "")
    assert t.find_prefix("fool") == (["A"], "l")

    assert t.find_all_prefix("fo") == ['B']
    assert t.find_all_prefix("foo") == ['B', 'A']

    assert t.find_all("fo") == ['B', 'D', 'A']
    assert t.find_all("foo") == ['A']

    assert t.find_all_key("fo") == [('fo', 'B'), ('folish', 'D'), ('foo', 'A')]

    assert t.find_all_key("foo") == [('foo', 'A')]

    t.additem("SemanticDesktop")
    t.additem("CamelCase")
    t.additem("A test")
    
    # return 3 things because string is indexed by Case, Camel and CamelCase
    assert t.find_all("ca") == ['CamelCase', 'CamelCase', 'CamelCase']
    assert t.find_all("case") == ['CamelCase']
    assert t.find_all("a") == ['A test', 'A test']
    
    t.removeitem("CamelCase")

    assert t.find_all("ca") == []
    assert t.find_all("a") == ['A test', 'A test']

    print "It's A'OK!"
