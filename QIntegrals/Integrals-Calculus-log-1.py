Python 3.11.4 | packaged by Anaconda, Inc. | (main, Jul  5 2023, 13:38:37) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

= RESTART: C:\Users\mulia\Documents\Others\Sci and Tech\Computers and Robots\MyPython\Python Project Files\Making a Calculator\Integrals-Calculus.py
Expression: 3*1 = 3
Expression: 10*2 = 20
Traceback (most recent call last):
  File "C:\Users\mulia\Documents\Others\Sci and Tech\Computers and Robots\MyPython\Python Project Files\Making a Calculator\Integrals-Calculus.py", line 55, in <module>
    setInputs(A, B)
  File "C:\Users\mulia\Documents\Others\Sci and Tech\Computers and Robots\MyPython\Python Project Files\Making a Calculator\qmul.py", line 77, in setInputs
    mCirc.data[AIndex+1].operation.name = gateName
  File "C:\ProgramData\Anaconda3\Lib\site-packages\qiskit\circuit\quantumcircuitdata.py", line 152, in __getitem__
    return self._circuit._data[i]
IndexError: list index out of range
A
181428571428571
B
1

factors
array([[181428571428571,               1],
       [100000000000000,               2]], dtype=int64)

G_Slopes_RawEq
1.81428571428571*x

coeffExp
(1.81428571428571, 1)


= RESTART: C:\Users\mulia\Documents\Others\Sci and Tech\Computers and Robots\MyPython\Python Project Files\Making a Calculator\Integrals-Calculus.py
Expression: 3*1 = 3
Expression: 10*2 = 20
Expression: 907143*1 = -903
Expression: 500000*2 = 576
Expression: 409091*1 = -515
Expression: 500000*2 = 576
Expression: 0*1 = 0
Expression: 1*1 = 1
Expression: 0*1 = 0
Expression: 1*1 = 1
Traceback (most recent call last):
  File "C:\Users\mulia\Documents\Others\Sci and Tech\Computers and Robots\MyPython\Python Project Files\Making a Calculator\Integrals-Calculus.py", line 59, in <module>
    resultMul = execCirc()
  File "C:\Users\mulia\Documents\Others\Sci and Tech\Computers and Robots\MyPython\Python Project Files\Making a Calculator\qmul.py", line 109, in execCirc
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
  File "C:\ProgramData\Anaconda3\Lib\site-packages\qiskit\converters\circuit_to_dag.py", line 83, in circuit_to_dag
    dagcircuit.add_qreg(register)
  File "C:\ProgramData\Anaconda3\Lib\site-packages\qiskit\dagcircuit\dagcircuit.py", line 266, in add_qreg
    existing_qubits = set(self.qubits)
  File "C:\ProgramData\Anaconda3\Lib\site-packages\qiskit\circuit\bit.py", line 113, in __hash__
    def __hash__(self):
KeyboardInterrupt

G_Slopes_BeforeInt
[0.3*x, 1.81428571428571*x, 0.818181818181818*x, 0, 0, 0, -0.727272727272727*x, -2.01428571428571*x, 3*x**2/20, -301*x**2/192, -515*x**2/576, 0, 0]


= RESTART: C:\Users\mulia\Documents\Others\Sci and Tech\Computers and Robots\MyPython\Python Project Files\Making a Calculator\Integrals-Calculus.py
Expression: 3*1 = 3
Expression: 10*2 = 20
Expression: 907143*1 = -903
Expression: 500000*2 = 576
Traceback (most recent call last):
  File "C:\Users\mulia\Documents\Others\Sci and Tech\Computers and Robots\MyPython\Python Project Files\Making a Calculator\Integrals-Calculus.py", line 59, in <module>
    resultMul = execCirc()
  File "C:\Users\mulia\Documents\Others\Sci and Tech\Computers and Robots\MyPython\Python Project Files\Making a Calculator\qmul.py", line 109, in execCirc
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
  File "C:\ProgramData\Anaconda3\Lib\site-packages\qiskit\transpiler\passes\basis\unroll_custom_definitions.py", line 100, in run
    decomposition = circuit_to_dag(unrolled)
  File "C:\ProgramData\Anaconda3\Lib\site-packages\qiskit\converters\circuit_to_dag.py", line 91, in circuit_to_dag
    op = copy.deepcopy(op)
  File "C:\ProgramData\Anaconda3\Lib\copy.py", line 137, in deepcopy
    d = id(x)
