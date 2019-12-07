"""Main Program"""

# Libraries
import time
import logging

# Logging
logging.basicConfig(
    filename='vor_error.log',
    level=logging.INFO,
    format='[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S %Z'
)

if __name__ == '__main__':
    try:
        time.sleep(10)
        print("Hello")
    except KeyboardInterrupt:
        print("vor is terminated")
