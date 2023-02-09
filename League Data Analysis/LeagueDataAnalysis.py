import pandas as pd
pd.set_option("display.max_rows", None, "display.max_columns", 8)
pd.set_option('display.expand_frame_repr', False)
data = pd.read_csv('leagueData.csv')
sorted = data.sort_values("Name", ascending=False)
#print(data.loc[:, ["Name", "ID"]].query('Name == "Bel\'Veth"'))
#print(data['Range'].mean())
#print(data.loc['ID'].query('ID' == "13"))

#Keep this as reference to how to do apostraphe names
print(data.query('Name == "Rek\'Sai"'))