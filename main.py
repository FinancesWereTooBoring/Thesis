import pandas as pd
from functools import reduce
from DataCreation import DataCreation

base_fp = "./data/"
exm = DataCreation(base_fp)
exm.compose_df()
exm.final_db