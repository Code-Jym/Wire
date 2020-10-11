"""
Python Strings, but better.
"""
class Wire():
    """
    Wire. Python Strings but better.
    """
    def __init__(self, wire):
        self.wire = wire

    """Basic Dunder Operations"""

    def __mul__(self, other):
        """
        Adds string together x times to form a new string
        e.g:
        >>> wire = Wire("hi")
        >>> wire * 3
        "hihihi"
        """

        self.wire = self.wire * other
        return self.wire

    def __add__(self, other):

        """
        Concantenates two strings
        """

        self.wire =  self.wire + other
        return self.wire

    def __sub__(self, other):

        """
        Removes the first instance of other that occures in the wire
        """

        self.wire  = self.wire.replace(other, "", 1)
        return self.wire
    
    def __truediv__(self, other):

        """
        Removes all instances of the other string/wire that occurs in the wire
        """

        self.wire = self.wire.replace(other, "")
        return self.wire

    def __len__(self):

        """
        Returns the length of the string
        """

        return len(self.wire)



    def getDiff(self, otherString):

        """
        Gets the difference this self and the other string/wire
        """

        diff = 0
        shortString, longString = None, None
        diff += abs(len(otherString) - len(self.wire)) # the difference in length is added to diff
        if len(otherString) > len(self.wire):
            shortString = self.wire
            longString = self.wire
        
        if len(self.wire) > len(otherString):
            shortString = otherString
            longString = self.wire

        else:
            pass

        if shortString != None:
            for index, letter in enumerate(shortString):
                if longString[index] != letter:
                    diff += 1
                if longString[index] != letter.lower() or longString[index] != letter.upper():
                    diff += 1
        
        if diff == 0:
            diff = True

        return diff
    
    def removeDuplicate(self, inOrder=True, caseSensitive=True):

        """
        Removes a duplicate  letter from a wire
        NOTE: having it not in order is faster than having it in order
        """

        singles = ""
        string = self.wire if caseSensitive else self.wire.lower()

        if inOrder:

            for letter in string:
                if letter not in singles:
                    singles += letter
            self.wire = singles

        else:

            for letter in set(string):
                singles += letter

            self.wire = singles

        return self.wire

