import pandas

########################################
# About missing data and data imputation
########################################

ds = pandas.read_csv("https://staticasssets.blob.core.windows.net/open-ai-coderunner/scripts/breast_cancer_data.csv")
# Find missing volues
#print("Missing values in the original DataFrame:\n",ds.isnull().sum(), "\n")

# Find missing values 
print("Missing values in 'bland_chromatin' before imputation:\n ", df['bland_chromatin'].isnull().sum(),"\n") 

# Impute missing values with mean 
df['bland_chromatin'].fillna(df['bland_chromatin'].mean(), inplace=True) 

# Impute missing values with median 
df['bland_chromatin'].fillna(df['bland_chromatin'].median(), inplace=True) 

# Impute missing values with mode 
df['bland_chromatin'].fillna(df['bland_chromatin'].mode()[0], inplace=True) 

# Find missing values after imputation 
print("Missing values in 'bland_chromatin' after imputation:\n ",  
df['bland_chromatin'].isnull().sum(),"\n") 