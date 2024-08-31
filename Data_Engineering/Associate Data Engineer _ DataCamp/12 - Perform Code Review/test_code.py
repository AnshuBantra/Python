import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def prepare_smartphone_data(file_path):
    """
    To prepare the smartphone data for visualization, a number of transformations
    will be applied after reading in the raw DataFrame to memory, including:
        - reducing the number of columns to only those needed for later analysis
        - removing records without a battery_capacity value
        - divide the price column by 100 to find the dollar amount

    :param file_path: the file path where the raw smartphone data is stored
    :return: a cleaned dataset having had the operations above applied to it
    """

    if os.path.exists(file_path):
        rawData = pd.read_csv(file_path)
        print(rawData.head())  # TODO: Use this for checking out the dataset, remove before submission
    else:
        raise Exception(f"File containing smartphone data not found at path {file_path}")

    columns_to_keep_in_clean_data = [
        "brand_name",
        "os",
        "price",
        "avg_rating",
        "processor_speed",
        "battery_capacity",
        "screen_size"
    ]
    trimmedData = rawData.loc[:, columns_to_keep_in_clean_data]
    
    # Remove records without a battery_capacity value
    reducedData = trimmedData.dropna(subset = ["battery_capacity", "os"])
    
    
    
    # Divide the price column by 100 to find the dollar amount
    reducedData["price"]=reducedData["price"]/ 100
    
    return reducedData


# Call the function
cleaned_data = prepare_smartphone_data("./data/smartphones.csv")
