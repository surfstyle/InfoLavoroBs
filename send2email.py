import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging
import os
from dotenv import load_dotenv

load_dotenv() # Load environmePATHnt variables from the .env file

PATH = os.getenv('APP_PATH')
FILE_NAME = os.getenv('APP_FILE_OUTPUT')
FILE_PATH = PATH + FILE_NAME
URL = os.getenv('APP_URL')

# Configure logging
logging.basicConfig(filename=PATH+'application.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

SMTP_SERVER = os.getenv('APP_SMTP_SERVER')
SMTP_PORT = os.getenv('APP_SMTP_PORT')
DESTINATARIO = os.getenv('APP_DESTINATARIO')
MITTENTE = os.getenv('APP_MITTENTE')
SOGGETTO = os.getenv('APP_SOGGETTO')
SMTP_USERNAME = os.getenv('APP_SMTP_USERNAME')
SMTP_PASSWORD = os.getenv('APP_SMTP_PASSWORD')   #App pwd generated 12/05/2024

def invia_email(destinatario, mittente, soggetto, corpo, smtp_username, smtp_password):
    msg = MIMEMultipart()
    msg['From'] = mittente
    msg['To'] = destinatario
    msg['Subject'] = soggetto
    msg.attach(MIMEText(corpo, 'plain'))

    try:
        # Connessione al server SMTP e invio del messaggio
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.send_message(msg)    
        logging.info("Email sent successfully!")
    except Exception as e:
        logging.error(f"Failed to send email: {e}")


def leggi_file_e_invia_email(file_path, destinatario, mittente, soggetto, smtp_username, smtp_password):
    try:
        # Legge il contenuto del file
        with open(file_path, 'r', encoding='utf-8') as file:
            righe = file.readlines()
        
        # Se il file contiene delle righe, invia l'email
        if righe:
            righe.append('\n------------------------------\nURL Website: \n' + URL)
            corpo = ''.join(righe)  # Unisce le righe del file in un unico corpo di email
            invia_email(destinatario, mittente, soggetto, corpo, smtp_username, smtp_password)
        else:
            logging.info("The file is empty, no email sent")
    except Exception as e:
        logging.error(f"An error occurred: {e}")    

if __name__ == "__main__":
    leggi_file_e_invia_email(FILE_PATH, DESTINATARIO, MITTENTE, SOGGETTO, SMTP_USERNAME, SMTP_PASSWORD)

