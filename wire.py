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
    def __repr__(self):
        """
        Returns wire
        """
        return self.wire

    def __str__(self):
        """
        Returns wire
        """
        return self.wire

    def __mul__(self, other):
        """
        Adds string together x times to form a new string
        e.g:
        >>> wire = Wire("hi")
        >>> wire * 3
        "hihihi"

        Returns a wire containing the string
        """

        self.wire = self.wire * other
        return self.wire

    def __add__(self, other):

        """
        Concantenates two strings
        >>> wire = Wire("hi")
        >>> wire + "low"
        "hilow"
        """

        self.wire =  self.wire + other
        return self.wire

    def __sub__(self, other):

        """
        Removes the first instance of other that occures in the wire
        Returns a wire object
        >>> wire = Wire("hihilow")
        >>> wire - "hi"
        "hilow"
        """

        self.wire  = self.wire.replace(other, "", 1)
        return self.wire
    
    def __truediv__(self, other):

        """
        Removes all instances of the other string/wire that occurs in the wire
        Returns a wire object
        >>> wire = Wire("hihilow")
        >>> wire / "hi"
        "low"
        """

        self.wire = self.wire.replace(other, "")
        return self.wire

    def __len__(self):

        """
        Returns the length of the string
        >>> wire = Wire("hi")
        >>> len(wire)
        2
        """

        return len(self.wire)
    
    """Functions that are reimplementations of strings"""
    def replace(self, old, new, count=None):
        """
        Replaces a the character(s) in a wire with other character(s)
        >>> wire = Wire("this is cool, this is not cool")
        >>> wire.replace("this", "it", 1)
        it is cool, this is not cool
        If count == None, then it will replace instances of the character(s)
        to be replaced
        """
        self.wire.replace(old, new, count)
        return self.wire


    """Functions that are unique to wires"""

    def getDiff(self, otherString):

        """
        Gets the difference this self and the other string/wire and returns it
        >>> wire = Wire("hi")
        >>> new_wire = Wire("Hilow")
        >>> wire.getDiff(new_wire)
        4
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
        NOTE: not having it in order, and not having it caseSensitive is the fastest
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

    def forEach(self, action, *args, **kwargs):

        """
        Equivalent of:
        >>> for i in wire:
        ...    action(i, *args, **kwargs)
        yields the result of each action
        NOTE: the letter being processed has to be the first argument 
        """

        for letter in self.wire:
            yield action(letter, *args, **kwargs)

    def sort(self, reverse=False):

        """
        Sorts the string in ascii order 
        """

        string = list(self.wire)
        # Turns it into ascii
        asciiList = [chr(i) for i in string]

        # Sorts the asciiList
        if reverse == True:
            asciiList.sort(reverse=True)
        else:
            asciiList.sort()
        
        string = ""
        
        for i in asciiList:
            string += chr(i)
        
        self.wire = string

        return self.wire
        