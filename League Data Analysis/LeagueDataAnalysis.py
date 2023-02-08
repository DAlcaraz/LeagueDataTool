import pandas as pd
pd.set_option("display.max_rows", None, "display.max_columns", 8)
pd.set_option('display.expand_frame_repr', False)
data = pd.read_csv(r'C:\Users\mda03\OneDrive\Documents\Data\leagueData.csv')
sorted = data.sort_values("Range", ascending=False)
#print(data.loc[:, ["Name", "ID"]].query("`ID` == 102"))
#print(data['Range'].mean())