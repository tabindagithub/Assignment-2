#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 02:08:41 2023

@author: Tabinda
"""

import pandas as pd
import matplotlib.pyplot as plt


def get_data(url):
    data = pd.read_csv(url)
    data = data.set_index("Country Name")
    data = data.dropna()
    transposed_data = data.copy()
    transposed_data = transposed_data.drop(
        ['Indicator Name', 'Indicator Code', 'Country Code'], axis=1)
    
    transposed_data = transposed_data.T
    data_with_country_columns = transposed_data.dropna()
    
    return data, data_with_country_columns


def line_plot(data, title, xlabel, ylabel, countries):
    filterred_data = data[countries]
    plt.figure(figsize=(8,6))
    plt.plot(filterred_data.iloc[-15:])
    plt.xlabel(xlabel)
    plt.xticks(rotation=90)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend(filterred_data, bbox_to_anchor=(1.0, 1), fontsize="7", 
               loc="upper right")
    plt.show()
    

def bar_graph(data, title, xlabel, ylabel, countries):
    data = data.iloc[-10:]
    data = data[countries]
    plt.figure(figsize=(8,6))
    ax = data.plot(kind='bar')
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    plt.xticks(rotation=0)
    ax.set_ylabel(ylabel)
    plt.legend(countries, bbox_to_anchor=(1.0, 1), fontsize="7", loc="upper right")
    plt.show()


base_path = ("/Volumes/Untitled 2/ds_assignments/assignment_2/" + 
    "tabinda/")

goods_import, goods_import_2 =\
    get_data(base_path + "GoodsAndServicesImport.csv")
gdp, gdp_2 =\
    get_data(base_path + "gdp_growth.csv")
mortality_rate, mortality_rate_2 =\
    get_data(base_path + "Mortality_Rate.csv")
population_ages, population_ages_2 =\
    get_data(base_path + "PopulationAges.csv")

countries = ["China", "Sudan", "South Asia", "Ghana", "Australia",
             "Argentina", "Pakistan"]

line_plot(goods_import_2, "Imports of goods and services (% of GDP)", 
          "Year", "Imports of goods and services", countries)
line_plot(gdp_2, "GDP growth (annual %)", 
          "Year", "GDP growth (annual %)", countries)

bar_graph(population_ages_2, "Population ages 15-64 (% of total population)",
          "Year", "Population ages 15-64", countries)
countries_2 =  ["Japan", "Sudan", "United States", "Ghana", "Australia",
             "India", "Pakistan"]
bar_graph(mortality_rate_2, "Mortality rate, under-5 (per 1,000 live births)",
          "Year", "Mortality rate, under-5", countries_2)



