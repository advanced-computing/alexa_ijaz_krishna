# Lab 8

# Data Loading Methods

We implement 3 different methods for loading data within a DuckDB database. Each method has a unique purpose depending on the requirements of the data loading and handling process. Below is a comparison of the 3 methods 

## 1. **Truncate Load Method**

### Purpose:
This method is used when we want to replace the entire table content with a fresh dataset. All existing data is cleared

## Append Load Method

### Purpose:
This method is used when we want to add new data to an existing dataset without removing or modifying the existing records. It added new records under existing data

## Incremental Load Method

### Purpose:

This is used when we want to add new data and ensuring previous data remains untouched,this method ensures there is no duplicate data in comparison to append load method. This is best used for updating data according to dates.