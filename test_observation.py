import pytest
from aurelion.data.observation import Observation

def test_observation_creation():
    item = Observation.create("test-feed", 12.5)
    assert item.source == "test-feed"
    assert item.value == 12.5
    assert item.timestamp

def test_observation_rejects_empty_source():
    with pytest.raises(ValueError):
        Observation.create(" ", 12.5)
