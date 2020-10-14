# Documentation

A list of all the functions unique to wire
______________________________________

## Note:

- Wire and string are used interchangeably
- This assumes you have Wire installed, run `pip install wire` to install wire

`Wire.__getitem__()`

Usage:

```py
>>> wire = Wire("Hi")
>>> wire[0]
H
>>> wire["H"]
0
```

`Wire.__repr__()`


Usage:

```py
>>> wire = Wire("Hello world")
>>> wire # The output is not to be confused with string "Hello world"
Hello world
```

`Wire.__setitem__()`

Usage:

```py
>>> wire = Wire("Hello world")
>>> wire[0] = "J"
>>> wire
Jello world
>>> wire["H"] = 4
>>> wire
olleJ world
```

### Note:

`wire[string] = newIndex` is correct. It takes the index of the Wire and swaps it with the newIndex so a character at that index gets swapped with the one at the newIndex

`Wire.__sub__()`

Usage:

```py
>>> wire = Wire("Hello world Hello universe")
>>> wire - "H"
ello world Hello universe
```

`Wire.__truediv__()`

Usage:

```py
>>> wire = Wire("Hello world")
>>> wire / "l"
Heo word
```

`Wire.forEach(action, *args, **kwargs)`

Usage:

```py
>>> wire = Wire("hello world")
>>> wire.forEach(print)
h
e
l
l
o
w
o
r
l
d
```

### Note;

`Wire.forEach` is the equivalent of:

```py
for i in wire:
    action(i, *args, **kwargs)
```

`Wire.format(*args, **kwargs)`

See the [string.format](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str) in python docs

`Wire.getDiff(otherString)`

Usage:
```py
>>> wire = Wire("Hello world")
>>> wire.getDiff("HELLO")
11
```

### Note:

The difference is calculated by the difference of string1 and string2 `abs(string1-string2)` for each unmatched case the difference gets added to by one. For each unmatched character, the difference gets added to be one.

`Wire.removeDuplicate(inOrder=True, caseSensitive=True)`

Usage:

```py
>>> wire = Wire("Hello world")
>>> wire.removeDuplicate()
Hel wrd
```

`Wire.replace(oldString, newString, count=None)`

Usage:

```py
>>> wire = Wire("Hello world")
>>> wire.replace("Hello", "Goodbye")
```

### Note:

`count=None` means that all the instances of that letter will be replaced. It can be replaced by how many instances of the substring (string in string) you want to replace.

`Wire.sort(reverse=False)`

Usage:

```py
>>> wire = Wire("Hello world")
>>> wire.sort()
Hdellloorw
```

### Note:

It sorts the Wire in ASCII order.

`Wire.swap(indexOne, indexTwo)`

Usage:
```py
>>> wire = Wire("Hello world")
>>> wire.swap(0, 10)
dello worlH
```
