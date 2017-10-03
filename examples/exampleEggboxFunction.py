import numpy as np
from pyDiamonds import *

class EggboxLikelihood(Likelihood):
    def __init__(self,observation,model):
        Likelihood.__init__(self,observation,model)
    def logValue(self,nestedSampleOfParameters):
        return np.power(2.0+np.cos(nestedSampleOfParameters[0]/2)*np.cos(nestedSampleOfParameters[1]/2),5)

data = np.array(([],[]))        #create Dummy data
model = ZeroModel(data[0])      #create dummy model -> likelihood directly computed

priors = np.array(([0,0],[10*np.pi,10*np.pi])).astype(float) #setup prior distribution. Array must be float!
uniformPriors = UniformPrior(priors[0],priors[1])

likelihood = EggboxLikelihood(data[0],model) #setup likelihood function


metric = EuclideanMetric()
minNclusters = 6
maxNclusters = 10
nTrials = 10
relTolerance = 0.01

kmeans = KmeansClusterer(metric,minNclusters,maxNclusters,nTrials,relTolerance) #setup k-means clusterer using euclidean metric

#configure nested sampling reference

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

tolerance = 1.e2
exponent = 0.4

livePointsReducer = PowerlawReducer(nestedSampler, tolerance, exponent, terminationFactor)
outputPathPrefix = "demoEggboxFunction_"
nestedSampler.run(livePointsReducer, nInitialIterationsWithoutClustering, nIterationsWithSameClustering, maxNdrawAttempts,
                  terminationFactor, outputPathPrefix)

#save results
results = Results(nestedSampler)
results.writeParametersToFile("parameter",".txt")
results.writeLogLikelihoodToFile("logLikelihood.txt")
results.writeEvidenceInformationToFile("evidenceInformation.txt")
results.writePosteriorProbabilityToFile("posteriorDistribution.txt")

credibleLevel = 68.3
writeMarginalDistributionToFile = False

results.writeParametersSummaryToFile("parameterSummary.txt", credibleLevel, writeMarginalDistributionToFile)