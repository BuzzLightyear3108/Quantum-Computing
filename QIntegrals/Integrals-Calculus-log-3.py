Python 3.11.4 | packaged by Anaconda, Inc. | (main, Jul  5 2023, 13:38:37) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

= RESTART: C:\Users\mulia\Documents\Others\Sci and Tech\Computers and Robots\MyPython\Python Project Files\MakeCalc\QIntegrals-NASA-7Page48.py
Traceback (most recent call last):
  File "C:\Users\mulia\Documents\Others\Sci and Tech\Computers and Robots\MyPython\Python Project Files\MakeCalc\QIntegrals-NASA-7Page48.py", line 13, in <module>
    RawEqParts = [coef*T**exp for coef, exp in zip('1.49 12.30 41.94 76.00 77.55 42.28 9.46 0.18 0.0009'.split(), range(8, -1, -1))]
  File "C:\Users\mulia\Documents\Others\Sci and Tech\Computers and Robots\MyPython\Python Project Files\MakeCalc\QIntegrals-NASA-7Page48.py", line 13, in <listcomp>
    RawEqParts = [coef*T**exp for coef, exp in zip('1.49 12.30 41.94 76.00 77.55 42.28 9.46 0.18 0.0009'.split(), range(8, -1, -1))]
TypeError: can't multiply sequence by non-int of type 'Pow'

2*T**3
2*T**3

type(T**3)
<class 'sympy.core.power.Pow'>

2.5*T**3
2.5*T**3

'2'*T**3
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    '2'*T**3
TypeError: can't multiply sequence by non-int of type 'Pow'


= RESTART: C:\Users\mulia\Documents\Others\Sci and Tech\Computers and Robots\MyPython\Python Project Files\MakeCalc\QIntegrals-NASA-7Page48.py
[149*T**9.0/900, 123*T**8.0/80, 7*T**7.0/50, 38*T**6.0/3, 527*T**5.0/100, 33*T**4.0/100, 473*T**3.0/150, 9*T**2.0/100, 9*T**1.0/784]
149*T**9.0/900
149*T**9.0/900


149/900
0.16555555555555557

123/80
1.5375

7/50
0.14

473/150
3.1533333333333333

coeffExp
(0.000900000000000000, 0)

coeffExpFrac
[(9, 10000), (0, 1)]

factorsSet
[array([[149,   1],
       [100,   9]]), array([[123,   1],
       [ 10,   8]]), array([[2097,    1],
       [  50,    7]]), array([[76,  1],
       [ 1,  6]]), array([[1551,    1],
       [  20,    5]]), array([[1057,    1],
       [  25,    4]]), array([[473,   1],
       [ 50,   3]]), array([[ 9,  1],
       [50,  2]]), array([[    9,     1],
       [10000,     1]])]

np.array(factorsSet)
array([[[  149,     1],
        [  100,     9]],

       [[  123,     1],
        [   10,     8]],

       [[ 2097,     1],
        [   50,     7]],

       [[   76,     1],
        [    1,     6]],

       [[ 1551,     1],
        [   20,     5]],

       [[ 1057,     1],
        [   25,     4]],

       [[  473,     1],
        [   50,     3]],

       [[    9,     1],
        [   50,     2]],

       [[    9,     1],
        [10000,     1]]])

2097/350
5.991428571428571

setInputs(1551, 265)

resultMul = execCirc()
resultMul
-139655

setInputs(6, 7)
resultMul = execCirc()

resultMul
-42


================================ RESTART: Shell ================================

= RESTART: C:\Users\mulia\Documents\Others\Sci and Tech\Computers and Robots\MyPython\Python Project Files\MakeCalc\qmul.py
setInputs(6, 7)
resultMul = execCirc()
resultMul
42

setInputs(6, -7); resultMul = execCirc(); resultMul
42

= RESTART: C:\Users\mulia\Documents\Others\Sci and Tech\Computers and Robots\MyPython\Python Project Files\MakeCalc\qmul.py
setInputs(6, -7); resultMul = execCirc(); resultMul
-42
setInputs(-6, 7); resultMul = execCirc(); resultMul
-42
setInputs(-6, -7); resultMul = execCirc(); resultMul
42

