# 365 Day's of Python Coding Challenge 
### Day 128: Cloud File Sharing using Python
### Upload As many as 50 files at once

### My Improved Version of the Original.

### Suppport Packages Required:
### pip install gofile

<!-- Adding Images Command -->
<!-- ![Alt text](code.png?raw=true "Cloud File Sharing Code") -->

```
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

```

## Original Code: With error 
### The error message "Object of type 'None' is not subscriptable" usually means that you are trying to access a subscript (such as an index or a key) of a variable that has a value of None. In the code you have provided, the variable url is initialized by calling the go.uploadFile(file) function. If this function returns None, then the next line print("Download Link: ", url["downloadPage"]) will raise an error, because you cannot access a key of None.

### To fix this error, you can check if url is not None before trying to access its keys. Here's an updated version of the code that includes this check:

### main.py problem: Object of type "None" is not subscriptablePylance

```
import gofile as go
def Store_Files(file):
    cur_server = go.getServer()
    print(cur_server)
    url = go.uploadFile(file)
    print("Download Link: ", url["downloadPage"])
Store_Files("test.jpeg")

```

This code will print the download link if the upload was successful, or an error message if the upload failed.

### #rayturner.dev #clcoding.com