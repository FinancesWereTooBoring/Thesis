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
    
def generate_growth_data(data):
    countries = list(data["Country"].unique())
    countries.remove("Turkey")
    countries.remove("Norway")
    columns = list(data.columns)
    columns.remove("Year")
    columns.remove("GDP")
    columns.remove("Country")


    for country in countries:
        df = data[(data["Country"] == country) & (data["Year"] >=1999)& (data["Year"] <=2020)]
        for column in columns:
            df[column] = df[column] * 0.01 * df["GDP"]
            df[column] = (df[column] - df[column].shift(1))/df[column].shift(1)
            
        df["GDP"] = (df["GDP"] - df["GDP"].shift(1))/df["GDP"].shift(1)
        
        df.to_excel("./output/"+country+"(growth).xlsx")