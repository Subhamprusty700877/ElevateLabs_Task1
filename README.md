# ElevateLabs_Task1
DATA ANALYST INTERNSHIP TASK 1

Task Description:

The goal was to take a raw dataset and clean it up so that it's ready for analysis. 

Dataset Used:

I used the Customer Personality Analysis dataset from Kaggle. It contains marketing campaign data from a company, including details like age, education, income, and customer behavior.

Tools I Used:
Python,
Pandas (for data handling),
VS Code (for writing and testing the code).

Steps I Did :
Loaded the dataset using Pandas.
Checked for missing values – found some in the Income column and filled them using the median.
Removed duplicate rows to avoid repeated entries.
Cleaned up text fields like Education and Marital_Status – made all entries lowercase and removed extra spaces for consistency.
Converted date columns to a proper date format so they can be used in time-based analysis later
(like Dt_Customer).
Renamed all column headers to make them easy to read and consistent (used lowercase letters and underscores instead of spaces).
Changed data types where needed – for example, converted Income to an integer.
Saved the final cleaned dataset as a new CSV file called cleaned_dataset.csv.

Things I Learned:
How to handle missing and duplicate data
How to clean and format text and date fields
Why clean data is so important before doing any analysis or visualization
How to use Pandas efficiently for basic data cleaning tasks
