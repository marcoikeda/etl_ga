import pandas as pd
from google2pandas import *

def get_sessions():
	conn = GoogleAnalyticsQuery(secrets='C:/Users/marcoikeda/Downloads/client_secrets.json', token_file_name='C:/Users/marcoikeda/Downloads/analytics.dat')	
	query = {\
	   'ids'           : 109089804,
	   'metrics'       : ['pageviews'],
	   'dimensions'    : ['dimension2', 'dimension3', 'medium', 'source', 'date', 'dateHour'],
	   'start_date'    : '7daysAgo',
	   'max_results'   : 1000
	}
	df, metadata = conn.execute_query(**query)
	return df

df = get_sessions()
