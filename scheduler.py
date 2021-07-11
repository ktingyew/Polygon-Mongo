from controllers.unixtime import get_time_NY, get_time_SG, fmt
from controllers.ticker import Ticker

from apscheduler.schedulers.background import BlockingScheduler

print(f"Current time SG: {get_time_SG()}")
print(f"Current time NY: {get_time_NY()}")

tkr = Ticker('AAPL')

def main_job():
    now = get_time_NY().strftime(fmt)
    now_sg = get_time_SG().strftime(fmt)
    tkr.send_polygon_to_mongo()
    print(f"Job done at SG time: {now_sg}. NY time: {now}")
    
sched = BlockingScheduler(timezone="America/New_York")                      
# sched.add_job(main_job, trigger='cron', day_of_week='mon,tue,wed,thu,fri', hour='9-16', minute='1')
sched.add_job(main_job, trigger='cron',  hour='*', minute='59')
sched.start()

"""
DST is active in US from:
Second Sunday of March and ends on the first Sunday of November.
"""