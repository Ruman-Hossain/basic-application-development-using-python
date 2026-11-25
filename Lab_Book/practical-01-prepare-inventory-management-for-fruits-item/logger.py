import datetime

def record_job(log_filename="job_log.txt", job_description=""):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(log_filename, 'a') as logfile:
        logfile.write(f"[{timestamp}] {job_description}\n")