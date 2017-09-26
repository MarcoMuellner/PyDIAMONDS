//
// Created by mamu on 9/20/17.
//

#ifndef DIAMONDS_PYMODEL_H
#define DIAMONDS_PYMODEL_H
#include "Model.h"
#include <pybind11/eigen.h>
#include <pybind11/pybind11.h>

using Eigen::ArrayXd;
typedef Eigen::Ref<Eigen::ArrayXd> RefArrayXd;

template <class ModelBase = Model> class PyModel : public ModelBase
{
public:
    using ModelBase::ModelBase;
    ArrayXd predict(RefArrayXd predictions, const RefArrayXd modelParameters) override
    {
        PYBIND11_OVERLOAD_PURE(
                ArrayXd,
                ModelBase,
                predict,
                predictions,
                modelParameters
        );
    }
};

#endif //DIAMONDS_PYMODEL_H
