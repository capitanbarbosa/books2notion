import schedule
import books2notion
import time
import os

# Change the interval from 60 minutes to 2 minutes
schedule.every(2).minutes.do(books2notion.main)

if "API_TOKEN" in os.environ:
    while True:
        schedule.run_pending()
        time.sleep(60)
else:
    books2notion.main()
