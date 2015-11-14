import os, datetime

# severity: 0 - Info, 1 - Warning, 2 - Error
def AddMessage(severity,message):
	sd = {0: 'Info', 1: 'Warning', 2: 'Error'}
	print "{0} at {1}: {2}".format(sd[severity],datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S'),message)
