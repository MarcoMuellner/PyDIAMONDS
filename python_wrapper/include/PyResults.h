//
// Created by marco on 03.10.17.
//

#ifndef PYDIAMONDS_PYRESULTS_H
#define PYDIAMONDS_PYRESULTS_H

#include "Results.h"

class ResultsPublicist : public Results {
public:
    using Results::parameterEstimation; // inherited with different access modifier
    using Results::posteriorProbability;
};


#endif //PYDIAMONDS_PYRESULTS_H
