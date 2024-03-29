import pandas as pd
data = {'Student': ['Ice Bear','Panda','Grizzly'],'Math' : [80,95,79]}
bear = pd.DataFrame(data,columns = ['Student','Math'])
data2 = {'Student': ['Ice Bear','Panda','Grizzly'],'Electronics' : [85,81,83]}
bear2 = pd.DataFrame(data2,columns = ['Student','Electronics'])
data3 = {'Student': ['Ice Bear','Panda','Grizzly'],'GEAS' : [90,79,93]}
bear3 = pd.DataFrame(data3,columns = ['Student','GEAS'])
data4 = {'Student': ['Ice Bear','Panda','Grizzly'],'ESAT' : [93,89,88]}
bear4 = pd.DataFrame(data4,columns = ['Student','ESAT'])

x = pd.merge(bear,bear2, how='right', on='Student')
y = pd.merge(x,bear3,how='right', on='Student')
z = pd.merge(y,bear4, how='right', on='Student')
LongFormat = pd.melt(z,id_vars='Student',var_name = 'Subject',value_name = 'Grades')
LongFormat = LongFormat.sort_values('Student').reset_index().drop(columns = ['index'])
print(LongFormat)