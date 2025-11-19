import pandas as pd

#data = ['Steven', '35', 'Male', '3.5']
data = [1.1, 2.2, '3.3', 4.4]
series = pd.Series(data, index=['Name', 'Age', 'Gender', 'Rating'])
series1 = pd.Series([1.1, 2.2, 3.3])
series2 = pd.Series(['apple', 'banana', 'cherry'])
series3 = pd.Series(( 'abcd', 786 , 2.23, 'john', 70.2 ))
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]



print ("Type of data: ", type(data))
print ("Type of series: ", series.dtype)
print ("Type of series: ", type(series), "\n")

print ("Type of series: ", series1.dtype)
print ("Type of series: ", type(series1), "\n")

print ("Type of series: ", series2.dtype)
print ("Type of series: ", type(series2), "\n")

print (series3[1:3], "\n")
print ("list: ", list[1:3], "\n") 
print (type(series3))

a=int(3* 2.24)
print(a)

#print(series)
