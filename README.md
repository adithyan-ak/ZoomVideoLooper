<h1 align="center">Zoom Video Looper</h1>

<h5 align="center">
  <br>
  <br>
  Zoom Video Looper
  <br>
</h5>

### About

Zoom Video Looper is a python tool that loops your video in zoom meetings by abusing the zoom virtual background capability.

### Requirements

- Python3

### Setup

- Disable all the camera sources in your computer.

- Capture a video of yourself like listening or writing or anything else appropriate to the Zoom meeting.

- Convert the video as frames using https://ezgif.com/video-to-jpg

- Download all the frames as zip. Extract them and place it in a folder.

- Open Zoom settings and go to virtual background settings.

- Click ```+``` button and add the images from the extracted folder in order one by one.


- Now, Clone this repository in your terminal.

```git clone https://github.com/adithyan-ak/ZoomVideoLooper.git```

```cd ZoomVideoLooper```

- Join a Zoom Meeting and Click on Join Video.

- Click Choose Virtual Background in Video settings.

- In the terminal, type

```python zoomloop.py```

- Within 5 Seconds, Choose the 1st image in the virtual background.

- Now, the images will keep changing at a rate at 0.1 Second which will make it look like a video.

- By default, the script will go upto 50 background images from first to last and on reaching last, it'll reverse the play from last to first. Please change the script according to the number of images you have in your Virtual Background settings.

- This process keeps on repeating in a loop until you exit(Ctrl + C).
