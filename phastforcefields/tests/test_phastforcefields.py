"""
Test loading PHAST Force fields via the plugin interface through the toolkit.
"""
import openmm
import pytest
from openff.toolkit.topology import Molecule
from openff.toolkit.typing.engines.smirnoff import ForceField
from openmm import unit


@pytest.mark.parametrize(
    "forcefield",
    [
        pytest.param("PHAST-HCNO-2.0.0.offxml", id="HCNO"),
        pytest.param("PHAST-H2CNO-2.0.0.offxml", id="H2CNO"),
        pytest.param("PHAST-HC2NO-2.0.0.offxml", id="HC2NO"),
        pytest.param("PHAST-HC4NO-2.0.0.offxml", id="HC4NO"),
        pytest.param("PHAST-H2C4NO-2.0.0.offxml", id="H2C4NO"),
        pytest.param("PHAST-H2CNO-ecut-1000-2.0.0.offxml", id="H2CNO-ecut-1000"),
        pytest.param("PHAST-H2CNO-ecut-100-2.0.0.offxml", id="H2CNO-ecut-100"),
        pytest.param("PHAST-H2CNO-nonpolar-2.0.0.offxml", id="H2CNO-nonpolar"),
    ],
)
def test_load_phast_ff(forcefield):
    """
    Load the PHAST FF and create an OpenMM system.
    """

    ff = ForceField(forcefield, load_plugins=True)
    ethanol = Molecule.from_smiles("CCO")

    system = ff.create_openmm_system(topology=ethanol.to_topology())

    forces = {force.__class__.__name__: force for force in system.getForces()}
    print(forces)
