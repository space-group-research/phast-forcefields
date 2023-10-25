# phast-forcefields

![workflow badge](https://github.com/space-group-research/phast-forcefields/actions/workflows/python-package-conda.yml/badge.svg)

# Installation

```
git clone https://github.com/space-group-research/phast-forcefields.git
cd phast-forcefields/devtools/conda-envs
conda env create --file test_env.yaml
conda activate phastff-test
cd ../..
python3 -m pip install .
```

## Usage

```python3
>>> from openff.toolkit.typing.engines.smirnoff import ForceField
>>> ff = ForceField('PHAST-H2CNO-2.0.0.offxml', load_plugins=True)
```

# History

To be published

## General versioning guidelines

Force fields moving forward will be called `name-X.Y.Z`

* `X` denotes some major change in functional form or fitting strategy.
* `Y` is the parameterization epoch / generation, or a minor change that can affect energy.
* `Z` is a bugfix version -- e.g. something we've caught and corrected.

## Copyright

Copyright (c) 2023 Adam Hogan