KeyboardInterrupt
factors
array([[409091,      1],
       [500000,      2]])

factors.dtype
dtype('int32')

coeffExp1
(0.818181818181818, 1)

coeffExp2
[0.818182, 1]

G_Slopes_BeforeInt
[0.3*x, 1.81428571428571*x, 0.818181818181818*x, 0, 0, 0, -0.727272727272727*x, -2.01428571428571*x, 3*x**2/20, -301*x**2/192]


= RESTART: C:\Users\mulia\Documents\Others\Sci and Tech\Computers and Robots\MyPython\Python Project Files\Making a Calculator\Integrals-Calculus.py
Traceback (most recent call last):
  File "C:\Users\mulia\Documents\Others\Sci and Tech\Computers and Robots\MyPython\Python Project Files\Making a Calculator\Integrals-Calculus.py", line 59, in <module>
    resultMul = execCirc()
  File "C:\Users\mulia\Documents\Others\Sci and Tech\Computers and Robots\MyPython\Python Project Files\Making a Calculator\qmul.py", line 109, in execCirc
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
  File "C:\ProgramData\Anaconda3\Lib\site-packages\qiskit\converters\circuit_to_dag.py", line 91, in circuit_to_dag
    op = copy.deepcopy(op)
  File "C:\ProgramData\Anaconda3\Lib\copy.py", line 153, in deepcopy
    y = copier(memo)
  File "C:\ProgramData\Anaconda3\Lib\site-packages\qiskit\circuit\controlledgate.py", line 241, in __deepcopy__
    cpy.base_gate = self.base_gate.copy()
  File "C:\ProgramData\Anaconda3\Lib\site-packages\qiskit\circuit\instruction.py", line 426, in copy
    cpy = self.__deepcopy__()
  File "C:\ProgramData\Anaconda3\Lib\site-packages\qiskit\circuit\instruction.py", line 433, in __deepcopy__
    cpy = copy.copy(self)
  File "C:\ProgramData\Anaconda3\Lib\copy.py", line 102, in copy
    return _reconstruct(x, None, *rv)
KeyboardInterrupt


= RESTART: C:\Users\mulia\Documents\Others\Sci and Tech\Computers and Robots\MyPython\Python Project Files\Making a Calculator\Integrals-Calculus.py
Traceback (most recent call last):
  File "C:\Users\mulia\Documents\Others\Sci and Tech\Computers and Robots\MyPython\Python Project Files\Making a Calculator\Integrals-Calculus.py", line 72, in <module>
    # Rule: ∫(f(x) + g(x))dx = ∫f(x)dx + ∫g(x)dx
  File "C:\Users\mulia\Documents\Others\Sci and Tech\Computers and Robots\MyPython\Python Project Files\Making a Calculator\Integrals-Calculus.py", line 72, in <listcomp>
    # Rule: ∫(f(x) + g(x))dx = ∫f(x)dx + ∫g(x)dx
TypeError: can only concatenate list (not "Mul") to list

= RESTART: C:\Users\mulia\Documents\Others\Sci and Tech\Computers and Robots\MyPython\Python Project Files\Making a Calculator\Integrals-Calculus.py
Traceback (most recent call last):
  File "C:\Users\mulia\Documents\Others\Sci and Tech\Computers and Robots\MyPython\Python Project Files\Making a Calculator\Integrals-Calculus.py", line 73, in <module>
    G_Integrated = [G_b_AfterInt+G_y_intercept_Part for G_Slopes_Part, G_y_intercept_Part in zip(G_Slopes_AfterInt, G_b_AfterInt)]
  File "C:\Users\mulia\Documents\Others\Sci and Tech\Computers and Robots\MyPython\Python Project Files\Making a Calculator\Integrals-Calculus.py", line 73, in <listcomp>
    G_Integrated = [G_b_AfterInt+G_y_intercept_Part for G_Slopes_Part, G_y_intercept_Part in zip(G_Slopes_AfterInt, G_b_AfterInt)]
TypeError: can only concatenate list (not "Mul") to list
G_Integrated
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    G_Integrated
NameError: name 'G_Integrated' is not defined

G_Slopes_AfterInt
[3*x**2/20, -301*x**2/192, -515*x**2/576, 0, 0, 0, 233*x**2/1152, -551*x**2/576]


