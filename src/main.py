from solrwatch import *
import schedule
import time

def job():
    solrwatch = SolrWatch()
    solrwatch.run()
    
schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