setInputs(6, 7); resultMul = execCirc(); resultMul
42

setInputs(1551, 265); resultMul = execCirc(); resultMul
-139655

1551*265
411015

1551//100
15

1551%100
51

setInputs(16, 7); resultMul = execCirc(); resultMul
112

setInputs(16, 8); resultMul = execCirc(); resultMul
128

setInputs(160, 8); resultMul = execCirc(); resultMul
1280

setInputs(1600, 8); resultMul = execCirc(); resultMul
-4608

setInputs(900, 8); resultMul = execCirc(); resultMul
7200

setInputs(1000, 8); resultMul = execCirc(); resultMul
8000

setInputs(1599, 8); resultMul = execCirc(); resultMul
-4600

setInputs(1200, 8); resultMul = execCirc(); resultMul
-1408

setInputs(1100, 8); resultMul = execCirc(); resultMul
-608
setInputs(1001, 8); resultMul = execCirc(); resultMul
8008

i
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    i
NameError: name 'i' is not defined. Did you mean: 'id'?

for i in range(1001, 1101):
    setInputs(i, 8); resultMul = execCirc(); resultMul
    if resultMul != i*8: break

    
8008
8016
8024
8032
Traceback (most recent call last):
  File "<pyshell#80>", line 2, in <module>
    setInputs(i, 8); resultMul = execCirc(); resultMul
  File "C:\Users\mulia\Documents\Others\Sci and Tech\Computers and Robots\MyPython\Python Project Files\MakeCalc\qmul.py", line 109, in execCirc
    job = execute(mCirc, backend, shots=shots)
  File "C:\ProgramData\Anaconda3\Lib\site-packages\qiskit\utils\deprecation.py", line 182, in wrapper
    return func(*args, **kwargs)
  File "C:\ProgramData\Anaconda3\Lib\site-packages\qiskit\utils\deprecation.py", line 182, in wrapper
    return func(*args, **kwargs)
  File "C:\ProgramData\Anaconda3\Lib\site-packages\qiskit\execute_function.py", line 304, in execute
    experiments = transpile(
  File "C:\ProgramData\Anaconda3\Lib\site-packages\qiskit\compiler\transpiler.py", line 418, in transpile
    out_circuits = pm.run(circuits, callback=callback)
  File "C:\ProgramData\Anaconda3\Lib\site-packages\qiskit\transpiler\passmanager.py", line 537, in run
    return super().run(circuits, output_name, callback)
  File "C:\ProgramData\Anaconda3\Lib\site-packages\qiskit\transpiler\passmanager.py", line 233, in run
    return [self._run_single_circuit(circuits[0], output_name, callback)]
  File "C:\ProgramData\Anaconda3\Lib\site-packages\qiskit\transpiler\passmanager.py", line 292, in _run_single_circuit
    result = running_passmanager.run(circuit, output_name=output_name, callback=callback)
  File "C:\ProgramData\Anaconda3\Lib\site-packages\qiskit\transpiler\runningpassmanager.py", line 125, in run
    dag = self._do_pass(pass_, dag, passset.options)
  File "C:\ProgramData\Anaconda3\Lib\site-packages\qiskit\transpiler\runningpassmanager.py", line 173, in _do_pass
    dag = self._run_this_pass(pass_, dag)
  File "C:\ProgramData\Anaconda3\Lib\site-packages\qiskit\transpiler\runningpassmanager.py", line 202, in _run_this_pass
    new_dag = pass_.run(dag)
  File "C:\ProgramData\Anaconda3\Lib\site-packages\qiskit\transpiler\passes\basis\unroll_custom_definitions.py", line 103, in run
    ).run(decomposition)
  File "C:\ProgramData\Anaconda3\Lib\site-packages\qiskit\transpiler\passes\basis\unroll_custom_definitions.py", line 103, in run
    ).run(decomposition)
  File "C:\ProgramData\Anaconda3\Lib\site-packages\qiskit\transpiler\passes\basis\unroll_custom_definitions.py", line 100, in run
    decomposition = circuit_to_dag(unrolled)
  File "C:\ProgramData\Anaconda3\Lib\site-packages\qiskit\converters\circuit_to_dag.py", line 92, in circuit_to_dag
    dagcircuit.apply_operation_back(op, instruction.qubits, instruction.clbits)
  File "C:\ProgramData\Anaconda3\Lib\site-packages\qiskit\dagcircuit\dagcircuit.py", line 669, in apply_operation_back
    node_index = self._add_op_node(op, qargs, cargs)
  File "C:\ProgramData\Anaconda3\Lib\site-packages\qiskit\dagcircuit\dagcircuit.py", line 603, in _add_op_node
    new_node = DAGOpNode(op=op, qargs=qargs, cargs=cargs)
  File "C:\ProgramData\Anaconda3\Lib\site-packages\qiskit\dagcircuit\dagnode.py", line 260, in __init__
    self.sort_key = str(self.qargs)
