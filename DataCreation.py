import pandas as pd
from functools import reduce

class DataCreation:
    def __init__(self, path):
        self.path = path
        self.my_countries = ["Norway", "Denmark", "Poland", "Hungary", "Turkey", "Greece"]
        self.unwanted = ["Country", 'Country Code', 'Indicator Name', 'Indicator Code']
        self.tax = ""
        self.social = ""
        self.moneysup = ""
        self.military = ""
        self.gdp = ""
        self.debt = ""
        self.final_db = ""
        
    def create_by_source(self):
        self.debt = pd.read_excel(self.path+"Debt(all).xls")
        self.debt["Country"] = self.debt["Country"].replace("Türkiye, Republic of", "Turkey")
        years = list(self.debt.columns)
        years.remove("Country")
        self.debt = self.debt.melt(id_vars="Country", value_vars=years, var_name="Year", value_name="Debt")
        self.debt.Year = pd.to_numeric(self.debt.Year)
        self.debt.Debt = self.debt.Debt.replace("None", None)
        self.debt.Debt = pd.to_numeric(self.debt.Debt)

        self.gdp = pd.read_excel(self.path+"GDP(all).xls")
        self.gdp["Country"] = self.gdp["Country Name"].replace("Turkiye", "Turkey")
        self.gdp = self.gdp.drop(columns=["Country Name"])
        self.gdp = self.gdp[self.gdp["Country"].isin(self.my_countries)]
        years = list(self.gdp.columns)
        new_years = [x for x in years if x not in self.unwanted]
        self.gdp = self.gdp.melt(id_vars="Country", value_vars=new_years, var_name="Year", value_name="GDP")
        self.gdp.Year = pd.to_numeric(self.gdp.Year)
        self.gdp.GDP = pd.to_numeric(self.gdp.GDP)

        self.military = pd.read_excel(self.path+"MilitarySpendings(all).xls")
        self.military["Country"] = self.military["Country Name"].replace("Turkiye", "Turkey")
        self.military = self.military.drop(columns=["Country Name"])
        self.military = self.military[self.military["Country"].isin(self.my_countries)]
        years = list(self.military.columns)
        new_years = [x for x in years if x not in self.unwanted]
        self.military = self.military.melt(id_vars="Country", value_vars=new_years, var_name="Year", value_name="Military")
        self.military.Year = pd.to_numeric(self.military.Year)
        self.military.Military = pd.to_numeric(self.military.Military)
        

        self.social = pd.read_excel(self.path+"SocialSpending(all).xls")
        self.social["Country"] = self.social["Country"].replace("Türkiye, Republic of", "Turkey")
        years = list(self.social.columns)
        new_years = [x for x in years if x not in self.unwanted]
        self.social = self.social.melt(id_vars="Country", value_vars=new_years, var_name="Year", value_name="Social")
        self.social.Year = pd.to_numeric(self.social.Year)
        self.social.Social = self.social.Social.replace("None", None)
        self.social.Social = pd.to_numeric(self.social.Social)

        self.tax = pd.read_excel(self.path+"TaxRevenue(all).xls")
        self.tax["Country"] = self.tax["Country Name"].replace("Turkiye", "Turkey")
        self.tax = self.tax.drop(columns=["Country Name"])
        self.tax = self.tax[self.tax["Country"].isin(self.my_countries)]
        years = list(self.tax.columns)
        new_years = [x for x in years if x not in self.unwanted]
        self.tax = self.tax.melt(id_vars="Country", value_vars=new_years, var_name="Year", value_name="Tax")
        self.tax.Year = pd.to_numeric(self.tax.Year)
        self.tax.Tax = pd.to_numeric(self.tax.Tax)
        
        most_mon_sup = pd.read_excel(self.path+"MoneySupply(Norway, Denmark, Greece, Poland, Hungary, Turkey).xlsx")
        most_mon_sup["Country"] = most_mon_sup["Country Name"].replace("Turkiye", "Turkey")
        most_mon_sup = most_mon_sup.drop(columns=["Country Name"])
        most_mon_sup = most_mon_sup[most_mon_sup["Country"].isin(self.my_countries)]
        most_mon_sup = most_mon_sup[most_mon_sup["Country"] != "Greece"]
        most_mon_sup = most_mon_sup.melt(id_vars="Country", value_vars=[str(x) for x in list(range(1960, 2022))], var_name="Year", value_name="Broad")


        mon_sup_gr = pd.read_excel(self.path+"MoneySupply(Greece).xls")
        mon_sup_gr = mon_sup_gr.rename(columns= {"DDDI05GRA156NWDB":"Broad"})
        mon_sup_gr=  mon_sup_gr.drop(columns=["observation_date"])
        mon_sup_gr["Country"] = "Greece"

        self.mon_sup = pd.concat([most_mon_sup, mon_sup_gr])
        self.mon_sup.Year = pd.to_numeric(self.mon_sup.Year)
        self.mon_sup.Broad = pd.to_numeric(self.mon_sup.Broad)
    
    def compose_df(self):
        self.create_by_source()
        dfs=[self.social, self.debt, self.gdp, self.military, self.mon_sup, self.tax]
        self.final_db = reduce(lambda left, right: pd.merge(left, right, on=["Country", "Year"], how="left"), dfs)