= RESTART: C:\Users\mulia\Documents\Others\Sci and Tech\Computers and Robots\MyPython\Python Project Files\Making a Calculator\Integrals-Calculus.py
G_Integrated
[3*x**2/20 + 0.08*x, -301*x**2/192 - 0.677142857142857*x, -515*x**2/576 + 0.518181818181818*x, 2.4*x, 2.4*x, 2.4*x, 233*x**2/1152 + 7.27272727272727*x, -551*x**2/576 + 17.3114285714286*x]


G_Slopes_BeforeInt
[0.3*x, 1.81428571428571*x, 0.818181818181818*x, 0, 0, 0, -0.727272727272727*x, -2.01428571428571*x]

G_Slopes_AfterInt
[3*x**2/20, -301*x**2/192, -515*x**2/576, 0, 0, 0, 233*x**2/1152, -551*x**2/576]

G_eqns
[0.3*x + 0.08, 1.81428571428571*x - 0.677142857142857, 0.818181818181818*x + 0.518181818181818, 2.40000000000000, 2.40000000000000, 2.40000000000000, 7.27272727272727 - 0.727272727272727*x, 17.3114285714286 - 2.01428571428571*x]

G_Integrated
[3*x**2/20 + 0.08*x, -301*x**2/192 - 0.677142857142857*x, -515*x**2/576 + 0.518181818181818*x, 2.4*x, 2.4*x, 2.4*x, 233*x**2/1152 + 7.27272727272727*x, -551*x**2/576 + 17.3114285714286*x]

G_eqns = [Fraction(str(m)).as_integer_ratio()*x+b for m, b in zip(G_Slopes, G_y_intercept)]
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    G_eqns = [Fraction(str(m)).as_integer_ratio()*x+b for m, b in zip(G_Slopes, G_y_intercept)]
  File "<pyshell#32>", line 1, in <listcomp>
    G_eqns = [Fraction(str(m)).as_integer_ratio()*x+b for m, b in zip(G_Slopes, G_y_intercept)]
TypeError: can't multiply sequence by non-int of type 'Symbol'

G_eqns = [Fraction(str(m))*x+b for m, b in zip(G_Slopes, G_y_intercept)]
G_eqns
[7500000000000001*x/25000000000000000 + 0.08, 3628571428571429*x/2000000000000000 - 0.677142857142857, 4090909090909091*x/5000000000000000 + 0.518181818181818, 2.40000000000000, 2.40000000000000, 2.40000000000000, 7.27272727272727 - 7272727272727273*x/10000000000000000, 17.3114285714286 - 1007142857142857*x/500000000000000]

G_eqns = [Fraction(str(m)).limit_denominator()*x+b for m, b in zip(G_Slopes, G_y_intercept)]
G_eqns
[3*x/10 + 0.08, 127*x/70 - 0.677142857142857, 9*x/11 + 0.518181818181818, 2.40000000000000, 2.40000000000000, 2.40000000000000, 7.27272727272727 - 8*x/11, 17.3114285714286 - 141*x/70]

G_Integrated
[3*x**2/20 + 0.08*x, -301*x**2/192 - 0.677142857142857*x, -515*x**2/576 + 0.518181818181818*x, 2.4*x, 2.4*x, 2.4*x, 233*x**2/1152 + 7.27272727272727*x, -551*x**2/576 + 17.3114285714286*x]

127/70
1.8142857142857143

-301/192
-1.5677083333333333


= RESTART: C:\Users\mulia\Documents\Others\Sci and Tech\Computers and Robots\MyPython\Python Project Files\Making a Calculator\Integrals-Calculus.py
G_eqns
[7500000000000001*x/25000000000000000 + 0.08, 3628571428571429*x/2000000000000000 - 0.677142857142857, 4090909090909091*x/5000000000000000 + 0.518181818181818, 2.40000000000000, 2.40000000000000, 2.40000000000000, 7.27272727272727 - 7272727272727273*x/10000000000000000, 17.3114285714286 - 1007142857142857*x/500000000000000]

G_Integrated
[3*x**2/20 + 0.08*x, -301*x**2/192 - 0.677142857142857*x, -515*x**2/576 + 0.518181818181818*x, 2.4*x, 2.4*x, 2.4*x, 233*x**2/1152 + 7.27272727272727*x, -551*x**2/576 + 17.3114285714286*x]

