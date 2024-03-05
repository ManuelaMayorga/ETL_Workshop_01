from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
import json
import os

def config_loader():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'db_settings.json')

    try:
        with open(file_path) as f:
            parameters = json.load(f)

        url = f"postgresql://{parameters['user']}:{parameters['password']}@{parameters['host']}:{parameters['port']}/{parameters['database']}"
        engine = create_engine(url)
        print(f'Connected successfully to {parameters["database"]} database')
        return engine

    except FileNotFoundError:
        print(f'Error: File not found at path {file_path}')
        return None  
    
    except SQLAlchemyError as e:
        print(f'Error: {e}')
        return None  

    