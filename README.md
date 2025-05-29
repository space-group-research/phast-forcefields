# phast-forcefields

![workflow badge](https://github.com/space-group-research/phast-forcefields/actions/workflows/python-package-conda.yml/badge.svg)

PHAST (Potentials with High Accuracy, Speed, and Transferability) provides general purpose small molecule forcefields with physically motivated functional forms. These forms are distinct from traditional Lennard-Jones based forcefields. Transferability is achieved by the default inclusion of explicit polarization and fitting parameters soley to electronic structure calculations.

## Functional Forms

### Repulsion-Dispersion Potential

The repulsion-dipsersion potential is a combination of exponential repulsion and the three leading dispersion coefficients, which are damped at short ranges to avoid singularities,

$$U_{rd} = \sum_{i \neq j} \frac{F_0}{\beta_{ij}} e^{\beta_{ij}(r_{ij}-\rho_{ij} )} + \sum_{n=3}^5 f_{2n}(\beta r_{ij}) \frac{C_{2n}}{r_{ij}^{2n}}$$

$$f_{2n}( \beta r_{ij} ) = 1 - e^{- \beta r_{ij}} \sum_{k=0}^{2n} \frac{(\beta r_{ij})^k}{k!}$$

Mixing rules for the dispersion coefficients are the usual geometric mean mixing rule from London and the repulsion mixing are from Smith 1972.

$$C_{2n, ij} = \sqrt{C_{2n, ii} * C_{2n, jj}}; n = 3, 4, 5$$

$$\rho_{ij} = \frac{1}{2} ( \rho_{ii} + \rho_{jj} )$$

$$\beta_{ij} = 2 \frac{\beta_{ii}\beta_{jj}}{\beta_{ii}+\beta_{jj}}$$

### Explicit Polarization

Many-body polarization is included via the induced dipole method of Silberstein, Thole and Applequist. The induced dipoles are obtained by scaling the atomic electric field by the atom's polarizability.

$$\vec{\mu}_{i} = \alpha_i \left( \vec{E}_i + \vec{E}^\prime_i \right)$$

Each induced dipole then induces an electric field on every other induced dipole, making the model many-body.

$$\vec{\mu}_{i} = \alpha_i \left( \vec{E}_i - \sum_{j \neq i} T_{ij} \vec{\mu}_j \right)$$

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
from openff.interchange import Interchange
from openff.toolkit import Molecule, ForceField
from openff.units import unit
from openff.units.openmm import to_openmm, from_openmm
import numpy as np
import openmm
import sys
ff = ForceField('PHAST-H2CNO-2.0.0.offxml', load_plugins=True)
mol = Molecule.from_smiles('CCC')
mol.generate_conformers()
cubic_box = unit.Quantity(30 * np.eye(3), unit.angstrom)
interchange = Interchange.from_smirnoff(topology=[mol], force_field=ff, box=cubic_box)
openmm_sys = interchange.to_openmm(combine_nonbonded_forces=False)
openmm_top = interchange.topology.to_openmm()
openmm_positions = interchange.positions.to_openmm()
openmm_integrator = openmm.LangevinMiddleIntegrator(
    to_openmm(300*unit.kelvin),
    to_openmm(1/unit.picosecond),
    to_openmm(0.002*unit.picoseconds)
)
simulation = openmm.app.Simulation(openmm_top, openmm_sys, openmm_integrator)
simulation.context.setPositions(openmm_positions)
simulation.minimizeEnergy()
simulation.reporters.append(openmm.app.PDBReporter('output.pdb', 1000))
simulation.reporters.append(openmm.app.StateDataReporter(sys.stdout, 1000, step=True,
        potentialEnergy=True, temperature=True))
simulation.step(10000)
```

# Limitations

Currently, a water model is not provided, this is a work in progess. OpenFF Interchange does not support export to any simulation software other than OpenMM due to the custom repulsion-dispersion potential. AmoebaMultipoleForce in OpenMM is being used behind the scenes, however this choice is not ideal due to some particular choices made early in AMOEBA's development.

# Publications

**The PHAST 2.0 Force Field for General Small Molecule and Materials Simulations**
Adam Hogan, Logan Ritter, and Brian Space
in press

**PHAHST Potential: Modeling Sorption in a Dispersion-Dominated Environment**
Logan Ritter, Brant Tudor, Adam Hogan, Tony Pham, and Brian Space
*Journal of Chemical Theory and Computation* **2024** *20* (13), 5570-5582
DOI: 10.1021/acs.jctc.4c00226

**Next-Generation Accurate, Transferable, and Polarizable Potentials for Material Simulations**
Adam Hogan and Brian Space
*Journal of Chemical Theory and Computation* **2020** *16* (12), 7632-7644
DOI: 10.1021/acs.jctc.0c00837

# History

## Version 2.1.0

WIP

## Version 2.0.0

Published in JCTC soon. Note that a water model is not included in this version of the forcefield.

- **PHAST-H2CNO-2.0.0.offxml** - Recommended for general use, mostly element-typed forcefield with 2 atom types for hydrogen
- **PHAST-H2CNO-direct-2.0.0.offxml** - Direct polarization version of the above, not included in published benchmarking
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
