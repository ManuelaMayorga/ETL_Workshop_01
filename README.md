# Workshop_01 - ETL
Autor: [@ManuelaMayorga](https://github.com/ManuelaMayorga)

## Welcome

The beginning of this work consisted of the analysis and manipulation of data contained in a CSV file with 50,000 rows of randomly generated information on participants in selection processes. Throughout this process, specific technologies were used in the work instructions, including:  
- _Python_ <img src="https://cdn-icons-png.flaticon.com/128/3098/3098090.png" alt="Python" width="21px" height="21px"> 
- _Jupyter Notebook_  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Jupyter_logo.svg/883px-Jupyter_logo.svg.png" alt="Jupyer" width="21px" height="21px">
- _PostgreSQL_ as the relational database management system (this was chosen by personal preference). <img src="https://cdn-icons-png.flaticon.com/128/5968/5968342.png" alt="Postgres" width="21px" height="21px">


## Objectives:

1. Migrate data from CSV file to PostgresQL database using SQLAlchemy.
2. Analyze and manipulate the data stored in the database.
3. Visualizations in Power BI:  
  - Hires by technology.
  - Hires by year.
  - Hires by seniority (level of experience).
  - Hires by country over years

## Description of `candidates.csv` file columns

50,000 rows and 10 columns, take into account that is randomly generated information

- First Name - Object
- Last Name - Object
- Email - Object
- Country - Object
- Application Date - Object
- Yoe (Years Of Experience) - Integer
- Seniority - Object
- Technology - Object
- Code Challenge Score - Integer
- Technical Interview - Integer

## How to run this project

First of all here is the requierements

Install Python : [Python Downloads](https://www.python.org/downloads/)  
Install PostgreSQL : [PostgreSQL Downloads](https://www.postgresql.org/download/)  
Instsll PowerBI : [PowerBi](https://powerbi.microsoft.com/en-us/downloads/)

1. Clone this repository:
   ```bash
   https://github.com/ManuelaMayorga/ETL_Workshop_01.git
   ```
2. Go to the project directory  
   ```bash
   cd ETL_Workshop_01
   ```
3. Create a virtual enviroment  
  ```bash
  python -m venv venv
  ```
4. Start the virtual enviroment  
  ```bash  
  ./venv/Scripts/activate
  ```
5. Create into src/database a json file named `db_settings.json` and add the following keys to the file:  
   ```json
   {
    "user": "Your PostgreSQL database username."
    "password": "Your PostgreSQL database password."
    "host": "The host address or IP where your PostgreSQL database is running."
    "port": "The port on which PostgreSQL is listening."
    "database": "The name of your PostgreSQL database."
   }
    ```
6. Create a .env file and add this variable:  
   WORK_PATH <- Sets the working directory for the application, indicating the base path for performing operations and managing files.

7. Create a database in PostgreSQL (Make sure is the same name as your 'database' name in the json file)

8. Start browsing the notebooks:
- 01_load_data
- 02_Candidates_EDA
- 03_load_newdata
- 04_HiredCandidate_EDA

9. Go to powerBi and follow this steps:
Step 1: Launch Power BI Desktop.  
![image](https://github.com/ManuelaMayorga/ETL_Workshop_01/assets/111150858/b25c1326-92b3-4e16-9d67-986440b1d305)

Step 2: In the dialogue box, under the database option, select ‘PostgreSQL database’ and click ‘Connect.’  
![image](https://github.com/ManuelaMayorga/ETL_Workshop_01/assets/111150858/06c29b36-a1bd-47ce-8db6-1650c94fc21c)

Step 3: In the following dialogue box, enter the server IP address and database name. 
![image](https://github.com/ManuelaMayorga/ETL_Workshop_01/assets/111150858/16637fec-c01b-4580-8971-309e1ae04a93)

Step 4: Enter your username and password in the following dialogue box and click Connect.  
![image](https://github.com/ManuelaMayorga/ETL_Workshop_01/assets/111150858/9631db07-0baa-4220-9af8-0242dca0a782)

Step 5: In the navigator window, select the data that you require

**You can see my dashboard [here]()**


## Thank you for visiting this repository, remember to rate if it was helpful

