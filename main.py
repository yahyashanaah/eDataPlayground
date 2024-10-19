import pandas as pd
import re

# Load the CSV file with a different encoding (ISO-8859-1)
df = pd.read_csv('data.csv', header=None, names=[
                 "ID", "Date", "Email", "Message"], encoding='ISO-8859-1')

# Function to extract 17-character alphanumeric VINs


def extract_vin(message):
    # VIN regex: 17 alphanumeric characters (excluding I, O, Q)
    match = re.findall(r'\b[A-HJ-NPR-Z0-9]{17}\b', message)
    return match[0] if match else None


# Apply the VIN extraction function to the last column (Message) and create a new column 'VIN'
df['VIN'] = df['Message'].apply(extract_vin)

# Save the updated CSV to a new file
df.to_csv('updated_data.csv', index=False)

print("VIN column added successfully and saved to 'updated_data.csv'")
