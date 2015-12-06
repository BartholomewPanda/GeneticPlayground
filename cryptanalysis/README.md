Description
===========

Here is a simple proof of concept of a genetic algorithm application to the Vigenère cryptanalysis.
This one is able to find the key of a cryptogram.

A simple description of this POC is available on my blog: http://blog.bartholomew.fr/cryptanalysis-with-genetic-algorithms/


How to use
==========

The genetic script allows to find the key.

Usage:
```
python ./genetic.py min_key_size max_key_size path nb_turn
```

- min_key_size and may_key_size are a range (min_key_size <= key lenght <= max_key_size)
- path is the path to the file that contains the cryptogram
- nb_turn is the number of iteration for the genetic algorithm

Some examples are available in the 'enc' directory. Example:

```
#in this example, we know that the key lenght is 12
python ./genetic.py 12 12 enc/gamma.enc 35
#in this example, we suppose that the key lenght is in the range [5, 10]
python ./genetic.py 5 10 enc/droit.enc 35
```


Example
=======

Here is a simple example on the file env/gamma.env:

![a simple example on env/gamma.env]
(https://raw.githubusercontent.com/BartholomewPanda/GeneticPlayground/master/cryptanalysis/img/example.gif)

