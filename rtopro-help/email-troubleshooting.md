# http://www.rtopro.com/help/email-troubleshooting.htm

# Email Troubleshooting

<< [Click to Display Table of Contents](index.md) >> **Navigation:** »No topics above this level« 

# Email Troubleshooting

|  [](welcome_welcome_1.md "Parent Chapter")  
---|---  
  
Follow the steps below for troubleshooting email:

1\. From Main Menu of RTO Pro click "SendMail" at the top.

2\. Click "Edit SMTP Settings" button at the bottom right.

3\. Make sure the info is filled in, if not contact your email provider to get your SMTP settings and credentials.

4\. If email credentials are filled in check the "Debug Send Direct" check box.

5\. Click Save

6\. Enter YOUR email in the TO:

7\. Type "test" in the subject field

8\. Click Send Mail

If it does not work it will display the message from the SMTP provider, sometimes the relevant part is toward the bottom. You would have to contact their email provider to correct anything wrong with your account or to get correct credentials, SMTP address etc.

If it does act like it went through check your email to verify you got the test email, sometimes it takes a couple of minutes.

Changes below are in version 5.9.224 and newer.

â¢When you send an email through SendMail with the box checked in the setup to send direct for debug, 2 source files will now be saved in the local logs folder, an .EML file and an .XML file. Please note EML files will not contain BCC info. This may help you troubleshoot issues with your email service provider. Ver 5.9.224 8/1/2022

![clip0074](clip0074.png)

Below is an example status message that displays when an email send fails, note the important part that says why it failed by the red arrows , toward the bottom, in this case bad user/pass (the red arrows are here for your reference only, they do not display in the messages). We cannot help them with their email user/pass or any other settings for their email provider, all we can do is show them why their emails are not sending, they have to contact their email provider to fix any issues.

![clip0075](clip0075.png)
