# phast-forcefields

![workflow badge](https://github.com/space-group-research/phast-forcefields/actions/workflows/python-package-conda.yml/badge.svg)

General purpose small molecule forcefields with alternative functional forms.

## Functional Forms

### Repulsion-Dispersion Potential

$$U_{rd} = \sum_{i \neq j} \frac{F_0}{\beta_{ij}} e^{\beta_{ij}(r_{ij}-\rho_{ij} )} + \sum_{n=3}^5 f_{2n}(\beta r_{ij}) \frac{C_{2n}}{r_{ij}^{2n}}$$

$$f_{2n}( \beta r_{ij} ) = 1 - e^{- \beta r_{ij}} \sum_{k=0}^{2n} \frac{(\beta r_{ij})^k}{k!}$$

$$C_{2n, ij} = \sqrt{C_{2n, ii} * C_{2n, jj}}; n = 3, 4, 5$$

$$\rho_{ij} = \frac{1}{2} ( \rho_{ii} + \rho_{jj} )$$

$$\beta_{ij} = 2 \frac{\beta_{ii}\beta_{jj}}{\beta_{ii}+\beta_{jj}}$$

### Explicit Polarization

$$\vec{\mu}_{i} = \alpha_i \left( \vec{E}_i + \vec{E}^\prime_i \right)$$

$$\vec{\mu}_{i} = \alpha_i \left( \vec{E}_i - \sum_{j \neq i} \mathbf{T}_{ij} \vec{\mu}_j \right)$$

# Installation

```bash
git clone https://github.com/space-group-research/phast-forcefields.git
cd phast-forcefields/devtools/conda-envs
conda env create --file test_env.yaml
conda activate phastff-test
cd ../..
python3 -m pip install .
```

## Usage

```python3
>>> from openff.toolkit import ForceField
>>> ff = ForceField('PHAST-H2CNO-2.0.0.offxml', load_plugins=True)
```

# History

## Version 2.1.0

WIP

## Version 2.0.0

Published in JCTC soon. Note that a water model is not included in this version of the forcefield.

- **PHAST-H2CNO-2.0.0.offxml** - Recommended for general use, mostly element-typed forcefield with 2 atom types for hydrogen
- **PHAST-H2CNO-nonpolar-2.0.0.offxml** - Nonpolar version of the above, only recommended for systems lacking significant permanent polarity
- **PHAST-HCNO-2.0.0.offxml** - Element-typed forcefield
- **PHAST-HC4NO-2.0.0.offxml** - Forcefield with 4 different carbon atom types (sp3, sp2, sp and aromatic sp2)
- **PHAST-HC2NO-2.0.0.offxml** - Forcefield with 2 different carbon atom types (aromatic and nonaromatic)
- **PHAST-H2C4NO-2.0.0.offxml** - Forcefield with 4 different carbon atom types and 2 hydrogen atom types
- **PHAST-H2CNO-ecut-1000-2.0.0.offxml** - Hyperparameter testing forcefield (not recommended)
- **PHAST-H2CNO-ecut-100-2.0.0.offxml** - Hyperparameter testing forcefield (not recommended)

## General versioning guidelines

Force fields moving forward will be called `name-X.Y.Z`

* `X` denotes some major change in functional form or fitting strategy.
* `Y` is the parameterization epoch / generation, or a minor change that can affect energy.
* `Z` is a bugfix version -- e.g. something we've caught and corrected.

## Copyright

Copyright (c) 2023-2025 Adam Hogan
