import pandas as pd
import json
from datetime import datetime


def process_date(date_string):
    try:
        date_object = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S.%fZ")
        formatted_date_string = date_object.strftime("%Y-%m-%d %H:%M:%S")
        return formatted_date_string
    except Exception as e:
        return date_string


def group_sales(data_frame):
    #data_frame = data_frame.dropna()
    data_frame["OrderDate"] = data_frame["OrderDate"].apply(process_date)
    data_frame['Sales'] = data_frame['Sales'].astype(int)
    grouped_data = data_frame.groupby("OrderDate")["Sales"].sum().reset_index()
    data = {
        "dates": grouped_data["OrderDate"].to_list(),
        "sales": grouped_data["Sales"].to_list(),
    }
    return data


def group_profit(data_frame):
    #data_frame = data_frame.dropna()
    data_frame["OrderDate"] = data_frame["OrderDate"].apply(process_date)
    data_frame['Profit'] = data_frame['Profit'].astype(int)
    grouped_data = data_frame.groupby("OrderDate")["Profit"].sum().reset_index()
    data = {
        "dates": grouped_data["OrderDate"].to_list(),
        "profit": grouped_data["Profit"].to_list(),
    }
    return data


def group_segment(data_frame):
    #data_frame = data_frame.dropna()
    data_frame['Sales'] = data_frame['Sales'].astype(int)
    grouped_data = data_frame.groupby("Segment")["Sales"].sum().reset_index()
    data = {
        "segment": grouped_data["Segment"].to_list(),
        "sales": grouped_data["Sales"].to_list(),
    }
    return data


def group_cities(data_frame):
    #data_frame = data_frame.dropna()
    data_frame['Sales'] = data_frame['Sales'].astype(int)
    grouped_data = data_frame.groupby("City")["Sales"].sum().reset_index()
    data = {
        "cities": grouped_data["City"].to_list(),
        "sales": grouped_data["Sales"].to_list(),
    }
    return data


def group_category(data_frame):
    #data_frame = data_frame.dropna()
    data_frame['Sales'] = data_frame['Sales'].astype(int)
    grouped_data = data_frame.groupby("Category")["Sales"].sum().reset_index()
    data = {
        "categories": grouped_data["Category"].to_list(),
        "sales": grouped_data["Sales"].to_list(),
    }
    return data


def group_sub_category(data_frame):
    #data_frame = data_frame.dropna()
    data_frame['Sales'] = data_frame['Sales'].astype(int)
    grouped_data = data_frame.groupby("Sub_Category")["Sales"].sum().reset_index()
    data = {
        "sub_categories": grouped_data["Sub_Category"].to_list(),
        "sales": grouped_data["Sales"].to_list(),
    }
    return data


def group_country(data_frame):
    #data_frame = data_frame.dropna()
    data_frame['Sales'] = data_frame['Sales'].astype(int)
    grouped_data = data_frame.groupby("Country")["Sales"].sum().reset_index()
    data = {
        "countries": grouped_data["Country"].to_list(),
        "sales": grouped_data["Sales"].to_list(),
    }
    return data


def group_product(data_frame):
    #data_frame = data_frame.dropna()
    data_frame['Sales'] = data_frame['Sales'].astype(int)
    grouped_data = data_frame.groupby("ProductName")["Sales"].sum().reset_index()
    data = {
        "products": grouped_data["ProductName"].to_list(),
        "sales": grouped_data["Sales"].to_list(),
    }
    return data
