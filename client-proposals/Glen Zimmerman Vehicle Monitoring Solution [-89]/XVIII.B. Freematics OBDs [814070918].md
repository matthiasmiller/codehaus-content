17.2. Freematics OBDs

Overview: Freematics ([https://freematics.com/](https://freematics.com/)) OBDs are the devices that customers will use to track vehicles. TODO_BR: Ben Reitz 10/01/2025: Add info about Model A vs Model B

  


Linking Freematics with Traccar:

1. Install Visual Studio Code: [https://code.visualstudio.com/](https://code.visualstudio.com/) 

2. Install PlatformIO extension for VS Code (VS Code | Extensions (bottom item on the lefthand toolbar)

3\. Go to [https://github.com/stanleyhuangyc/Freematics](https://github.com/stanleyhuangyc/Freematics)

4\. Click "Copy", then click "Download ZIP" PAY ATTENTION TO WHERE THIS WAS DOWNLOADED TO

5\. In your file explorer, find the zipped "Freematics-master" folder. Right click and select "Extract All"

6\. Open Visual Studio Code and navigate to the PlatformIO extension

7\. Click "Import Arduino Project"

8\. Select "Espressif ESP-WROVER-KIT" in the first drop list. Note that you can find it by searching "wrover"

9\. Follow this pathing to get the correct folder to import: Places | <User that you saved the Freematics-master folder to> | <Location that you saved the Freematics-master folder to> | Freematics-master | firmware_v5 | telelogger

10\. Click "Import"

11\. When the project opens automatically, click "config.h"

12\. Scroll to line 89 (#define CELL_APN " ") and inside the quotation marks, enter the APN as directed by your SIM provider. (If you're using a Hologram SIM, simply put "hologram")

13\. On line 91 (#define SERVER_HOST " "), enter the IP address from your "Welcome to Traccar" email

14\. On line 106 (#define SERVER_PORT 8081), change "8081" to "5170"

15\. On line 157 (#define GNSS_ALWAYS_ON 0), change "0" to "1"

16\. Click "File" (top left), then "Save" to save these changes (alternatively, simply do Ctrl + S to save)

17\. Plug your Freematics device into your computer

18\. In PlatformIO, under "Project Tasks", click "Upload" (note, if you're receiving a message in this "Project Tasks" section about not having any projects, simply close the entire application and reopen it)

19\. Allow PlatformIO to run its process of copying the code into your device

20\. Plug the device into your car and drive around. Then check your Traccar server to confirm that the device was tracking the information correctly
