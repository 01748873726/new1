import pandas as pd

mydataset = {
  'name': ["a", "b", "c"],
  'roll': [3, 7, 2]
}
address=["dhaka","kushtia","khulna"]

data = pd.DataFrame(mydataset,index=["x","y","z"])

data.loc[:,"address"]= address

print(data)

'''import pandas as pd
data=[1, 2 ,3 ]
d=pd.Series(data,index=["day1","day2","day3"])
print(d)'''
