from FullSubtractor import *

X = 5
Y = 2

XBinary1 = bin(X)[2:]
YBinary1 = bin(Y)[2:]

# Find Longest NBit by sorting out the temporary array of the lengths of X and Y in binary numbers.
longestNBit = sorted([len(XBinary1), len(YBinary1)])[-1]

XBinary2 = afmtsd(XBinary1, '0', longestNBit)
YBinary2 = afmtsd(YBinary1, '0', longestNBit)

# Since we are doing subtraction using algorithm that goes from the back of the number, reverse the Binary numbers
XBinary3, YBinary3 = XBinary2[::-1], YBinary2[::-1]

# Create a placeholder for the Result (in Python, Binary numbers starts with "0b")
result = '0b'

# Create a placeholder for Borrow-In named BIn as opposed to BOut (Borrow-Out)
# (not to be confused with "Bin" as in "Binary")
BIn = 0

for xDigit, yDigit in zip(XBinary3, YBinary3):
    setInputs(int(xDigit), int(yDigit), BIn)
    counts = execCirc()
    
    D, BOut = list(list(counts)[0][::-1])
    
    BIn = int(BOut)
    result += D
    
print(result)