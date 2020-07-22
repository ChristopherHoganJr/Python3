from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import json
import time

# Enter your Mac username here
userName = '' 

folder_to_track = '/Users/'+userName+'/Downloads/'
jpg_destination = '/Users/'+userName+'/Documents/downloadedJPG/'
dmg_destination = '/Users/'+userName+'/Documents/downloadedDMG/'
pdf_destination = '/Users/'+userName+'/Documents/downloadedPDF/'
zip_destination = '/Users/'+userName+'/Documents/downloadedZIP/'
txt_destination = '/Users/'+userName+'/Documents/downloadedTXT/'

class MyHandler(FileSystemEventHandler):
    if not os.path.isdir(jpg_destination) == True:
        os.mkdir(jpg_destination)
    if not os.path.isdir(dmg_destination) == True:
        os.mkdir(dmg_destination)
    if not os.path.isdir(pdf_destination) == True:
        os.mkdir(pdf_destination)
    if not os.path.isdir(zip_destination) == True:
        os.mkdir(zip_destination)
    if not os.path.isdir(txt_destination) == True:
        os.mkdir(txt_destination)

    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            if filename.endswith('.txt'):
                if not filename in os.listdir(txt_destination):
                    os.rename(folder_to_track+filename, txt_destination+filename)
            elif filename.endswith('.jpg'):
                if not filename in os.listdir(jpg_destination):
                    os.rename(folder_to_track+filename, jpg_destination+filename)
            elif filename.endswith('.dmg'):
                if not filename in os.listdir(dmg_destination):
                    os.rename(folder_to_track+filename, dmg_destination+filename)
            elif filename.endswith('.pdf'):
                if not filename in os.listdir(pdf_destination):
                    os.rename(folder_to_track+filename, pdf_destination+filename)
            elif filename.endswith('.zip'):
                if not filename in os.listdir(zip_destination):
                    os.rename(folder_to_track+filename, zip_destination+filename)

event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(5)
except KeyboardInterrupt:
    observer.stop()
observer.join()
