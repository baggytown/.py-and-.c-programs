import pandas as pd
teacher_data = {
    "Name":["Joe","Bob","Donald","Liam"],
    "Years of Teaching":[18,12,13,14],
    "Score":[10,9,7,10]
}
df= pd.DataFrame(teacher_data)
#print(df)


df = pd.DataFrame(teacher_data,index=("1","2","3","4"))
#print(df)



#print(df["Name"])



#print(df["Name"],df["Years of Teaching"])



df["Student Liking"]=[10,2,10,8]
#print(df)




df["Score"]=df["Score"]+1
#print(df)




#print(df[df["Score"]>8])





#print(df.sort_values("Score",ascending=False))






#print(df.drop("Score",axis=1))




df.info()
df.columns




df.head(2)





df.tail(2)