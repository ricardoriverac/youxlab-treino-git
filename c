Help on class int in module builtins:

class iinntt(object)
 |  int([x]) -> integer
 |  int(x, base=10) -> integer
 |  
 |  Convert a number or string to an integer, or return 0 if no arguments
 |  are given.  If x is a number, return x.__int__().  For floating point
 |  numbers, this truncates towards zero.
 |  
 |  If x is not a number or if base is given, then x must be a string,
 |  bytes, or bytearray instance representing an integer literal in the
 |  given base.  The literal can be preceded by '+' or '-' and be surrounded
 |  by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
 |  Base 0 means to interpret the base from the string as an integer literal.
 |  >>> int('0b100', base=0)
 |  4
 |  
 |  Built-in subclasses:
 |      bool
 |  
 |  Methods defined here:
 |  
 |  ____aabbss____(self, /)
 |      abs(self)
 |  
 |  ____aadddd____(self, value, /)
 |      Return self+value.
 |  
 |  ____aanndd____(self, value, /)
 |      Return self&value.
 |  
 |  ____bbooooll____(self, /)
 |      True if self else False
 |  
 |  ____cceeiill____(...)
 |      Ceiling of an Integral returns itself.
 |  
 |  ____ddiivvmmoodd____(self, value, /)
 |      Return divmod(self, value).
 |  
 |  ____eeqq____(self, value, /)
 |      Return self==value.
 |  
 |  ____ffllooaatt____(self, /)
 |      float(self)
 |  
 |  ____fflloooorr____(...)
 |      Flooring an Integral returns itself.
 |  
 |  ____fflloooorrddiivv____(self, value, /)
 |      Return self//value.
 |  
 |  ____ffoorrmmaatt____(self, format_spec, /)
 |      Default object formatter.
 |  
 |  ____ggee____(self, value, /)
 |      Return self>=value.
 |  
 |  ____ggeettaattttrriibbuuttee____(self, name, /)
 |      Return getattr(self, name).
 |  
 |  ____ggeettnneewwaarrggss____(self, /)
 |  
 |  ____ggtt____(self, value, /)
 |      Return self>value.
 |  
 |  ____hhaasshh____(self, /)
 |      Return hash(self).
 |  
 |  ____iinnddeexx____(self, /)
 |      Return self converted to an integer, if self is suitable for use as an index into a list.
 |  
 |  ____iinntt____(self, /)
 |      int(self)
 |  
 |  ____iinnvveerrtt____(self, /)
 |      ~self
 |  
 |  ____llee____(self, value, /)
 |      Return self<=value.
 |  
 |  ____llsshhiifftt____(self, value, /)
 |      Return self<<value.
 |  
 |  ____lltt____(self, value, /)
 |      Return self<value.
 |  
 |  ____mmoodd____(self, value, /)
 |      Return self%value.
 |  
 |  ____mmuull____(self, value, /)
 |      Return self*value.
 |  
 |  ____nnee____(self, value, /)
 |      Return self!=value.
 |  
 |  ____nneegg____(self, /)
 |      -self
 |  
 |  ____oorr____(self, value, /)
 |      Return self|value.
 |  
 |  ____ppooss____(self, /)
 |      +self
 |  
 |  ____ppooww____(self, value, mod=None, /)
 |      Return pow(self, value, mod).
 |  
 |  ____rraadddd____(self, value, /)
 |      Return value+self.
 |  
 |  ____rraanndd____(self, value, /)
 |      Return value&self.
 |  
 |  ____rrddiivvmmoodd____(self, value, /)
 |      Return divmod(value, self).
 |  
 |  ____rreepprr____(self, /)
 |      Return repr(self).
 |  
 |  ____rrfflloooorrddiivv____(self, value, /)
 |      Return value//self.
 |  
 |  ____rrllsshhiifftt____(self, value, /)
 |      Return value<<self.
 |  
 |  ____rrmmoodd____(self, value, /)
 |      Return value%self.
 |  
 |  ____rrmmuull____(self, value, /)
 |      Return value*self.
 |  
 |  ____rroorr____(self, value, /)
 |      Return value|self.
 |  
 |  ____rroouunndd____(...)
 |      Rounding an Integral returns itself.
 |      
 |      Rounding with an ndigits argument also returns an integer.
 |  
 |  ____rrppooww____(self, value, mod=None, /)
 |      Return pow(value, self, mod).
 |  
 |  ____rrrrsshhiifftt____(self, value, /)
 |      Return value>>self.
 |  
 |  ____rrsshhiifftt____(self, value, /)
 |      Return self>>value.
 |  
 |  ____rrssuubb____(self, value, /)
 |      Return value-self.
 |  
 |  ____rrttrruueeddiivv____(self, value, /)
 |      Return value/self.
 |  
 |  ____rrxxoorr____(self, value, /)
 |      Return value^self.
 |  
 |  ____ssiizzeeooff____(self, /)
 |      Returns size in memory, in bytes.
 |  
 |  ____ssuubb____(self, value, /)
 |      Return self-value.
 |  
 |  ____ttrruueeddiivv____(self, value, /)
 |      Return self/value.
 |  
 |  ____ttrruunncc____(...)
 |      Truncating an Integral returns itself.
 |  
 |  ____xxoorr____(self, value, /)
 |      Return self^value.
 |  
 |  aass__iinntteeggeerr__rraattiioo(self, /)
 |      Return integer ratio.
 |      
 |      Return a pair of integers, whose ratio is exactly equal to the original int
 |      and with a positive denominator.
 |      
 |      >>> (10).as_integer_ratio()
 |      (10, 1)
 |      >>> (-10).as_integer_ratio()
 |      (-10, 1)
 |      >>> (0).as_integer_ratio()
 |      (0, 1)
 |  
 |  bbiitt__ccoouunntt(self, /)
 |      Number of ones in the binary representation of the absolute value of self.
 |      
 |      Also known as the population count.
 |      
 |      >>> bin(13)
 |      '0b1101'
 |      >>> (13).bit_count()
 |      3
 |  
 |  bbiitt__lleennggtthh(self, /)
 |      Number of bits necessary to represent self in binary.
 |      
 |      >>> bin(37)
 |      '0b100101'
 |      >>> (37).bit_length()
 |      6
 |  
 |  ccoonnjjuuggaattee(...)
 |      Returns self, the complex conjugate of any int.
 |  
 |  ttoo__bbyytteess(self, /, length, byteorder, *, signed=False)
 |      Return an array of bytes representing an integer.
 |      
 |      length
 |        Length of bytes object to use.  An OverflowError is raised if the
 |        integer is not representable with the given number of bytes.
 |      byteorder
 |        The byte order used to represent the integer.  If byteorder is 'big',
 |        the most significant byte is at the beginning of the byte array.  If
 |        byteorder is 'little', the most significant byte is at the end of the
 |        byte array.  To request the native byte order of the host system, use
 |        `sys.byteorder' as the byte order value.
 |      signed
 |        Determines whether two's complement is used to represent the integer.
 |        If signed is False and a negative integer is given, an OverflowError
 |        is raised.
 |  
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |  
 |  ffrroomm__bbyytteess(bytes, byteorder, *, signed=False) from builtins.type
 |      Return the integer represented by the given array of bytes.
 |      
 |      bytes
 |        Holds the array of bytes to convert.  The argument must either
 |        support the buffer protocol or be an iterable object producing bytes.
 |        Bytes and bytearray are examples of built-in objects that support the
 |        buffer protocol.
 |      byteorder
 |        The byte order used to represent the integer.  If byteorder is 'big',
 |        the most significant byte is at the beginning of the byte array.  If
 |        byteorder is 'little', the most significant byte is at the end of the
 |        byte array.  To request the native byte order of the host system, use
 |        `sys.byteorder' as the byte order value.
 |      signed
 |        Indicates whether two's complement is used to represent the integer.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  ____nneeww____(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  ddeennoommiinnaattoorr
 |      the denominator of a r