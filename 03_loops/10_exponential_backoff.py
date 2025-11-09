"""
10. Exponential Backoff - it is used in Password reset and also otp sending time
Problem: Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries.

"""


import time

max_retries = 5
attempt=0
wait_time = 1

while attempt<max_retries:
    print("Attempt", attempt + 1, "- wait time", wait_time, )
    time.sleep(wait_time)
    wait_time*=2
    attempt+=1