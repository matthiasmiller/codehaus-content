# http://www.rtopro.com/help/importing-email-templates.htm

# Importing Email Templates

<< [Click to Display Table of Contents](index.md) >> **Navigation:** »No topics above this level« 

# Importing Email Templates

|  [](welcome_welcome_1.md "Parent Chapter")  
---|---  
  
We do not provide support for using other software or editing files created from other software. This help topic is here as a courtesy to help you with importing Email Templates that can be made online from a lot of different services that allow easy email template creation by choosing from many pre-made templates, then editing it by drag and drop. 

A couple of examples of sites that offers this are below: 

<https://beefree.io/>

<https://unlayer.com>

Follow the steps below.

1\. Choose the site you want to use to make your email template, remember responsive designs are best, they look good on any device.

2\. Design the layout you want and make any edits you want on the design site. You can always easily make edits after importing also, so don't worry about everything being perfect.

3\. Most sites will have an Export or Download feature, when you have the design the way you want it export(download) it to your computer.

4\. It will probably be in a zip file, unzip the contents into a folder you can easily find.

5\. When you unzipped the zip file it should have made 1 file and 1 folder, the folder is probably named "Images"

6\. Now go into RTO Pro >Customer Menu > Edit Letters > make sure you are on the "Letters to Email" tab, click "Add File" button at the top.

7\. Browse to the location you unzipped the email template in step 4 and select the HTML file. You will be prompted for a description, enter that and you should be done. Double click the new email letter you just added and it should display and look just like it did when you designed it.

Note for imported templates to work the image files must be copied to the RTO Pro storage folder for HTML images and the HTML file edited to update the src for the images, this should be handled by RTO Pro automatically, if RTO Pro can't copy the images or edit the file follow the steps below.

* * *

Manually Editing Email Template and Copying Image Files

1\. Follow steps 1 to 5 above.

2\. Go to the folder you unzipped the template file to in step #4 above. Copy the files in the images folder to your email images folder for RTO Pro, this will be on your server in your data folder(default is "C:\rtowin", but yours could be anywhere) under "docs\\_HTMLimages\", so if RTO Pro is installed in default location it would be "C:\RTOwin\Docs\\_HTMLimages\". For Central Server companies it would be "C:\RTOwin\Docs\001\\_HTMLimages\" (the 001 is the store number you are making this template for, choose the correct store number folder as needed)

3\. The 1 HTML file that was in the zip file was probably named "index.html", we need to edit this file so it knows where the images are going to be when used by RTO Pro.

4\. Open the index.html file with Windows Notepad, you can do a search and replace to change the path for the images, search for "src="images/" and replace with "src="_HTMLimages/". Note if they used a different folder name than images this search would have to be changed accordingly.

5\. Click File > Save AS, save it with a name so you would know what it is for, like "Summer Sale Email.html" for example.

6\. Now go into RTO Pro >Customer Menu > Edit Letters > make sure you are on the "Letters to Email" tab, click "Add File" button at the top.

7\. Browse to the location you saved the file in step 9 and select that file. You will be prompted for a description, enter that and you should be done. Double click the new email letter you just added and it should display and look just like it did when you designed it.
