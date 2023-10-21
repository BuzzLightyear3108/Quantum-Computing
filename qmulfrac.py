from qmul import *

# Circuit 1 (Numerator Circuit)

# Set the Inputs by using setInputs()
A, B = -7, -6
setInputs(A, B)

# Execute the Circuit by using execCirc()
execCirc()

# Draw the Circuit
mCirc.draw(output='mpl')


# Circuit 2 (Denominator Circuit)

# Set the Inputs by using setInputs()
A, B = -4, -5
setInputs(A, B)

# Execute the Circuit by using execCirc()
execCirc()

# Draw the Circuit
mCirc.draw(output='mpl')
