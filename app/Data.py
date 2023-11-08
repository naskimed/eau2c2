""" Here we will define the data that will be used in the dashboard """

# Importing libraries
import pandas as pd





# Cleaning the data

# Importing the data
data = pd.read_csv('Data.csv')

# Create a mapping of old column names to new column names with spaces removed
column_name_mapping = {col: col.replace(' ', '') for col in data.columns}

# Rename the columns using the mapping
data = data.rename(columns=column_name_mapping)


# Creating a function to change the data to be suitable for the model

def change_data_format(data):
    columns_to_convert = [
    'PLUV(mm)', 'COTE(m)', 'VOLUME(Mm3)', 'SURFACE(Ha)', 'EVP(mm)',
           'V.Evap(Mm3)', 'IRRIGATION(Mm3)', 'DEVASEMENT(Mm3)', 'TURBINAGE(Mm3)',
           'FUITE(Mm3)', 'TRANSFERT(Mm3)', 'DEVERSEMENT(Mm3)', 'TotLach(Mm3)',
           'Bilan(Mm3)', 'Apport(Mm3)', 'Perte(Mm3)']
    # Loop through each column and convert to float, treating empty strings as NaN
    for col in columns_to_convert:
        data[col] = pd.to_numeric(data[col].str.strip(), errors='coerce')

    data=data.dropna()

    columns_to_delete = [9, 11]  # Replace with the actual column indices you want to delete
    # Use iloc to delete the specified columns by index
    data = data.drop(data.columns[columns_to_delete], axis=1)
    # Now, the columns at the specified indices have been removed from the DataFrame
    data.info()

    return data
