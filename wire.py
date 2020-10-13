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

    def __getitem__(self, key):
        """
        Returns the index if the key is a string or Wire
        else, it returns the key itself
        """
        if type(key) == str or type(key) == Wire:
            return self.wire.index(key)
        else:
            return self.wire[key]
    
    def __setitem__(self, key, value):
        """
        If the key is a string, it finds the index of the string swaps 
        the string index with the given index, for example:

        >>> wire = Wire("Hello world")
        >>> wire["H"] = 9
        >>> wire
        dello worlH

        If the key is an integer, it replaces the value of that index 
        with another one:

        >>> wire = Wire("Hello world")
        >>> wire[0] = "J"
        >>> wire
        Jello World
        """
        if type(key) == str or type(key) == Wire:
            string = self.wire
            indexOne = string.index(key)
            indexTwo = value
            self.swap(indexOne, indexTwo)

        else:
            string = list(self.wire)
            string[key] = value
            newString = ""

            for i in string:
                newString += i
            self.wire = newString

        return self.wire

            

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
    
    """Functions that are reimplementations of string functions"""

    def replace(self, old, new, count=None):
        """
        Replaces a the character(s) in a wire with other character(s)
        >>> wire = Wire("this is cool, this is not cool")
        >>> wire.replace("this", "it", 1)
        it is cool, this is not cool
        If count == None, then it will replace instances of the character(s)
        to be replaced
        """
        if count == None:
            self.wire = self.wire.replace(old, new)
        else:
            self.wire = self.wire.replace(old, new, count)
        return self.wire
    
    def format(self, *args, **kwargs):
        """
        Does the same thing as str.format()
        >>> name = "Wire"
        >>> wire = Wire("hi {}")
        >>> wire.format(name)
        hi wire
        or more concisely ...
        >>> name = "Wire"
        >>> wire = Wire("hi {}").format(name) # with the same result
        hi wire
        """
        self.wire = self.wire.format(*args, **kwargs)
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
        >>> wire = Wire("Hello")
        >>> wire.removeDuplicate()
        >>> wire
        Helo
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
        returns the result of each action as a list
        NOTE: the letter being processed has to be the first argument 
        """
        results = []
        for letter in self.wire:
            results.append(action(letter, *args, **kwargs))
        return results

    def sort(self, reverse=False):

        """
        Sorts the string in ascii order 
        >>> wire = Wire("Hello world")
        >>> wire.sort()
        dlrow olleH
        """

        string = list(self.wire)
        # Turns it into ascii
        asciiList = [ord(i) for i in string]

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
    
    def swap(self, indexOne, indexTwo):
        """
        Swaps indexOne with indexTwo
        >>> wire = Wire("Fido")
        >>> wire.swap(0, 2)
        diFo
        """
        example = list(self.wire)
        example[indexOne], example[indexTwo] = example[indexTwo], example[indexOne]
        string = ""
        for i in example:
            string += i
        self.wire = string
        return self.wire