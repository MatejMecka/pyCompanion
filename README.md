pyCompanion
=========

Uses voice recognition library, can login you on Facebook, search on YouTube or Google.

Requirements
------------
You probably going to need some of these things.

* `Python 2.6, 2.7, or 3.3+`
* `PyAudio 0.2.9+` (required only if you need to use microphone input)
* `Speech Recognition` - library

Installing
------------

* `pip install SpeechRecognition`
* Execute `sudo apt-get install portaudio19-dev python-all-dev python3-all-dev && sudo pip install pyaudio` (replace pip with pip3 if using Python 3).

Usage
-----

Run `python3 pyCompanion.py`.

* Say `Facebook` - it will open new browser window and login you on Facebook. (You are going to need to add your user / pass manually in the code.)
* Say 'YouTube' + what you want be searched. (example: "YouTube Darude Sandstorm")
* Say 'Google' + what you want to be searched. (example: "Google how to make cookies")
