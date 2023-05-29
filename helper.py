import pandas as pd

def descriptive_stats(data, folder_desc, main_name):
#Code for descriptive stats
    cols = list(data.columns)
    cols.remove("Country")
    cols.remove("Year")

    countries = (data["Country"].unique())
    fin = pd.DataFrame({"index":['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max']})
    overall = pd.DataFrame(index=countries, columns=cols)
    for state in countries:
        for col in cols:
            fin = fin.merge(data[data["Country"] ==state][col].describe().reset_index(), on=["index"])
            overall[col].loc[state] = data[data["Country"] ==state][col].mean()
            print(fin)
        fin["Country"] = state
        fin.to_excel("./" + folder_desc +"/"+state+"_descriptive_ind.xlsx")
        fin = pd.DataFrame({"index":['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max']})
    overall.to_excel(main_name + ".xlsx")
    
def generate_growth_data(data, year_start, year_finish):
    countries = list(data["Country"].unique())
    #countries.remove("Turkey")
    #countries.remove("Norway")
    columns = list(data.columns)
    columns.remove("Year")
    columns.remove("GDP")
    columns.remove("Country")

    result = pd.DataFrame()

    for country in countries:
        df = data[(data["Country"] == country) & (data["Year"] >=year_start)& (data["Year"] <=year_finish)]
        for column in columns:
            df[column] = df[column] * 0.01 * df["GDP"]
            df[column] = (df[column] - df[column].shift(1))/df[column].shift(1)
            
        df["GDP"] = (df["GDP"] - df["GDP"].shift(1))/df["GDP"].shift(1)
        result = pd.concat([result, df])
    return result
        

def generate_actual_data(data, year_start, year_finish):
    countries = list(data["Country"].unique())
    #countries.remove("Turkey")
    #countries.remove("Norway")
    columns = list(data.columns)
    columns.remove("Year")
    columns.remove("GDP")
    columns.remove("Country")

    result = pd.DataFrame()
    for country in countries:
        df = data[(data["Country"] == country) & (data["Year"] >=year_start)& (data["Year"] <=year_finish)]
        for column in columns:
            df[column] = df[column] * 0.01 * df["GDP"]
        result = pd.concat([result, df])
    return result

def save_by_country(folder, data, tag):
    countries = (data["Country"].unique())
    for country in countries:
        data[data["Country"] == country].to_excel(f"./{folder}/{country}({tag}).xlsx")

