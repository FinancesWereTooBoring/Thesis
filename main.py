import pandas as pd
from functools import reduce
from DataCreation import DataCreation
from descriptive import descriptive_stats
base_fp = "./data/"
exm = DataCreation(base_fp)
exm.compose_df()
tb= exm.final_db

#descriptive_stats(data=exm, folder_desc="descriptive_ind", main_name="All_the_means")
        
countries = list(tb["Country"].unique())
columns = list(tb.columns)
columns.remove("Year").remove("GDP")

for country in countries:
    df = tb[(tb["Country"] == country) & (tb["Year"] >=1999)& (tb["Year"] <=2020)]
    for column in columns:
        df[column] = df[column] * 0.01 * df["GDP"]
        
    
    df.to_excel("./output/"+country+"(fin).xlsx")