G_eq_BeforeInt = [Fraction(str(m)).limit_denominator()*x+b for m, b in zip(G_Slopes, G_y_intercept)]

G_eq_BeforeInt
[3*x/10 + 0.08, 127*x/70 - 0.677142857142857, 9*x/11 + 0.518181818181818, 2.40000000000000, 2.40000000000000, 2.40000000000000, 7.27272727272727 - 8*x/11, 17.3114285714286 - 141*x/70]

factorsSet
[array([[ 3,  1],
       [10,  2]]), array([[907143,      1],
       [500000,      2]]), array([[409091,      1],
       [500000,      2]]), array([[0, 1],
       [1, 1]]), array([[0, 1],
       [1, 1]]), array([[0, 1],
       [1, 1]]), array([[-727273,       1],
       [1000000,       2]]), array([[-1007143,        1],
       [  500000,        2]])]

np.array(factorsSet)
array([[[       3,        1],
        [      10,        2]],

       [[  907143,        1],
        [  500000,        2]],

       [[  409091,        1],
        [  500000,        2]],

       [[       0,        1],
        [       1,        1]],

       [[       0,        1],
        [       1,        1]],

       [[       0,        1],
        [       1,        1]],

       [[ -727273,        1],
        [ 1000000,        2]],

       [[-1007143,        1],
        [  500000,        2]]])

coeffExpFrac
[(-1007143, 500000), (1, 1)]

coeffExpFrac
[(-1007143, 500000), (1, 1)]

G_eq_BeforeInt
[3*x/10 + 0.08, 127*x/70 - 0.677142857142857, 9*x/11 + 0.518181818181818, 2.40000000000000, 2.40000000000000, 2.40000000000000, 7.27272727272727 - 8*x/11, 17.3114285714286 - 141*x/70]

G_Inte
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    G_Inte
NameError: name 'G_Inte' is not defined

G_Integrated
[3*x**2/20 + 0.08*x, -301*x**2/192 - 0.677142857142857*x, -515*x**2/576 + 0.518181818181818*x, 2.4*x, 2.4*x, 2.4*x, 233*x**2/1152 + 7.27272727272727*x, -551*x**2/576 + 17.3114285714286*x]


G_eq_BeforeInt
[3*x/10 + 0.08, 127*x/70 - 0.677142857142857, 9*x/11 + 0.518181818181818, 2.40000000000000, 2.40000000000000, 2.40000000000000, 7.27272727272727 - 8*x/11, 17.3114285714286 - 141*x/70]

G_Integrated
[3*x**2/20 + 0.08*x, -301*x**2/192 - 0.677142857142857*x, -515*x**2/576 + 0.518181818181818*x, 2.4*x, 2.4*x, 2.4*x, 233*x**2/1152 + 7.27272727272727*x, -551*x**2/576 + 17.3114285714286*x]

G_Slopes_BeforeInt
[0.3*x, 1.81428571428571*x, 0.818181818181818*x, 0, 0, 0, -0.727272727272727*x, -2.01428571428571*x]


= RESTART: C:\Users\mulia\Documents\Others\Sci and Tech\Computers and Robots\MyPython\Python Project Files\Making a Calculator\Integrals-Calculus.py

G_eq_BeforeInt
[3*x/10 + 0.08, 127*x/70 - 0.677142857142857, 9*x/11 + 0.518181818181818, 2.40000000000000, 2.40000000000000, 2.40000000000000, 7.27272727272727 - 8*x/11, 17.3114285714286 - 141*x/70]

G_Integrated
[3*x**2/20 + 0.08*x, -301*x**2/192 - 0.677142857142857*x, -515*x**2/576 + 0.518181818181818*x, 2.4*x, 2.4*x, 2.4*x, 233*x**2/1152 + 7.27272727272727*x, -551*x**2/576 + 17.3114285714286*x]

np.array(factorsSet)
array([[[       3,        1],
        [      10,        2]],

       [[  907143,        1],
        [  500000,        2]],

       [[  409091,        1],
        [  500000,        2]],

       [[       0,        1],
        [       1,        1]],

       [[       0,        1],
        [       1,        1]],

       [[       0,        1],
        [       1,        1]],

       [[ -727273,        1],
        [ 1000000,        2]],

       [[-1007143,        1],
        [  500000,        2]]])

