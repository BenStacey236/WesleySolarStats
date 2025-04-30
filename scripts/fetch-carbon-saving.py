import os
import json

from SolarAPI import *

if __name__ == "__main__":
    API_KEY = os.getenv('API_KEY')
    DEVICE_SERIAL_NUMBER = os.getenv('DEVICE_SERIAL_NUMBER')

    connection = configure_connection(API_KEY, DEVICE_SERIAL_NUMBER)

    try:
        carbonSaving = {"carbon-savings": connection.get_generation()['cumulative']}

        jsonString: str = json.dumps(carbonSaving, indent=4, ensure_ascii=False)
        
        with open(f'data/carbon-savings.json', 'w') as file:
            file.write(jsonString)

        print(f'Carbon savings successfully written to details/carbon-savings.json')

    except Exception as e:
        print(f"Error writing JSON to file: {e}")