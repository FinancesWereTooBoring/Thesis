import pandas as pd
from functools import reduce
from DataCreation import DataCreation
from helper import descriptive_stats, generate_growth_data
base_fp = "./data/"
exm = DataCreation(base_fp)
exm.compose_df()
tb= exm.final_db

#descriptive_stats(data=exm, folder_desc="descriptive_ind", main_name="All_the_means")
        
generate_growth_data(tb)