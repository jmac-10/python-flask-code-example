import pandas as pd

path = "data/patient_tb.csv"
data = pd.read_csv(path)
data.drop_duplicates(
    subset=["PatientID", "MostRecentTestDate", "TestName"],
    inplace=True
)
data.to_csv(path, index=False)
