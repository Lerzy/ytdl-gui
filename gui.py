import PySimpleGUI as sg
import os
import sys
from downloader import Downloader

sg.theme("Black")


layout = [
    [sg.Text('Video/playlist link to download:')],
    [sg.InputText(k="-VIDEO-URL-")],
    [sg.Radio("MP4", "RADIO1", k="-MP4-", default=True)],
    [sg.Radio("MP3", "RADIO1", k="-MP3-", default=False)],
    [sg.Text("Downloads should be downloaded in 'ytdl-gui-downloads' folder")],
    [sg.Button('Download'), sg.Button('Close')],
    [sg.Output(size=(45, 3), k="-DOWNLOAD-STATUS-")]
]



window = sg.Window('youtube-dl GUI', layout)

download_folder = "ytdl-gui-downloads"

if getattr(sys, "frozen", False):
    parent_dir = os.path.dirname(sys.executable)
elif __file__:
    parent_dir = os.path.dirname(__file__)
print(parent_dir)
download_path = os.path.join(parent_dir, "ytdl-gui-downloads")


def create_folder():
    if os.path.exists(download_folder):
        return True
    else:
        try:
            os.mkdir(download_path)
            return True
        except:
            print(f"Failed to create download folder, downloads will be downloaded in {parent_dir}")
            return False

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Close': 
        break

    if event == "Download":
        folder_status = create_folder()
        Downloader(values["-VIDEO-URL-"], download_path if folder_status is True else parent_dir, "MP4" if values["-MP4-"] is True else "MP3")
        

window.close()