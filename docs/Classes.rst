Classes
=======

This section describes the implemented classes and the methods that are available via the bindings. This list is temporary, and will be replaced in v2.0.0 with a proper documentation of the interface. For now it only lists the available classes and their methods as well as the type of arguments they accept. Generally also shows return types if they are non void (C++). Further documentation can be found within the header files of DIAMONDS.

``Clusterer``
-------------
The ``Clusterer`` is an abstract class for clustering algorithms.

+ ``__init__(Metric)``
+ ``cluster(ndarray,[int],[int])`` ``ret:int`` ``pure virtual``

``Ellipsoid``
-------------
The ``Ellipsoid`` creates an ellipsoid object to be used within the sampler class

+ ``_init_(ndarray,float)``
+ ``resetEnlargementFraction(float)```
+ ``overlapsWith(Ellipsoid,bool)`` ``ret:bool``
+ ``containsPoint(ndarray)`` ``ret:bool``
+ ``drawPoint(ndarray)`` 
+ ``getCenterCoordinates()`` ``ret:ndarray``
+ ``getEigenvalues()`` ``ret:ndarray``
+ ``getSample()`` ``ret:ndarray``
+ ``getCovarianceMatrix()`` ``ret:ndarray``
+ ``getEigenvectors()`` ``ret:ndarray``
+ ``getSampleSize()`` ``ret:int``
+ ``getHyperVolume()`` ``ret:float``
+ ``getEnlargementFraction()`` ``ret:float``

``Metric``
----------

The ``Metric`` abstract class provides metric distances for the sampler class.

+ ``__init__()``
+ ``distance(ndarray,ndarray)`` ``ret:float`` ``pure virtual``

``Likelihood``
--------------

The ``Likelihood`` abstract class provides likelihood computations.

+ ``__init__(ndarray,Model)``
+ ``getObservations()`` ``ret:ndarray``
+ ``logValue(ndarray)`` ``ret:float`` ``pure virtual``

``Model``
---------

The ``Model`` abstract class provides an interface for building models.

+ ``__init__(ndarray)``
+ ``getCovariates()`` ``ret:ndarray``
+ ``predict(ndarray,ndarray)`` ``ret:ndarray`` ``pure virtual``
+ ``getNParameters()`` ``ret:int``

``Prior``
---------

The ``Prior`` abstract class provides an interface for prior computations.

+ ``__init__(int)``
+ ``logDensity(ndarray,bool)`` ``ret:float`` ``pure virtual``
+ ``drawnPointIsAccepted(ndarray)`` ``ret:bool`` ``pure virtual``
+ ``draw(ndarray)`` ``pure virtual``
+ ``drawWithConstraint(ndarray,Likelihood)`` ``pure virtual``
+ ``writeHyperParametersToFile(str)`` ``pure virtual``

``LivePointsReducer``
---------------------

The ``LivePointsReducer`` abstract class provides an interface for the nested sampling.

+ ``__init__(NestedSampler)``
+ ``findIndicesOfLivePointsToRemove`` ``ret:[int]``
+ ``getNlivePointsToRemove()`` ``ret:int``
+ ``updateNlivePoints()`` ``ret:int`` ``pure virtual``

``NestedSampler``
-----------------
The ``NestedSampler`` abstract class provides an implementation of the nested sampling algorithm.

+ ``__init__(bool, int, int, [Prior], Likelihood, Metric, Clusterer``
+ ``run(LivePointsReducer, int, int, int, float, str)``
+ ``drawWithConstraint(ndarray, int, [int], [int], ndarray, float, int)`` ``ret:bool``
+ ``getNiterations()`` ``ret:int``
+ ``getNdimensions()`` ``ret:int``
+ ``getNlivePoints()`` ``ret:int``
+ ``getInitialNlivePoints()`` ``ret:int``
+ ``getMinNlivePoints()`` ``ret:int``
+ ``getLogCumulatedPriorMass()`` ``ret:float``
+ ``getLogRemainingPriorMass()`` ``ret:float``
+ ``getRatioOfRemainderToCurrentEvidence()`` ``ret:float``
+ ``getLogMaxLikelihoodOfLivePoints()`` ``ret:float``
+ ``getComputationalTime()`` ``ret:float``
+ ``getTerminationFactor()`` ``ret:float``
+ ``getNlivePointsPerIteration()`` ``ret:[int]``
+ ``getNestedSample()`` ``ret:ndarray``
+ ``getLogLikelihood()`` ``ret:ndarray``
+ ``setLogEvidence(float)``
+ ``getLogEvidence()`` ``ret:float``
+ ``setLogEvidenceError(float)``
+ ``getLogEvidenceError()`` ``ret:float``
+ ``setInformationGain(float)`` ``ret:float``
+ ``getInformationGain()`` ``ret:float``
+ ``setPosteriorSample(ndarray)``
+ ``getPosteriorSample()`` ``ret:ndarray``
+ ``setLogLikelihoodOfPosteriorSample(ndarray)``
+ ``getLogLikelihoodOfPosteriorSample()`` ``ret:ndarray``
+ ``setLogWeightOfPosteriorSample(ndarray)`` ``ret:ndarray``
+ ``getLogWeightOfPosteriorSample()`` ``ret:ndarray``
+ ``setOutputPathPrefix(str)``
+ ``getOutputPathPrefix()`` ``ret:str``
+ ``verifySamplerStatus()`` ``ret:bool`` ``pure virtual``

``EuclideanMetric``
-------------------
The ``EuclideanMetric`` class implements the virtual functions of ``Metric`` and has the same signature.

``ExponentialLikelihood``
-------------------------
The ``ExponentialLikelihood`` class implements the virtual functions of ``Likelihood`` and has the same signature

``FerozReducer``
----------------
The ``FerozReducer`` class implements the virtual functions of ``LivePointsReducer`` and has the same signature

``GridUniformPrior``
--------------------
The ``GridUniformPrior`` class implements the virtual functions of ``Prior`` and has the same signature, except:

+ ``__init__(ndarray,ndarray,ndarray,ndarray)``
+ ``getStartingCoordinate()`` ``ret:ndarray``
+ ``getNgridPoints()`` ``ret:ndarray``
+ ``getSeparation()`` ``ret:ndarray``
+ ``getTolerance()`` ``ret:ndarray``

``KmeansClusterer``
-------------------
The ``KmeansClusterer`` class implements the virtual functions of ``Clusterer`` and has the same signature, except:

+ ``__init__(Metric,int,int,int,float)``

``MultiEllipsoidSampler``
-------------------------
The ``MultiEllipsoidSampler`` class implements the virtual functions of ``NestedSampler`` and has the same signature, except:

+ ``__init__(bool,[Prior],Likelihood,Metric,Clusterer,int,int,float,float)``
+ ``getEllipsoids()`` ``ret:[Ellipsoid]``
+ ``getInitialEnlargementFraction()`` ``ret:float``
+ ``getShrinkingRate()`` ``ret:float``

``NormalLikelihood``
--------------------
The ``NormalLikelihood`` class implements the virtual functions of ``Likelihood`` and has the same signature, 
except:

+ ``getUncertainties()`` ``ret:ndarray``

``NormalPrior``
---------------
The ``NormalPrior`` class implements the virtual functions of ``Prior`` and has the same signature, except:

+ ``__init__(ndarray,ndarray)``
+ ``getMean()`` ``ref:ndarray``
+ ``getStandardDeviation()`` ``ref:ndarray``

``PowerlawReducer``
-------------------
The ``PowerlawReducer`` class implements the virtual functions of ``LivePointsReducer`` and has the same signature, except:

+ ``__init__(NestedSampler,double,double,double)``

``Results``
-----------
The ``Results`` class implements a possibility to write files to the system.

+ ``__init__(NestedSampler)``
+ ``writeParametersToFile(str, str)``
+ ``writeLogLikelihoodToFile(str)``
+ ``writeLogWeightsToFile(str)``
+ ``writeEvidenceInformationToFile(str)``
+ ``writePosteriorProbabilityToFile(str)``
+ ``writeLogEvidenceToFile(str)``
+ ``writeLogMeanLiveEvidenceToFile(str)``
+ ``writeParametersSummaryToFile(str, double, bool )`` 

``SuperGaussianPrior``
----------------------
The ``SuperGaussianPrior`` class implements the virtual functions of ``Prior`` and has the same signature, except:

+ ``__init__(ndarray,ndarray,ndarray)``
+ ``getCenter()`` ``ret:ndarray``
+ ``getSigma()`` ``ret:ndarray``
+ ``getWidthOfPlateau()`` ``ret:ndarray``

``UniformPrior``
----------------
The ``UniformPrior`` class implements the virtual functions of ``Prior`` and has the same signature, except:

+ ``__init__(ndarray,ndarray)``
+ ``getMinima()`` ``ret:ndarray``
+ ``getMaxima()`` ``ret:ndarray``

``ZeroClusterer``
-----------------
The ``ZeroClusterer`` class implements the virtual functions of ``Clusterer`` and has the same signature.

``ZeroPrior``
-------------
The ``ZeroPrior`` class implements the virtual functions of ``Prior`` and has the same signature.
