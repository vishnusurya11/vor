"""Main Program"""

# Libraries
import time
import logging



def vor():
    """ Main function that calls other functions to collect data and write
    to a given location
    """
    try:
        print('Hola')
        time.sleep(10)
        folder_check()
        return True
    except Exception as e:
        logging.exception(e)
        return False

def folder_check():
    """Checks the folder structure and files required to run vor
    and creates if not available
    """
    try:
        print('folder check function ran successfully')
        return True
    except Exception as e:
        logging.exception(e)
        return False

# Logging
logging.basicConfig(
    filename='vor_error.log',
    level=logging.INFO,
    format='[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S %Z'
)

if __name__ == '__main__':
    try:
        vor()
    except KeyboardInterrupt:
        print("vor is terminated")
