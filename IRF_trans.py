import pandas as pd

countries = ["Denmark", "Norway", "Poland", "Turkey"]
result = pd.DataFrame()

for country in countries:
    data = pd.read_excel("Tables for graphs(IRF).xlsx", sheet_name=country)
    cols = list(data.columns)
    outcome = pd.DataFrame(index = list(range(10)))
    cols.remove("Period")
    for col in cols:
        var = data[col]
        var_diff1 = var[1::2].reset_index().drop(columns=["index"])
        var_diff1 = var_diff1.rename(columns={col:f"{col}Diff1"})
        var_diff2 = var_diff1
        var_diff2= var_diff2.rename(columns={f"{col}Diff1":f"{col}Diff2"})
        var_fin = var[0::2].reset_index().drop(columns=["index"])
        var_fin = var_fin.rename(columns={col:f"{col}Fin"})
        var_high, var_low = var_fin[f"{col}Fin"]-var_diff1[f"{col}Diff1"], var_fin[f"{col}Fin"]+var_diff1[f"{col}Diff1"]
        var_high = var_high = var_high.reset_index().drop(columns=["index"])
        var_high = var_high.rename(columns={0:f"{col}High"})
        var_low = var_low.reset_index().drop(columns=["index"])
        var_low = var_low.rename(columns={0:f"{col}Low"})
        var_val=var_high
        var_val = var_val.rename(columns={f"{col}High":f"{col}Val"})
        df = pd.concat([var_fin, var_high, var_val, var_diff1, var_diff2], axis=1)
        outcome = pd.concat([outcome, df], axis=1)
        var, var_fin, var_diff1, var_diff2, var_high, var_low, var_val = None, None, None, None, None, None, None
    print(country)
    outcome.to_excel(f"./IRFS/{country}.xlsx")
