import pandas as pd

class DataVerifier:
    """Evaluates multi-layered datasets to isolate logical errors and variations."""
    
    def __init__(self, file_path: str):
        self.df = pd.read_csv(file_path)

    def flag_anomalies(self) -> pd.DataFrame:
        """Flags non-physical engineering values (e.g., negative pressures or excessive stress)."""
        # Criteria: Pressure cannot be negative, Stress cannot exceed material limits (e.g., 250 MPa)
        self.df['anomaly_detected'] = (self.df['pressure_psi'] < 0) | (self.df['calculated_stress_mpa'] > 250)
        return self.df

    def cross_reference_calculations(self, expected_velocity_col: str) -> bool:
        """Verifies dataset internal consistency against strict baseline equations."""
        # Simple logical audit to verify data alignment
        mismatches = self.df[self.df['recorded_velocity'] != self.df[expected_velocity_col]]
        return len(mismatches) == 0
      
