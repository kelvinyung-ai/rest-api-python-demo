import pandas as pd

#########################
# About detect duplicate
#########################

df = pd.read_csv("https://staticasssets.blob.core.windows.net/open-ai-coderunner/scripts/breast_cancer_data.csv") 

# Identify duplicates based on all columns 
duplicates = df.duplicated() 

# Print out the duplicate counts  
print("duplicate counts: ", "\n", duplicates.value_counts(), "\n") 

# Print the duplicate row(s) 
print(df[duplicates]) 


# Specify the columns for duplicate identification 
#columns_to_check = ['patient_id', 'clump_thickness', 'cell_size_uniformity'] 

# Identify duplicates based on specific columns 
#duplicates = df.duplicated(subset=columns_to_check) 


# Print out the duplicate counts 
#print(duplicates.value_counts()) 

# Print the duplicate rows 
#print(df[duplicates]) 

# Mark duplicates using the keep parameter  
#duplicates = df.duplicated(subset=columns_to_check, keep='first')  

# Mark the duplicates
# To make the duplicates more visible, a new column 'Duplicates' is added to the DataFrame df, which contains the values of the duplicates series.
#df['Duplicates'] = duplicates 

# Print the duplicate rows  
# Finally, the last 10 rows of the DataFrame are displayed using the tail() and the print() functions, allowing you to observe and analyze the marked duplicate rows along with the rest of the data
#print(df.tail(10)) 

# Print the duplicate rows 
#print(df[duplicates]) 