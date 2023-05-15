import pandas as pd
from functools import reduce
from DataCreation import DataCreation

base_fp = "./data/"
exm = DataCreation(base_fp)
exm.compose_df()
tb= exm.final_db

#Code for descriptive stats
cols = list(tb.columns)
cols.remove("Country")
cols.remove("Year")

tb = tb[tb["Year"] >=2004]
countries=exm.my_countries
fin = pd.DataFrame({"index":['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max']})
overall = pd.DataFrame(index=countries, columns=cols)
for state in countries:
    for col in cols:
        fin = fin.merge(tb[tb["Country"] ==state][col].describe().reset_index(), on=["index"])
        overall[col].loc[state] = tb[tb["Country"] ==state][col].mean()
        print(fin)
    fin["Country"] = state 
    fin.to_excel("./descriptive_ind/"+state+"_descriptive_ind.xlsx")
    fin = pd.DataFrame({"index":['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max']})
overall.to_excel("All_the_means.xlsx")
        
