# 365 Day's of Python Coding Challenge 
# Day 128: Cloud File Sharing using Python
# Upload As many as 50 files at once

## An Improved Version of the Original.

import gofile as go

def Store_Files(file):
    cur_server = go.getServer()
    print(cur_server)
    url = go.uploadFile(file)
    if url is not None:
        print("Download Link: ", url["downloadPage"])
    else:
        print("Error: Upload failed.")

Store_Files("test.jpeg")

# rayturner.dev #clcoding.com