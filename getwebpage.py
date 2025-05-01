from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from dotenv import load_dotenv
import logging

load_dotenv() # Load environmePATHnt variables from the .env file

PATH = os.getenv('APP_PATH')

# Configure logging
logging.basicConfig(filename=PATH+'application.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

URL = os.getenv('APP_URL')
FILE_NAME = os.getenv('APP_FILE_NAME')
FILE_PATH = PATH + FILE_NAME
RADIO_BUTTON_ID = "WizardZone_StandardWizard_ApplicationHost_ctl00_PartHost_SimplePartView_ctl00_ControlHost_ctl00_InfoSelector_EnumSelectorList_1"
RESULT_CLASS_NAME = "wizard_step_section"


def setup_driver():
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')
    # Set up the WebDriver (e.g., Chrome, Firefox)
    driver = webdriver.Firefox(options=options)
    return driver

def save_to_file(content, file_name):
    with open(file_name, 'wb') as file:
        file.write(content.encode('utf-8'))

def main():
    driver = setup_driver()
    
    try:
        # Open the web page
        driver.get(URL)
    
        # Wait for the radio buttons to be clickable and select the desired one
        radio_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, RADIO_BUTTON_ID))
        )
        radio_button.click()

        # Wait for the result page to load
        result = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, RESULT_CLASS_NAME)) #"result_element_id")) Ricerca by CLASS_NAME del div annunci
        )

        # Retrieve and process the result
        result_text = result.text
        save_to_file(result_text, FILE_PATH)
        logging.info(f"Page successfully downloaded and saved to {FILE_NAME}")
    
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        
    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    main()
