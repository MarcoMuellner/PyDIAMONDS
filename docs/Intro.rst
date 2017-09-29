Introduction
============

About DIAMONDS
--------------

DIAMONDS was created in 2014 by `Enrico Corsaro <http://www.astrofit2.inaf.it/astrofit2-fellows/enrico-corsaro/>`_ and
`Joris de Ridder <https://fys.kuleuven.be/ster/staff/senior-staff/joris>`_.

The DIAMONDS (high-DImensional And multi-MOdal NesteD Sampling) code performs a Bayesian parameter estimation and model
comparison by means of the nested sampling Monte Carlo (NSMC) algorithm. The code was designed to be generally
applicable to a large variety of problems. Diamonds is developed in C++11 and is structured in classes for flexibility
and configurability. Any new model, likelihood and prior probability density functions can be defined and implemented,
deriving from an abstract class.

About PyDIAMONDS
----------------

In 2017 it was necessary to create python bindings on the DIAMONDS code, which this project is about. The goal of
PyDIAMONDS is to provide a pythonic interface to most if not all Classes provided by DIAMONDS using pybind11. This
allows the exploitation of the flexibility of python, as well as its myriad of scientific tools in combination with the
speed and reliability of the DIAMONDS code.

About this Documentation
------------------------

The aim of this documentation is to provide an entry point on how to use PyDIAMONDS (obviously). This documentation will
not show the concepts of bayesian methods and the nested sampling algorithm, for this have a look at the myriad of
papers on the topics. A good starting point on bayesian methods is the excellent paper by
`Trotta (2008) <http://cdsads.u-strasbg.fr/abs/2008ConPh..49...71T>`_ as well as references therein. To get a deeper
understanding of the Nested sampling algorithm see the paper by
`Skilling (2006) <https://projecteuclid.org/euclid.ba/1340370944>`_. A more specialized documentation on DIAMONDS is
also available in the docs folder of DIAMONDS.