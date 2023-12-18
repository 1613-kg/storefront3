from time import sleep
from celery import shared_task
@shared_task
def notify_customer(message):
    print("sending 10k")
    print(message)
    print(10)
    print("sent")
