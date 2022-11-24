# Bytes Object
print(bytes(4)) # when printed out, bytes are recognized by the letter 'b' at the beginning.

# each byte is represented by a back slash and letter 'x' followed by two zeros [\b00] #hexadecimal (16 base)

# Emojis are encoded with utf-8; which is a type of Unicode Transformation Format.

smileyBytes = bytes('😀', 'utf-8') # not sure if the 'utf-8' string thing is important.
print(smileyBytes) # prints the emoji encoded.
print(smileyBytes.decode('utf-8')) # prints out the emoji itself, not the code that represents it.

# Bytes are similar to tuples when it comes to editing. So, if we need to edit them, we need to use
# something called bytearray

byteArray = bytearray('😀', 'utf-8') #bytearray is a class used in Python.
print(byteArray)
print(byteArray[3]) #128

# So, if we want to edit these bytarrays we need to deal with them as a list [each byte represents a character]

byteArray[3] = int('84', 16) # this changes the byte no. 2 in the index order to the new one
# making that smileyface of byteArray something different.

byteArray[0] = int('f0', 16)

print(byteArray.decode('utf-8'))

byteArray[1] = int('9f', 16)
byteArray[2] = int('99', 16)


print(byteArray.decode('utf-8'))


