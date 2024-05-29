import pandas as pd

mydataset = {
  'name': ["a", "b", "c"],
  'roll': [3, 7, 2]
}
print(mydataset[1:2])
data = pd.DataFrame(mydataset)

print(data)
