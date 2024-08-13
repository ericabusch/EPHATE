# Exogenous-PHATE (E-PHATE) package

## Quick Start
If you would like to get started using E-PHATE, check out our example below or sample notebook within this repository.

If you have loaded a matrix `X1` (with samples on rows, features on columns, generally a form of high-dimensional biological data) and a second matrix of *exogenously-measured* data `X2` (with matched samples in the same order as the rows of `X1`), you can run E-PHATE as follows:

```
import ephate

ephate_op = ephate.EPHATE()
ephate_embedding = ephate_op.fit_transform(X1, X2)

```
Exogenous-PHATE (E-PHATE) is a method to model the interplay of multi-dimensional, multi-modal measurements from matched samples as a low-dimensional manifold. In our recent paper "Manifold learning uncovers nonlinear interactions between the adolescent brain and environment that predict emotional and behavioral problems," we use E-PHATE to combine children's brain activation with multiple metrics of risk in their environments. These are both high-dimensional, noisy measurements hypothesized to interact in a complex manner and explain variance in mental health, and E-PHATE uncovers low-dimensional manifold structure which improves prediction of mental health outcomes. E-PHATE is a general-purpose method for combining high-dimensional samples of signals measured endogenously (e.g., fMRI activation) with signals measured exogenously (e.g., behavioral or environmental data) for matched samples (i.e., different metrics about the same samples).

For more information, see our [publication in Biological Psychiatry: Cognitive Neuroscience and Neuroimaging](https://doi.org/10.1016/j.bpsc.2024.07.001).

### Erica L. Busch, August 2024
