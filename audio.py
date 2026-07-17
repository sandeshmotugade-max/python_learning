import time
import random

def stream_logs():
    logs = [701,60,50,100,55,301,40,80,904,101,66,88,132]
    while True:   
        yield random.choice(logs)
        time.sleep(1)

def filter_errors(log_streams):
    for log in log_streams:
        print("scanning...")
        if log > 100:
            yield log
            

def alert(errors_logs):
    from playsound import playsound
    for error in errors_logs:
        print("TEMERATURE IS HIGH:", error)
        playsound("C:\\Users\\Guru\Downloads\\audiofire Audio 2026-03-24 at 11.52.45 AM.mp3")

logs = stream_logs()
error = filter_errors(logs)
alert(error)