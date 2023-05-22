import pandas as pd

def descriptive_stats(data, folder_desc, main_name):
#Code for descriptive stats
    tb= data.final_db
    cols = list(tb.columns)
    cols.remove("Country")
    cols.remove("Year")

    tb = tb[tb["Year"] >=2000]
    countries=exm.my_countries
    fin = pd.DataFrame({"index":['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max']})
    overall = pd.DataFrame(index=countries, columns=cols)
    for state in countries:
        for col in cols:
            fin = fin.merge(tb[tb["Country"] ==state][col].describe().reset_index(), on=["index"])
            overall[col].loc[state] = tb[tb["Country"] ==state][col].mean()
            print(fin)
        fin["Country"] = state 
        fin.to_excel("./" + folder_desc +"/"+state+"_descriptive_ind.xlsx")
        fin = pd.DataFrame({"index":['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max']})
    overall.to_excel(main_name + ".xlsx")