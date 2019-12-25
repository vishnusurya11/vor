"""Main Program"""

# Libraries
import time
import logging
import pandas as pd
import datetime 
import pandas_datareader as web
import vor_class_variables 


def vor():
    """ Main function that calls other functions to collect data and write
    to a given location
    """
    try:
        folder_check()
        #get_stock_data()
        ticker_list = get_list_of_tickers('process_log.csv')
        ticker_status_check(ticker_list)
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
    try:
        start = datetime.datetime(1970,1,1)
        pan = web.get_data_yahoo('STZ.B',start)
        pan.to_csv('STZ.B.csv')
    except Exception as e:
        print(e)
    return True

def get_list_of_tickers(filename):
    try:
        process_log_df = pd.read_csv(filename)
        return list(process_log_df.Symbol)
    except Exception as e:
        logging.exception(e)

def ticker_status_check(ticker_list):
    try:
        ticker_obj = vor_class_variables.ProcessLogEntry()
        for ticker in ticker_list:
            for i,j in get_ticker_record(ticker): 
                setattr(ticker_obj,i.lower(), j)
            decision_maker(ticker_obj)
    except Exception as e:
        print(e)
        logging.exception(e)
    return True

def get_ticker_record(ticker):
    try:
        process_log_df = pd.read_csv('process_log.csv')
        a = process_log_df[process_log_df.Symbol == ticker]
        return zip(list(a.columns),a.values.tolist()[0])
    except Exception as e:
        print(e)
        logging.exception(e)
    return True

def decision_maker(ticker_obj):
    try:
        print(ticker_obj)
        return True
    except Exception as e:
        print(e)
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
