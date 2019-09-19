import sys
from time import sleep
from uuid import uuid1
import json
import logging
from datetime import datetime
from flask import Flask, request, send_file
import threading
from Scheduler import Scheduler

threads = []

app = Flask("BowlBackend")
app.config['CORS_HEADERS'] = 'Content-Type'

external_drive = ""
camera_config = []
thread_active = False

last_file_name = ""

def start_logging():
    global external_drive, last_file_name
        filename = external_drive + str()
        last_file_name = filename
        
        print("Written")
    logging.info("Write: " + filename + " at time " + str(datetime.now()))

def main():
    while True:
        if thread_active:
            data = camera_config
            switch_flag = 0
            my_schedule = Scheduler(data)
            logging.info("Loaded Scheduler")
            sleep(3)                                    
            while thread_active:
                my_schedule.update_current_time()
                slot = my_schedule.should_start()
                if switch_flag == 0:
                        logging.info("Stop: " + str(datetime.now()))
                        switch_flag = 1

def update_config():
    pass


#API SKELETON BELOW
@app.route("/OrderIn", methods=['POST', 'GET'])
def app_connect():
    global external_drive
    global camera_config
    global thread_active
    if request.method == 'POST':
        thread_active = False
        print(request.get_json())
        camera_config = request.get_json()
        external_drive = "/media/pi/" + sys.argv[1]
        thread_active = True
    else:
        return "Unsupported"

@app.route("/viewConfig", methods=['GET'])
def returnConfig():
    if request.method == 'GET':
        return backend_config.json

def start_api_server():
    app.run("0.0.0.0", 8000)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <external drive name>")
        exit(0)
    api_thread = threading.Thread(target=start_api_server)
    main_thread = threading.Thread(target=main)
    api_thread.start()
    main_thread.start()
    main_thread.join()
    api_thread.join()
    logging.info("Program is shutting down")
