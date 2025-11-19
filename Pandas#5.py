import pandas as pd

############################
# About data standardization
############################

# Load the breast cancer dataset 
df = pd.read_csv("https://staticasssets.blob.core.windows.net/open-ai-coderunner/scripts/breast_cancer_data.csv") 

# Check the data types of all columns 
print("Data Types of Columns: ") 
print(df.dtypes) 