Quick Example
=============

This example should show a quick example on how to use pyDiamonds and show some of its advantages.

Eggbox Example
--------------
This tutorial assumes that python and pip are installed as well as minimum experince with python.. If you don't have
them installed, visit `this link<https://wiki.python.org/moin/BeginnersGuide>`_ for a beginners guide, as well as
`this link<https://pip.pypa.io/en/stable/installing/>`_ for an installation guide on pip.

If you have python as well as pip, simply open the terminal of your choise and install pyDIAMONDS as well as numpy
using:

.. code-block:: ba
    user@machine:~$pip install pyDiamonds
    user@machine:~$pip install numpy

After installing pyDIAMONDS, open python

.. code-block:: bash

    user@machine:~$ python

After opening python, the first step is to import pyDIAMONDS and numpy

.. code-block:: python

    import numpy as np
    from pyDiamonds import *

Lets approach the Eggbox demo from DIAMONDS. First of all we need to create a small class that implements the
Likelihood. This class only implements the logValue method of Likelihood to provide the Likelihood.

.. code-block:: python

    class EggboxLikelihood(Likelihood):
        def __init__(self,observation,model):
            Likelihood.__init__(self,observation,model)
        def logValue(self,nestedSampleOfParameters):
            return np.power(2.0+np.cos(nestedSampleOfParameters[0]/2)*np.cos(nestedSampleOfParameters[1]/2),5)

Next we need to get the data and the model. For this case, these are dummy objects, as the likelihood is directly
computed.

.. code-block:: python

    data = np.array(([],[]))        #create Dummy data
    model = ZeroModel(data[0])      #create dummy model -> likelihood directly computed

Next we need to setup some priors. In this case we want to use uniform priors. This is very easy with python.

.. code-block:: python

    priors = np.array(([0,0],[10*np.pi,10*np.pi])).astype(float) #setup prior distribution. Array must be float!
    uniformPriors = UniformPrior(priors[0],priors[1])

Now that we have the Priors, we need to setup the likelihood function, using our EggboxLikelihood class.

.. code-block:: python

    likelihood = EggboxLikelihood(data[0],model) #setup likelihood function

We will continue with setting up the KmeansClusterer, by creating some basic parameters.

.. code-block:: python

    metric = EuclideanMetric()
    minNclusters = 6
    maxNclusters = 10
    nTrials = 10
    relTolerance = 0.01

    kmeans = KmeansClusterer(metric,minNclusters,maxNclusters,nTrials,relTolerance) #setup k-means clusterer using euclidean metric

The creation of the nested sampler is the next step. For this again, we create a couple of configuring parameters, which we will pass
to the constructor of the nested Sampler.

.. code-block:: python

    printOnScreen = True                            #print results on screen
    initialNobjects = 2000                          #Initial number of active points evolving within the nested sampling proc
    minNobjects = 2000                              #Minimum number of active points allowed in the nesting process
    maxNdrawAttempts  =50000                        #Maximum number of attempts when trying to draw a new sampling point
    nInitialIterationsWithoutClustering = 2000      #The firs n iterations, we assume that there is only 1 cluster
    nIterationsWithSameClustering = 20              #Clustering is only happening every X iterations
    initialEnlargementFraction = 0.2                #Fraction by which each axis in an ellipisoid has to be enlarged, >= 0,
                                                    # where 0 means no enlargement
    shrinkingRate = 0.15                            #Exponent for remaining prior mass in ellipsoid enalargement fraction
                                                    #It is a number between 0 and 1. The smalle the slower the shrinkage of
                                                    # the ellipsoids
    terminationFactor = 0.05                        #termination factor for nesting loops

    nestedSampler = MultiEllipsoidSampler(printOnScreen,[uniformPriors],likelihood,metric,kmeans,initialNobjects
                                          ,minNobjects,initialEnlargementFraction,shrinkingRate)

To finally run the the algorithm, we just need to create a powerlawReducer and call the run function.

.. code-block::python

    tolerance = 1.e2
    exponent = 0.4

    livePointsReducer = PowerlawReducer(nestedSampler, tolerance, exponent, terminationFactor)
    outputPathPrefix = "demoEggboxFunction_"
    nestedSampler.run(livePointsReducer, nInitialIterationsWithoutClustering, nIterationsWithSameClustering, maxNdrawAttempts,
                      terminationFactor, outputPathPrefix)

In the end we want to save the result, for which we will create a ``Results`` class and write them to the filesystem.

.. code-block::python

    #save results
    results = Results(nestedSampler)
    results.writeParametersToFile("parameter",".txt")
    results.writeLogLikelihoodToFile("logLikelihood.txt")
    results.writeEvidenceInformationToFile("evidenceInformation.txt")
    results.writePosteriorProbabilityToFile("posteriorDistribution.txt")

    credibleLevel = 68.3
    writeMarginalDistributionToFile = False

    results.writeParametersSummaryToFile("parameterSummary.txt", credibleLevel, writeMarginalDistributionToFile)

The full code for this example is available in the examples folder.

Comparison
----------

It should be clear now, why using python for this is very advantagous. The code reduction is from around 270 lines of
code in C++ to 64 lines of code in python. This comes at the cost of being significantly slower than the pure C++ Code