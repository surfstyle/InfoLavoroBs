import logging
import os
from dotenv import load_dotenv

load_dotenv() # Load environmePATHnt variables from the .env file

PATH = os.getenv('APP_PATH')

# Configure logging
logging.basicConfig(filename=PATH+'application.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

FILE_INPUT = os.getenv('APP_FILE_NAME')
FILE_OUTPUT = os.getenv('APP_FILE_OUTPUT')
FILE_PATH_IN =  PATH + FILE_INPUT
FILE_PATH_OUT = PATH + FILE_OUTPUT
# Custom search! Lista delle parole da cercare
SEARCH_KEYWORDS = ["informat", "programmat", "develop", "sistemi", "system", "ict", "telecomu", "computer", "data scien", "helpdesk", "help-desk", "help desk", "informaz"]

def cerca_e_salva_righe(file_input, file_output, parole_da_cercare):
    # Converti tutte le parole da cercare in minuscolo
    parole_da_cercare = [parola.lower() for parola in parole_da_cercare]    
    
    try:
        # Apri il file di in&out in modalità di lettura&scrittura con codifica utf-8
        with open(file_input, 'r', encoding='utf-8') as fin, open(file_output, 'w', encoding='utf-8') as fout:            
            lines = fin.readlines() # Leggi tutte le righe dal file di input

            for i, line in enumerate(lines):
                line_lower = line.lower() # Converti la riga corrente in minuscolo

                # Controlla se una parola case-insensitive è tra quelle da cercare
                if any(parola in line_lower for parola in parole_da_cercare):
                    # Scrivi le 2 righe precedenti
                    for j in range(max(i - 2, 0), i):
                        fout.write(lines[j])
                    # Scrivi la riga corrente (contenente la parola trovata)
                    fout.write(line)
                    # Scrivi le 2 righe successive
                    for j in range(i + 1, min(i + 3, len(lines))):
                        fout.write(lines[j])
                    # Aggiungi una riga vuota come separatore
                    fout.write('\n')
            logging.info(f"Search completed successfully and saved to {FILE_OUTPUT}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")


if __name__ == "__main__":
    cerca_e_salva_righe(FILE_PATH_IN, FILE_PATH_OUT, SEARCH_KEYWORDS)
