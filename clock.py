from apscheduler.schedulers.blocking import BlockingScheduler
import main

sched = BlockingScheduler()

@sched.scheduled_job('interval', hours = 2)
def timed_job():
    main.main()

sched.start()
