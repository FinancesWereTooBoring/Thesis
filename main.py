import pandas as pd
from functools import reduce
from DataCreation import DataCreation
from helper import descriptive_stats, generate_growth_data, generate_actual_data, save_by_country
base_fp = "./data/"
exm = DataCreation(base_fp)
exm.compose_df()
tb= exm.final_db

descriptive_stats(generate_actual_data(tb,1996, 2019), "descriptive_ind", "Means(actual)")