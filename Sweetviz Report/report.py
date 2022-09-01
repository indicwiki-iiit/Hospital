import pandas as pd
import sweetviz

Hospitals = pd.read_excel("Final_Data_Hospitals.xlsx")

# Hospitals['Pincode'] = Hospitals['Pincode'].astype(str)
Hospitals['Pincode'] = pd.to_numeric(Hospitals['Pincode'], errors='coerce')

Hospitals['Contact No'] = pd.to_numeric(
    Hospitals['Contact No'], errors='coerce')

Hospitals['No. of Doctors'] = pd.to_numeric(
    Hospitals['No. of Doctors'], errors='coerce')

Hospitals['No. of Beds'] = pd.to_numeric(
    Hospitals['No. of Beds'], errors='coerce')
# Hospitals['District_ID'] = Hospitals['District_ID'].astype(str)

my_report = sweetviz.analyze(
    [Hospitals, "Hospitals"])
my_report.show_html('Hospital_Data_Report.html')