KeyboardInterrupt

for i in range(1001, 1101):
    setInputs(i, 8); resultMul = execCirc()
    if resultMul != i*8: break

    
i
1024

2**100
1267650600228229401496703205376

len(str(2**1000))
302

2**1000
10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376

[data[(i//lendata**d)%lendata] for d in range(digits)[::-1]]
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    [data[(i//lendata**d)%lendata] for d in range(digits)[::-1]]
NameError: name 'digits' is not defined

m
<module 'math' (built-in)>

m.log(2097, 100)
1.6607992152326718

ceil(m.log(2097, 100))
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    ceil(m.log(2097, 100))
NameError: name 'ceil' is not defined

m.ceil(m.log(2097, 100))
2

digits = m.ceil(m.log(2097, 100))
[data[(i//lendata**d)%lendata] for d in range(digits)[::-1]]
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    [data[(i//lendata**d)%lendata] for d in range(digits)[::-1]]
  File "<pyshell#101>", line 1, in <listcomp>
    [data[(i//lendata**d)%lendata] for d in range(digits)[::-1]]
NameError: name 'data' is not defined

[(i//lendata**d)%lendata for d in range(digits)[::-1]]
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    [(i//lendata**d)%lendata for d in range(digits)[::-1]]
  File "<pyshell#103>", line 1, in <listcomp>
    [(i//lendata**d)%lendata for d in range(digits)[::-1]]
NameError: name 'lendata' is not defined

lendata = 100
[(i//lendata**d)%lendata for d in range(digits)[::-1]]
[10, 24]

i
1024

i = 2097
digits = m.ceil(m.log(2097, 100))
lendata = 100
[(i//lendata**d)%lendata for d in range(digits)[::-1]]
[20, 97]

i = 3094
[(i//lendata**d)%lendata for d in range(digits)[::-1]]
[30, 94]

2097*3094
6488118

>>> AGrouped = [20, 97]
>>> BGrouped = [30, 94]
>>> 
>>> for AGNum in AGrouped:
...     for BGNum in BGrouped:
...         AGNum, BGNum
... 
...         
(20, 30)
(20, 94)
(97, 30)
(97, 94)
>>> 
>>> midTerms = []
>>> 
>>> for AGNum in AGrouped:
...     for BGNum in BGrouped:
...         if (AGNum, BGNum) != (AGrouped[0], BGrouped[0]) or (AGNum, BGNum) != (AGrouped[-1], BGrouped[-1]):
...            midTerms.append((AGNum, BGNum))
... 
...            
>>> 
>>> midTerms
[(20, 30), (20, 94), (97, 30), (97, 94)]

>>> midTerms = []
>>> for AGNum in AGrouped:
...     for BGNum in BGrouped:
...         if (AGNum, BGNum) != (AGrouped[0], BGrouped[0]) and (AGNum, BGNum) != (AGrouped[-1], BGrouped[-1]):
...            midTerms.append((AGNum, BGNum))
... 
...            
>>> midTerms
[(20, 94), (97, 30)]
>>> 