coeffExpFrac
[(-1007143, 500000), (1, 1)]

G_Slopes_BeforeInt
[3*x/10, 127*x/70, 9*x/11, 0, 0, 0, -8*x/11, -141*x/70]

G_Slopes_BeforeInt[1]
127*x/70

G_Slopes_BeforeInt[1].as_coeff_exponent(x)
(127/70, 1)

[round(coeffExp1Num, 6) for coeffExp1Num in coeffExp1]
[-2.014286, 1]

127/70
1.8142857142857143

coeffExp1
(-141/70, 1)

[round(coeffExp1Num, 6) for coeffExp1Num in G_Slopes_RawEq.as_coeff_exponent(x)]
[-2.014286, 1]

[round(coeffExp1Num, 6) for coeffExp1Num in G_Slopes_BeforeInt[1].as_coeff_exponent(x)]
[1.814286, 1]

round(Fraction(127,70), 6)
Fraction(907143, 500000)


= RESTART: C:\Users\mulia\Documents\Others\Sci and Tech\Computers and Robots\MyPython\Python Project Files\Making a Calculator\Integrals-Calculus.py
G_eq_BeforeInt
[3*x/10 + 0.08, 127*x/70 - 0.677142857142857, 9*x/11 + 0.518181818181818, 2.40000000000000, 2.40000000000000, 2.40000000000000, 7.27272727272727 - 8*x/11, 17.3114285714286 - 141*x/70]

G_Integrated
[3*x**2/20 + 0.08*x, 127*x**2/140 - 0.677142857142857*x, 9*x**2/22 + 0.518181818181818*x, 2.4*x, 2.4*x, 2.4*x, 4*x**2/11 + 7.27272727272727*x, 141*x**2/140 + 17.3114285714286*x]

G_Int_Func = [lambdify(x, G_Integrated) for G_Integrated in G_Integrated_eqns]
KeyboardInterrupt

G_Integrated_eqns = G_Integrated
G_Int_Func = [lambdify(x, G_Integrated) for G_Integrated in G_Integrated_eqns]
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    G_Int_Func = [lambdify(x, G_Integrated) for G_Integrated in G_Integrated_eqns]
  File "<pyshell#97>", line 1, in <listcomp>
    G_Int_Func = [lambdify(x, G_Integrated) for G_Integrated in G_Integrated_eqns]
NameError: name 'lambdify' is not defined

G_Int_Func = [sympy.lambdify(x, G_Integrated) for G_Integrated in G_Integrated_eqns]

G_Int_Func
[<function _lambdifygenerated at 0x00000203B1BE84A0>, <function _lambdifygenerated at 0x00000203B0EC6AC0>, <function _lambdifygenerated at 0x00000203B0EC7060>, <function _lambdifygenerated at 0x00000203B0EC72E0>, <function _lambdifygenerated at 0x00000203B0EC7240>, <function _lambdifygenerated at 0x00000203B1BE94E0>, <function _lambdifygenerated at 0x00000203B0EC6E80>, <function _lambdifygenerated at 0x00000203B0EC68E0>]


G_Integrated_eqns
[3*x**2/20 + 0.08*x, 127*x**2/140 - 0.677142857142857*x, 9*x**2/22 + 0.518181818181818*x, 2.4*x, 2.4*x, 2.4*x, 4*x**2/11 + 7.27272727272727*x, 141*x**2/140 + 17.3114285714286*x]


[T_Interval for T_Interval in T_Intervals]
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    [T_Interval for T_Interval in T_Intervals]
NameError: name 'T_Intervals' is not defined

T_Intervals = [(T1,T2) for T2, T1 in zip(T[1:], T[:-1])]

[T_Interval for T_Interval in T_Intervals]
[(0, 0.5), (0.5, 1.2), (1.2, 2.3), (2.3, 3.7), (3.7, 5.3), (5.3, 6.7), (6.7, 7.8), (7.8, 8.5)]

[T_Interval[1]-T_Interval[0] for T_Interval in T_Intervals]
[0.5, 0.7, 1.0999999999999999, 1.4000000000000004, 1.5999999999999996, 1.4000000000000004, 1.0999999999999996, 0.7000000000000002]

