from aurelion.core.engine import AurelionEngine


def test_engine_starts_empty():
    engine = AurelionEngine()
    assert engine.status()["observations_recorded"] == 0


def test_engine_records_observation():
    engine = AurelionEngine()
    engine.record({"symbol": "TEST", "price": 100.0})

    assert engine.status()["observations_recorded"] == 1
