import os
import pandas as pd
from src.calculator import EngineeringCalculator
from src.verifier import DataVerifier

def run_pipeline():
    print("Initializing Computational Engineering Pipeline...")
    
    # 1. Create mock input simulation data if it doesn't exist
    if not os.path.exists('data'):
        os.makedirs('data')
        
    raw_data_path = 'data/raw_simulation_data.csv'
    mock_data = pd.DataFrame({
        'trial_id':,
        'force_n': [10000, 15000, -5000, 20000],  # Trial 3 has anomalous force
        'area_m2': [0.05, 0.05, 0.05, 0.0001],   # Trial 4 will cause extreme stress
        'pressure_psi': [120, 145, -10, 130],     # Trial 3 has negative pressure
        'recorded_velocity': [2.5, 3.1, 0.0, 4.2]
    })
    mock_data.to_csv(raw_data_path, index=False)
    
    # 2. Process data with Engineering Calculations
    print(" Executing math modeling and transformations...")
    df = pd.read_csv(raw_data_path)
    
    stress_outputs = []
    for idx, row in df.iterrows():
        try:
            stress = EngineeringCalculator.calculate_structural_stress(row['force_n'], row['area_m2'])
            stress_outputs.append(stress / 1e6) # Convert to MPa
        except ValueError:
            stress_outputs.append(None)
            
    df['calculated_stress_mpa'] = stress_outputs
    df.to_csv(raw_data_path, index=False)

    # 3. Perform Data Verification Audit
    print("🔍 Auditing dataset for anomalies and logical gaps...")
    verifier = DataVerifier(raw_data_path)
    audited_df = verifier.flag_anomalies()
    
    # Save the formal technical deliverable
    output_path = 'data/verified_output.csv'
    audited_df.to_csv(output_path, index=False)
    print(f" Technical verification complete. Output saved to: {output_path}")

if __name__ == "__main__":
    run_pipeline()
