Description
===========

Here is a simple proof of concept of a genetic algorithm application to the Vigenère cryptanalysis.
This one is able to find the key of a cryptogram.

How to use
==========

```
python ./genetic.py key_size path nb_turn
```

- key_size is the size of the key
- path is the path to the file that contains the cryptogram
- nb_turn is the number of iteration for the genetic algorithm

Some examples are available in the 'enc' directory. Example:

```
python ./genetic.py 12 enc/gamma.enc 35
```

Example
=======

![a simple example on env/gamma.env]
(https://raw.githubusercontent.com/BartholomewPanda/GeneticPlayground/master/cryptanalysis/img/example.gif)

