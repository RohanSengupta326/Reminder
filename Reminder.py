import time 
from plyer import notification

if __name__ == '__main__':
    while True:
        notification.notify(
            title = "Bullshit Reminder",
            message = "I have nothing to say , just a bullshit reminder program",
            timeout=10
        )
        time.sleep(60*60)