import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk

sns.set_theme(style="darkgrid")

url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
df = pd.read_csv(url)

df["date"] = pd.to_datetime(df["date"])

def covid_analysis(country):
    df_country = df[df["location"] == country]
    df_latest = df_country[df_country["date"] == "2023-08-30"]

    plt.figure(figsize=(8,6))
    plt.bar(x=df_latest["location"], height=df_latest["total_cases_per_million"], label="Total cases per million")
    plt.bar(x=df_latest["location"], height=df_latest["total_deaths_per_million"], label="Total deaths per million")
    plt.xlabel("Country")
    plt.ylabel("Cases and deaths per million")
    plt.title(f"COVID-19 cases and deaths per million for {country} as of August 30, 2023")
    plt.legend()
    plt.show()

    df_country = df_country[(df_country["date"] >= "2020-01-01") & (df_country["date"] <= "2023-08-30")]

    plt.figure(figsize=(12,8))
    plt.plot(df_country["date"], df_country["new_cases_smoothed"], label="Daily new cases (smoothed)")
    plt.plot(df_country["date"], df_country["new_deaths_smoothed"], label="Daily new deaths (smoothed)")
    plt.xlabel("Date")
    plt.ylabel("Cases and deaths")
    plt.title(f"COVID-19 daily new cases and deaths for {country} from January 1, 2020 to August 30, 2023")
    plt.legend()
    plt.show()

def show_graphs():
    country = combo.get()
    
    covid_analysis(country)

window = tk.Tk()

window.title("COVID-19 Data Analysis")

window.geometry("400x200")

label = tk.Label(window, text="Select a country to see the COVID-19 graphs:")

label.grid(row=0, column=0, padx=10, pady=10)

countries = list(df["location"].unique())

combo = ttk.Combobox(window, values=countries)

combo.grid(row=1, column=0, padx=10, pady=10)

button = tk.Button(window, text="Show graphs", command=show_graphs)

button.grid(row=2, column=0, padx=10, pady=10)

window.mainloop()