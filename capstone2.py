import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv(r"C:\Users\HP\Desktop\online_retail_II.csv")
print(df.tail())
print(df.info())
print(df.shape)

print(df.isnull().sum())
df.columns=df.columns.str.lower().str.replace(" ","_")
df["description"]=df["description"].fillna("unknown product")
registered_df=df[df["customer_id"].notna()].copy()
unregistered_df=df[df["customer_id"].isna()]
# registered_df.to_csv("registered_customers.csv", index=False)
# unregistered_df.to_csv("unregistered_customers.csv", index=False)

df['invoice_date'] = pd.to_datetime(df['invoicedate'])

df['year'] = df['invoice_date'].dt.year
df['month'] = df['invoice_date'].dt.month
df['day'] = df['invoice_date'].dt.day
df['weekday'] = df['invoice_date'].dt.day_name()
df['hour'] = df['invoice_date'].dt.hour


df['total_amount'] = df['quantity'] * df['price']
registered_df['total_amount'] = (registered_df['quantity'] * registered_df['price'])

customer_summary = (
    registered_df
    .groupby('customer_id')
    .agg(
        total_revenue=('total_amount', 'sum'),
        total_orders=('invoice', 'nunique'),
        last_purchase=('invoicedate', 'max')
    )
    .reset_index()
)
print(customer_summary)

registered_df['invoicedate'] = pd.to_datetime(registered_df['invoicedate'])
customer_summary['last_purchase'] = pd.to_datetime(customer_summary['last_purchase'])


customer_summary['recency_days'] = (
    registered_df['invoicedate'].max() - customer_summary['last_purchase']
).dt.days

print(df)
registered_df.to_csv("registered_customers.csv", index=False)
unregistered_df.to_csv("unregistered_customers.csv", index=False)
from sqlalchemy import create_engine
from urllib.parse import quote_plus

username = "root"
password = quote_plus("kashdata17@")
host = "127.0.0.1"
port = "3306"
database = "retail"

engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
)

# test connection
engine.connect()
print("Connected successfully!")

table_name = "invoice"   # choose any table name
df.to_sql(table_name, engine, if_exists="replace", index=False)