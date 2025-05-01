import subprocess
import time
import logging
import os
from dotenv import load_dotenv

load_dotenv() # Load environmePATHnt variables from the .env file

PATH = os.getenv('APP_PATH')
WAIT = 3 # Secondi attesa
FILES = [PATH+'getwebpage.py', PATH+'searchkeywords.py', PATH+'send2email.py'] # Lista dei file da eseguire

# Configure logging
logging.basicConfig(filename=PATH+'application.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run_scripts(files, wait):
    for file in FILES:
        try:
            # Esegui il file
            subprocess.run(['python3', file], check=True)
            
            logging.info(f'Successfully ran {file}')
            
            # Attendi x secondi
            time.sleep(WAIT)
        except subprocess.CalledProcessError as e:
            logging.error(f'Error running {file}: {e}')
    logging.info('--------------')

if __name__ == "__main__":
    run_scripts(FILES, WAIT)