[T_Interval[1]- for T_Interval, G_Int_Func in zip(T_Intervals, G_Int_Funcs)]
SyntaxError: invalid syntax

[G_Int_Func(T_Interval[1])-G_Int_Func(T_Interval[0]) for T_Interval, G_Int_Func in zip(T_Intervals, G_Int_Funcs)]
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    [G_Int_Func(T_Interval[1])-G_Int_Func(T_Interval[0]) for T_Interval, G_Int_Func in zip(T_Intervals, G_Int_Funcs)]
NameError: name 'G_Int_Funcs' is not defined. Did you mean: 'G_Int_Func'?

G_Int_Funcs = [sympy.lambdify(x, G_Integrated) for G_Integrated in G_Integrated_eqns]

[G_Int_Func(T_Interval[1])-G_Int_Func(T_Interval[0]) for T_Interval, G_Int_Func in zip(T_Intervals, G_Int_Funcs)]
[0.0775, 0.6055000000000001, 2.145, 3.360000000000001, 3.839999999999998, 3.3599999999999994, 13.799999999999997, 23.609500000000025]

G_Areas = [G_Int_Func(T_Interval[1])-G_Int_Func(T_Interval[0]) for T_Interval, G_Int_Func in zip(T_Intervals, G_Int_Funcs)]


G_Areas
[0.0775, 0.6055000000000001, 2.145, 3.360000000000001, 3.839999999999998, 3.3599999999999994, 13.799999999999997, 23.609500000000025]

sum(G_Areas)
50.79750000000002

RawEqParts = [49, 42*T, 9*T**2]

Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    RawEqParts = [49, 42*T, 9*T**2]
TypeError: unsupported operand type(s) for ** or pow(): 'list' and 'int'

T = sympy.Symbol('T')

RawEqParts = [49, 42*T, 9*T**2]

RawEqParts[0].as_coeff_exponent(T)
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    RawEqParts[0].as_coeff_exponent(T)
AttributeError: 'int' object has no attribute 'as_coeff_exponent'

RawEqParts[1].as_coeff_exponent(T)
(42, 1)

sympy.Expr(49)
Expr(49)

type(42*T)
<class 'sympy.core.mul.Mul'>

sympy.Mul(49)
49
>>> 
>>> RawEqParts = [sympy.Mul(49), 42*T, 9*T**2]
>>> 
>>> RawEqParts[1].as_coeff_exponent(T)
(42, 1)

>>> RawEqParts[0].as_coeff_exponent(T)
(49, 0)
>>> 
>>> 
= RESTART: C:\Users\mulia\Documents\Others\Sci and Tech\Computers and Robots\MyPython\Python Project Files\Making a Calculator\Integrals-Calculus.py
>>> Eqn_Integrated
[49*T, 21*T**2, 3*T**3]
>>> 
>>> 
= RESTART: C:\Users\mulia\Documents\Others\Sci and Tech\Computers and Robots\MyPython\Python Project Files\Making a Calculator\Integrals-Calculus.py
Simulation failed and returned the following error message:
ERROR:  [Experiment 0] Insufficient memory to run circuit circuit-122 using the statevector simulator. Required memory: 67108864M, max memory: 16169M
Traceback (most recent call last):
  File "C:\Users\mulia\Documents\Others\Sci and Tech\Computers and Robots\MyPython\Python Project Files\Making a Calculator\Integrals-Calculus.py", line 37, in <module>
    resultMul = execCirc(backend=Aer.get_backend('qasm_simulator'))
  File "C:\Users\mulia\Documents\Others\Sci and Tech\Computers and Robots\MyPython\Python Project Files\Making a Calculator\qmul.py", line 111, in execCirc
    counts = result.get_counts()
  File "C:\ProgramData\Anaconda3\Lib\site-packages\qiskit\result\result.py", line 269, in get_counts
    exp = self._get_experiment(key)
  File "C:\ProgramData\Anaconda3\Lib\site-packages\qiskit\result\result.py", line 397, in _get_experiment
    raise QiskitError(result_status, ", ", exp_status)
qiskit.exceptions.QiskitError: 'ERROR:  [Experiment 0] Insufficient memory to run circuit circuit-122 using the statevector simulator. Required memory: 67108864M, max memory: 16169M ,  ERROR: Insufficient memory to run circuit circuit-122 using the statevector simulator. Required memory: 67108864M, max memory: 16169M'
