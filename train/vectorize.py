"""
A utility for converting strings to arrays and vice versa
"""

import numpy

ALPHA = tuple("abcdefghijklmnopqrstuvwxyz")
NUM = tuple("0123456789")
UPPER = ALPHA.upper()

class Vectorizer:
    def __init__(self,mode):
        """
        Mode:

        The mode of vectorization
        Combine sets ALPHA, NUM, and UPPER by seperating them using spaces

        Examples:
        "ALPHA NUM" - All lowercase letters plus numbers
        "ALPHA UPPER NUM" - All alphanumeric characters

        Alternatively, use "ALL" to use all ASCII characters
        """

        mode = mode.upper().strip()
        self.mode = mode
        self.chrset = []

        if mode=="ALL":
            for i in range(256):
                self.chrset.append(chr(i))
        else:
            subsets = mode.split(" ")
            while "" in subsets:
                subsets.remove(" ")
            for subset in subsets: self.chrset+=eval(subset)
        self.maximum = len(self.chrset)
        self.chrset = tuple(self.chrset)
    def toIndex(self,char):
        return self.chrset.index(char)
    def fromIndex(self,index):
        return self.chrset[index]
    def toValue(self,char):
        return toIndex(char)/self.maximum
    def fromValue(self,value):
        return fromIndex(value*self.maximum)
    def vectorize(self,string):
        return (toValue(c) for c in string)
    def toString(self,vectorized):
        new = ""
        for i in vectorized:
            new+=fromValue(i)
        return new
