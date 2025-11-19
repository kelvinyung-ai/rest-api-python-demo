import pandas as pd
import warnings

#########################
# About remove duplicate
#########################

# Ignore warning messages to enhance readability 
warnings.filterwarnings('ignore')    
 
# Load the breast cancer dataset 
df = pd.read_csv("https://staticasssets.blob.core.windows.net/open-ai-coderunner/scripts/breast_cancer_data.csv") 

# Identify duplicates based on all columns  
duplicates = df.duplicated()  
 
# Print the duplicate row(s)  
print('Duplicate row(s) in the DataFrame', df[duplicates])  

# Keep the first occurrence of duplicates 
# The cleaned dataset is stored in the DataFrame df_cleaned. It contains the original rows but without any duplicates beyond the first occurrence. 
df_cleaned = df.drop_duplicates(keep='first') 

# Keep the last occurrence of duplicates 
df_cleaned = df.drop_duplicates(keep='last') 

# Remove the duplicate rows from the DataFrame in-place
# By setting inplace=True, the DataFrame df is modified directly.
df.drop_duplicates(inplace=True) 


# Print the duplicate rows after removing duplicates from the DataFrame 
print('After removing duplicates from the DataFrame', df[duplicates]) 

# Print the cleaned dataset
# head() - displays the first few rows, default is 5 rows
print("\nCleaned Dataset:") 
print(df_cleaned.head()) 

# Specify the columns for duplicate identification 
columns_to_check = ['patient_id', 'clump_thickness', 'cell_size_uniformity'] 

# Remove duplicates based on specific columns 
df_cleaned = df.drop_duplicates(subset=columns_to_check) 

# Print the cleaned dataset 
print(df_cleaned.tail(10))