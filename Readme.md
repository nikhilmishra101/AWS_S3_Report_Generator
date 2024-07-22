# AWS_S3_Report_Generator

- This Repository will be responsible for fetching data of all the files in the S3 and storing it in the excel and later deleting the unused data from s3


# Use Case:-

- Alot of times team stores alot of data on s3 as the part of their development process and thus it's cruical that the data which is not in used will be deleted and 
  this report generator is responsible for that only fetching infromation of different files along with their file type date created and pattern it allows user to do
  analysis on the unused data by having the option to perfrom etl operation and later user can delete the data with the help of etl operations data stored in a csv file

# Advantage of Report Generator

- It can reduce the cost significantly for generating the unused S3 Files Report every sprint which can help teams to reduce their cloud cost
- Since It has an Option to Perform ETL operations it provides flexibility to the user for deleting the certain variation of report
- Deleting Document through csv provides a controlled environment execution where user has the access of deleting which information thus it prevents the system of deleting any information which is cruicial for the user and overlooked in the general batch deletion of data

# How to Use the Repo:-

- Clone the Repository and setup a .venv environment by running setup.bat script
- Once the virtual environment is activated create a .env file and store the following credentials
- AWS Region
- AWS Access Token
- AWS Secret Key
- AWS Access Name
- After that run the get_data_s3.py file it'll fetch the data and store it in a .csv file
- If you want to do data analysis and transformation you can use the etl.py file
- Once Done With transformations it'll store the data into a csv file again
- Upon Satisfaction and Review You can run the delete_s3_csv.py file for deleting the data from s3 which is present in csv file


# Tech and Libraries used :- Python 3, Boto 3, AWS, Pandas
# Tools and Operation Strategies used :- ETL, Data Scraping, Data Warehouse, Data Management, Data Engineering 
