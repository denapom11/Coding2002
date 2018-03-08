# Import the logging module
import logging
import requests

# Specify to log to a file, specify the format for the message and the date format and the logging level
logging.basicConfig(filename='mylog.log',format='%(asctime)s %(levelname)s: %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)

# Log some messages
logging.debug('This is a debug message. You should see this in the file.')
logging.info('This is an info message. You should see this in the file.')
logging.warning('This is a warning message. You should see this in the file.')


try:
	resp = requests.get("https://thisurlwontwork.com",headers=headers,params="",verify = False)
	response_json = resp.json()
	logging.info("Status: ",resp.status_code)
except:
	logging.error("Something wrong with GET /host request!")
