import pytest

from gaqqie_door.adaptor.qiskit.gaqqie_provider import GaqqieProvider


class TestGaqqieProvider:
    def test_init(self):
        # default parameters
        actual = GaqqieProvider()
        assert actual.name == "gaqqie"
        assert actual.status == None
        assert actual.description == None

        # specific parameters
        actual = GaqqieProvider(
            name="test_provider", status="ACTIVE", description="desc"
        )
        assert actual.name == "test_provider"
        assert actual.status == "ACTIVE"
        assert actual.description == "desc"
