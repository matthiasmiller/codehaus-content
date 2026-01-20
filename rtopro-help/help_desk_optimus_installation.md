# http://www.rtopro.com/help/help_desk_optimus_installation.htm

# Optimus Installation (Metrologic scanner PDC)

<< [Click to Display Table of Contents](index.md) >> **Navigation:** [Help Desk](help_desk_pricingsetup.md) >

# Optimus Installation (Metrologic scanner PDC)

|  [](cipherlab_1166_setup.md "Previous Topic") [](help_desk_pricingsetup.md "Parent Chapter") [](help_desk_scanpal_2_setup.md "Next Topic")  
---|---  
  
Follow the installation directions for installing the drivers for the scanner. (Install the CD that came with the scanner and plug the scanner into the computer.)

Find out the Com Port the scanner it is on as it shows below. Open up Control Panel > System > Hardware > Device Manager. Look for the Optimus under "Ports" to see what com port it is on. Write this down you will need it later.

![1](1.jpg)

On the scanner do the following

1\. Power up the Optimus and select the Utilities option.

2\. This will open additional menu options. Select the Transfer Files option.

3\. Select Get Program on the next menu. The unit is now ready to download an application

program.

4\. Place unit in cradle it should say "Waiting to Connect".

On your computer do the following

5\. Open the Optimizer program. It can be found under Programs > Optimus Software > Optimizer

6\. Choose File > Open and browse to the folder you have RTO Pro installed (default is c:\rtowin).

7\. Open the file "RTO Pro Optimus.opt" as shown below

![2](2.jpg)

8\. Then as it shows below Click on Tools > Communication > Download Program (you can also push F6).

![3](3.jpg)

9\. Set the correct Com Port as below then click OK. It will install the scanning program into the scanner and you are ready to start scanning.

If it does not transfer the program check the settings in the scanner and make sure it has the same Baud Rate as it shows here 115200 bps.

![4](4.jpg)

Next on your computer do the following:

1\. Open the Data_read program. It can be found under Programs > Optimus Software > Utilities > Data_read

2\. Verify the info under "Communications Parameters" the rest of the settings do not matter, click OK after the settings are correct.

Interface: "Cradle-IR"

Com Port: (the com port you wrote down above)

Baud Rate: 115200 bps

![image61](image61.jpg)

Below for reference, what the buttons on the scanner look like.

![image60](image60.jpg)

If you only get 2 menu options on the scanner follow the directions below with the "RTO Pro Optimus.opt" file loaded in the Optimizer, then download the program to the scanner again. Make sure you have Ver 1.37.0 or newer of the Optimizer.

NOTE: When you follow the directions below at one point you have to go into "Utilities" on the scanner, while your scanner only has 2 options on the main menu option 3 is still the Utilities menu even though it is not displayed on the screen, you can press the #3 on the keyboard to get to it. Option 2 is "Send Data" even though it says it is Utilities.

To update Optimizer to the current version, go to:

http://www.metrologic.com/northamerica/download/SP5500/ and download the Software Suite

![image63](image63.jpg)

![image62](image62.jpg)
