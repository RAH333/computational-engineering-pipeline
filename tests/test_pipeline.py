import pytest
from src.calculator import EngineeringCalculator

def test_stress_calculation():
    # Verify standard functional calculations
    assert EngineeringCalculator.calculate_structural_stress(100, 2) == 50

def test_invalid_area_exception():
    # Verify that errors are caught correctly by the logical engine
    with pytest.raises(ValueError):
        EngineeringCalculator.calculate_structural_stress(100, 0)
