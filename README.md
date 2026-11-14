# Lab overview
## What  is this lab?
This lab focused on basic object-oriented data processing in Python, demonstrating how. to load table data from a `.csv` file into a memory and preform simple data analysis operation without using externalm data libraries like pandas.
## Project Structure
* `Cities.csv`: a dataset containing city, country, latitude, longitude, temperature.
* `data_processing_lab.py`: The main Python script containing the `DataLoader` and the `Table` class, along with example code that analyze the city dataset

## DataLoader Class
Located in `data_processing_lab.py`, the `DataLoader` class includes:
### Attribute
* `Base_path` (pathname): The directory path where the `.csv` file are located.
### Method
* `load_csv` (filename): Read the specified `.csv` file from `Base_path` and return as a list of dictionaries.

## Table Class
also located in `data_processing_lab.py`, the `Table` class includes:
### Attribute
* `name` (str): The name identifier for the table (e.g., `'cities'`)
* `table` (list): list of dictionaries of the `.csv` file , representing the rows and columns of the dataset
### Method
* `filter(condition)`: filter the wanted value in the `table`
* `aggregate(function, column)`:  analyze and calculate from the specified `column` and applied an aggregation `function` to the resulting list or value

## How to test and run your code
1. Ensure that both `data_processing.py` and `Cities.csv` are located in the same directory.
2. Open a terminal or command prompt and navigate to the project directory.
3. Run the script using Python 3:
   ```bash
   python3 data_processing.py

