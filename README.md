# two-PythonAppsCommunication
The instructions for installing and running these two applications are as follows:

1. Requirements:

* You need to have Python3 installed on your system.
* The only dependency for these applications is the 'JSON' library, which is part of the Python Standard Library.

sys is a built-in module in Python, so it doesn't need to be installed. It provides access to some variables used or maintained by the Python interpreter and to functions that interact strongly with the Python interpreter.

time is also a built-in module in Python, and it provides various time-related functions. For example, time.sleep(secs) makes the program to sleep for 1 seconds.

2. Installing:

* Download the two python files and save them in the same folder as well as the JSON file.

3. Running the Applications:

Open the terminal in the folder where you saved the python files.
make sure you change the directory in app_a to your directory
make sure also you keep the access point file name as it is so it gets easier for you when you copy and paste from task instructions to get your desired output
Run Application A in the terminal by typing: python3 app_a.py
Run Application B in a different terminal tab by typing: python app3_b.py
open your JSON file from VScode or any terminal using vi

For more information on these libraries and their functions, you can refer to the official Python documentation:

JSON library: https://docs.python.org/3/library/json.html
time library: https://docs.python.org/3/library/time.html

Execution environment: Linux/macOS
Programming Language: Python 3.9.x and above

Your task is to create two Python applications communicating with each other where appa monitors the
changes to a file which contains surrounding Wireless APs in JSON format and informs appb which is
responsible for displaying the change in format of:
SNR and/or channel value has changed from to
is added to the list with SNR and channel
is removed from the list.
It should be possible to run multiple instances of app_B, preferably on different machines.

{
"access_points": [
{
"ssid": "MyAP",
"snr": 63,
"channel": 11
},
{
"ssid": "YourAP",
"snr": 42,
"channel": 1
},
{
"ssid": "HisAP",
"snr": 54,
"channel": 6
}
]
}

cat /tmp/access_points (after X seconds)
Coding exercise

Instructions

JavaScript

{
"access_points": [
{
"ssid": "MyAP",
"snr": 82,
"channel": 11
},
{
"ssid": "YourAP",
"snr": 42,
"channel": 6
},
{
"ssid": "HerAP",
"snr": 71,
"channel": 1
}
]
}

Expected output:
MyAP’s SNR has changed from 63 to 82
YourAP’s channel has changed from 1 to 6
HisAP is removed from the list
HerAP is added to the list with SNR 71 and channel 1

You must include instructions on how to install and run your solutions together with your code
(README.md)
If you have any dependencies (packages, libraries that you use) do not forget to mention them in the
installation instructions
You need to run your application and test it according to the instructions above (expected output);
please provide a screenshot of the execution or a log file
Please do NOT upload the result to public GitHub; provide us with your results through TeamTailor,
email, secure sharing location or private GitHub repo.

The assignment is not about creating a complete and polished application, but about showing us that you
can design an application from the ground up. We have intentionally left the specification open to
Submitting your code

Notes

JavaScript

interpretation to give you room to be creative but also to determine some suitable limits of the application.
There are no absolute right and wrong answers to this exercise.
Please keep in mind:
Code quality matters
Please document well; preferably in markdown
Testability is important
