import pandas as pd

data= {
    'Name':['Wodden Sword','Summebrander','silver sword'],
    'Price':['200','1000000000000000000000000000000000000000000000000000000000000000000000000','3000'],
    'Quantity':['100','1','345']
}
print(pd.DataFrame(data))