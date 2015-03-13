Symbolic Regression
===================

Here is a simple solution of a probem given by my university. The problem is
very simple: we have a dataset (datfile.dat) with values of a function. The
goal is to find the coefficients (a, b, c, d, e, f) of this polynomial function:
```
f(x) = a + b.x + c.x^2 + d.x^3 + e.x^4 + f.x^5
```

How can I tune the algorithm?
==============================

I'm too lazy to use config file. You can tune the algorithm by changing the
parameters in the file "genetic.ml".

Some graphics
=============

The polynomial function's graph:
![the graph of function]
(https://github.com/BartholomewPanda/GeneticPlayground/raw/master/symbolic_regression/img/f.jpg)

The graph of fitness (log scale):
![the graph of fitness]
(https://github.com/BartholomewPanda/GeneticPlayground/raw/master/symbolic_regression/img/fitness.jpg)

The best solution (error of 0.000421):
![the best solution]
(https://github.com/BartholomewPanda/GeneticPlayground/raw/master/symbolic_regression/img/best.jpg)

How to compile and run?
=======================

To compile:
```
ocamlbuild -use-ocamlfind -pkgs str genetic.native
```

To run:
```
./genetic.native
```
