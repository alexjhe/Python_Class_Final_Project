# Python Project 2
# Portion by Alexander Herring
# Foregin aid data from US AID, https://explorer.usaid.gov/data.html#tab-data-download
# GDP data from World Bank, https://data.worldbank.org/indicator/NY.GDP.MKTP.CD?view=chart


#Question 1: What are the high level U.S. foreign aid spending trends?
#Historic Trends in US Foreign Aid spending
#150 account levels compared to overall US budget
#Annual spending levels from the 150 account
#Annual spending levels by agency from 150 account
#Annual spending levels by category from 150 account
#Military vs. economic spending
#Recipient countries (ranked)


# Import packages and choose settings

import pandas as pd
import numpy as np
pd.options.display.float_format = "{:,.2f}".format
import matplotlib.pyplot as plt
plt.style.use("ggplot")

# Import the data

us_for_aid = pd.read_csv("C:\\Users\\Alex\\Desktop\\Python Project 2\\us_foreign_aid_complete.csv", index_col = False)
us_for_aid_df = pd.DataFrame(us_for_aid)
gdp_world = pd.read_csv("C:\\Users\\Alex\\Desktop\\Python Project 2\\API_NY.GDP.MKTP.CD_DS2_en_csv_v2.csv", skiprows = 4, index_col = False)
gdp_world_df = pd.DataFrame(gdp_world)
print(gdp_world_df)
gdp_world_df.head()

# Clean data

us_for_aid_df["constant_amount"] = us_for_aid_df["constant_amount"].astype(float)
us_for_aid_df["fiscal_year"] = us_for_aid_df["fiscal_year"].astype(str)
# Relabeling years coded as "1976tq" to 1976
us_for_aid_df_adj = us_for_aid_df.copy()
us_for_aid_df_adj.loc[:, "fiscal_year"].replace("1976tq", "1976", inplace=True)
us_for_aid_df_adj["fiscal_year"] = us_for_aid_df_adj["fiscal_year"].astype(int)

#gdp_world_us = pd.DataFrame(gdp_world["Country Code" == "USA"])
#gdp_world_df["Country Code"] == "USA"
gdp_us_df = gdp_world_df.loc[gdp_world_df["Country Code"].str.contains(r"USA"), ].copy()
print(gdp_us_df)

# Get summary of data
#print(us_for_aid_df_adj.head())
#print(us_for_aid_df_adj)
#us_for_aid_df_adj.fiscal_year.unique()
# Track high-level trends



# Donations Received by Region
region_const_amt = pd.DataFrame(us_for_aid_df_adj.groupby("region_name").constant_amount.sum().sort_values(ascending = False))
region_const_amt.reset_index(inplace = True)
region_const_amt.head(10)
print(region_const_amt.columns)
region_const_amt["constant_amount"]


region_const_amt.plot.bar(x = "region_name", y = "constant_amount")
plt.title("Donations Received by Region")
plt.xlabel("Region Name")
plt.xticks(rotation = 45)
plt.ylabel("Amount (Constant $)")
plt.legend("")
#plt.tick_params(labelsize=14)
ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))


ax.get_yaxis().set_major_formatter(
    matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x) * 1000, ',')))



# Donations received by country
country_const_amt = pd.DataFrame(us_for_aid_df_adj.groupby("country_name").constant_amount.sum().sort_values(ascending = False))
country_const_amt.head()


#add yoy here, useful for graph

# Donations received by year
year_const_amt = pd.DataFrame(us_for_aid_df_adj.groupby("fiscal_year").constant_amount.sum().sort_values(ascending = False))
year_const_amt.head()
year_const_amt.sort_index(inplace = True, ascending = False)
print(year_const_amt)



# Agency funding aid
agency_const_amt = pd.DataFrame(us_for_aid_df_adj.groupby("funding_agency_name").constant_amount.sum().sort_values(ascending = False))
agency_const_amt.head()
#print(agency_const_amt)


# Category of aid
aid_cat_const_amt = pd.DataFrame(us_for_aid_df_adj.groupby("assistance_category_name").constant_amount.sum().sort_values(ascending = False))
aid_cat_const_amt.head()

# Name for Aid
aid_name_const_amt = pd.DataFrame(us_for_aid_df_adj.groupby("activity_name").constant_amount.sum().sort_values(ascending = False))
aid_name_const_amt.head()

# Track transaction types
transac_type_const_amt = us_for_aid_df.groupby("transaction_type_name").constant_amount.sum().sort_values(ascending = False)
transac_type_const_amt.head()

# Graph

# Track transaction type by year
reduced_df = pd.DataFrame(us_for_aid_df_adj[["region_name", "country_name", "fiscal_year", "funding_agency_name", "assistance_category_name", "activity_name", "transaction_type_name", "constant_amount"]].copy())
print(reduced_df)

reduced_sums = us_for_aid_df.groupby(["country_name", "transaction_type_name", "fiscal_year"]).constant_amount.sum()
reduced_sums.head(20)
reduced_sums

#mon_contrib_wide = mon_contrib.pivot(index='date', columns='cand_nm', values='contb_receipt_amt')
reduced_sums.plot()


#Yoy funding 

#bar charts by country, maybe region

# us budget or gdp, and have foreign aid as a proportion - break by military and non-military (pay attention to inflation)

#size of receiving country population - world bank

#look at from standpoint of years, trend analysis (trend line) - money by year or decade, perhaps by spending level or type

#area chart - kind in plot box, area