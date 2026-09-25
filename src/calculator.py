import numpy as np

class EngineeringCalculator:
    """Handles complex engineering math calculations and modeling."""
    
    @staticmethod
    def calculate_fluid_velocity(flow_rate: float, diameter: float) -> float:
        """Calculates velocity based on continuous flow rate and pipe diameter."""
        if diameter <= 0 or flow_rate < 0:
            raise ValueError("Invalid physical dimensions provided.")
        area = np.pi * (diameter ** 2) / 4
        return flow_rate / area

    @staticmethod
    def calculate_structural_stress(force: float, area: float) -> float:
        """Calculates mechanical stress (Force / Area)."""
        if area <= 0:
            raise ValueError("Area must be greater than zero.")
        return force / area
      
