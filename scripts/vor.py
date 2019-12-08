"""Main Program"""

# Libraries
import time
import logging
import pandas
import pandas_datareader as web


def vor():
    """ Main function that calls other functions to collect data and write
    to a given location
    """
    try:
        folder_check()
        get_stock_data()
        return True
    except Exception as e:
        logging.exception(e)
        return False

def folder_check():
    """Checks the folder structure and files required to run vor
    and creates if not available
    """
    try:
        #TODO: add the folders and files to be checked later
        return True
    except Exception as e:
        logging.exception(e)
        return False

def get_stock_data():
    """
    """
    pan = web.get_data_yahoo('MSFT', '2019-11-01', '2019-11-30', interval='v')
    pan.to_csv('GOOG_v.csv')
    return True

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
