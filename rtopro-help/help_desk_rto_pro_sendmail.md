# http://www.rtopro.com/help/help_desk_rto_pro_sendmail.htm

# RTO Pro Sendmail

# 

<< [Click to Display Table of Contents](index.md) >> **Navigation:** [Help Desk](help_desk_pricingsetup.md) >

# RTO Pro Sendmail

# 

|  [](help_desk_rto_pro_document_imaging.md "Previous Topic") [](help_desk_pricingsetup.md "Parent Chapter") [](employee_email_as_from_or_repl.md "Next Topic")  
---|---  
  
[Click here for help troubleshooting sending email.](help_desk_rto_pro_sendmail.md#troubleshootingemailsendingissues)

The RTO Pro Sendmail interface can be used to E-Mail reports, receipts, Home Office files or just E-Mails with any attachment you choose or E-Mails without attachments. It can also be used to send form emails to all customers from the customer list report, or overdue customers from the overdue reports screen or the on screen account manager. When sending form emails the email interface will not display, you simply select the form email to send, set the report parameters for what customers to include and then run the report.

When sending individual emails the Sendmail interface will display, instructions for using the SendMail interface are below.

In The recipient textbox you enter the E-mail address that you want to send the E-Mail to, to send to multiple addresses separate each address with a comma. You can also choose an E-mail address from the address book on the top right of the sendmail screen by double clicking an entry.

You can add entries to the phone book that you use often so you donât have to remember the addresses. To add an address click on the add button and enter the name or the store # and the E-Mail address.

Setting up your email account settings

At the bottom left of the Sendmail screen there is a button to edit SMTP settings, these settings can also be found in Store Setup. Click on the Edit Settings button and fill in the required info and then click on Save Settings.

Please note RTO Pro does not provide email service, only the software to send emails, you must have an email service in order to send emails. All Internet Service Providers(ISP's) have outgoing SMTP servers for their clients, so if you have internet access you have an email service already. Contact your ISP for their SMTP server info, or you can use a service such as Google's Gmail (see below for more info), or for a paid service use something like Amazon SES (see below). At the time of this writing the free Yahoo, Hotmail / MSN email services do not allow 3rd party software to use their SMTP servers, so these services cannot be used to send email through RTO Pro. CONTACT YOUR EMAIL PROVIDER TO SEE IF THEY WILL ALLOW YOU TO USE THEIR SMTP SERVERS, WE CANNOT ANSWER THESE QUESTIONS FOR YOU.

Also please note almost all email services have a maximum number of emails that they will allow to be sent. Some of them have a maximum per minute, hour or per day, contact your ISP or email provider for more info on their maximums. This is a good article on Gmails limits: <http://www.serversmtp.com/en/limits-of-gmail-smtp-server> If you need to send hundreds of emails a day you may need to get setup with a paid SMTP service (although there are many free ones that allow you to send thousands of emails a month), search the web for SMTP Service providers to find one. Your ISP (internet service provider) is your best bet for outgoing SMTP server, you should contact them first to see what their limits are and see if they will work for you.

We now offer an outgoing email service, if you are interested in using our outgoing SMTP service see this page for info: [www.rtopro.com/emailservice.aspx](http://www.rtopro.com/emailservice.aspx)

Below is the explanation of each setting:

Sender Name / Store: When you send emails this is what the recipient will see along with your email address, for instance "AAA Rentals [sales@aaarentals.com]".

Your Email Address: This is the address you use to receive E-Mails at your store. When the recipient replies to your email this is where the reply would be sent to.

The settings below depend on who's outgoing email service you are going to use, typically this will be your internet service provider (ISP). 

Contact your ISP or your email provider to get this info, WE CANNOT PROVIDE THIS INFO TO YOU, ONLY YOUR EMAIL SERVICE PROVIDER CAN.

Outgoing SMTP server: This is the server to use to send the E-Mails, this would usually be the Outgoing SMTP server of your ISP.

SMTP User Name: If your email provider requires you to use a username and password for outgoing emails enter the user name here.

SMTP Password: If your email provider requires you to use a username and password for outgoing emails enter the password here.

Send Using SSL: If your email provider requires SSL check this box... if you check this box typically the port would have to be entered also.

Email Port: If your email provider requires you to use a specific port enter the port here.

* * *

Amazon SES

For a paid SMTP service we recommend Amazon SES, it is very inexpensive and has a very high sending limit. Below is how you set up RTO Pro to use Amazon SES. 36 and 37 you would enter your user name and password Amazon gives you for use with SMTP. 34 you enter the name you want customers to see the email is from, 35 enter your stores email address. 33 is the SMTP address for our service with Amazon SES, it may be different if you set up an account with them.

![clip0030](clip0030.png)

Setting up SES on Amazon's side can be a little complicated. For your convenience, below are a few links that will help you set up Amazon SES. Our support services do not include helping to set up or configure SES or any other email services.

<https://docs.bitnami.com/aws/how-to/use-ses/>

<https://docs.aws.amazon.com/ses/latest/DeveloperGuide/quick-start.html>

<https://www.formget.com/setup-amazon-ses-account/>

<https://docs.bitnami.com/aws/how-to/use-ses/>

* * *

Google's Gmail

Please note sometime in May 2022 or soon after Gmail will no longer work as an SMTP provider with RTO Pro. They are enforcing OATH2 protocol for SMTP which requires a user to periodically enter their Google user/password on a web page to authorize the SMTP connection. We are not going to implement OATH2 for our email because it would not work well with the background email sending process. The email process needs to work in the background without user intervention, with OATH2 they would be required to continually authorize the connection. We recommend users to either use their SMTP from their ISP, or if they send a lot of emails Sendgrid or Amazon SES are both good options. Sendgrid is easier to set up, but more expensive than Amazon SES. We do not provide support for setting up any email service and there are many more services that can be found by searching for SMTP services.

Please note, we have not tested this thoroughly and do not provide support for setting it up, but it appears you can follow the steps below to set up an "App Password" that would allow you to use Gmail SMTP for outgoing emails in RTO Pro, if you have 2 factor auth enabled for your Gmail account.

<https://support.google.com/accounts/answer/185833>

Please note in 2014 Google enabled security features that prevent you from using their SMTP servers unless you configure your account to allow it, see this page for more info from Google about it: <https://support.google.com/mail/answer/78754>

Below is how to setup Gmail's SMTP server to send email. At the time of this writing Gmail allows other software to use their outgoing SMTP server, they are the only free service that does as of the time of this writing. Yahoo and MSN cannot be used unless you have a paid account with them. 

Below is how to setup your SMTP if you have a Google Gmail account (they are free). Please note these companies change their services often, they may no longer offer free use of SMTP or could have changed ports etc. Always contact your service provider to verify you have the correct information.

![SMTPsettings](smtpsettings.jpg)

The SMTP user name is your Gmail address and primary login at Gmail. The password would be your Gmail password. To use Googles SMTP you have to check the "Send using SSL" check box and put in port 465. 

* * *

Using Yahoo! Mail Plus as your outgoing SMTP Server

(Note Yahoo! Mail Plus is not the free Yahoo Mail account, the FREE Yahoo account CANNOT be used by other software to send email)

POP Yahoo! Mail Plus with Another Email Client

Here are the basic server settings for Yahoo! Mail:

Incoming Mail (POP3) Server: plus.pop.mail.yahoo.com (Use SSL, port: 995)

Outgoing Mail (SMTP) Server: plus.smtp.mail.yahoo.com (Use SSL, port: 465, use authentication)

Account Name/Login Name: Your Yahoo! Mail ID (your email address without the "@yahoo.com")

Email Address: Your Yahoo! Mail address (e.g., user@yahoo.com)

Password: Your Yahoo! Mail password

The free Hotmail Mail account cannot be used by other software to send email.

* * *

Sendgrid example. This worked after setting up an account with Sendgrid 4/2022, contact Sendgrid to verify settings if this does not work for you. You must set up your own account and use your credentials. At the time of this writing according to their docs the user name is always "apikey" (line 41 below).

![clip0055](clip0055.png)

* * *

Microsoft Exchange Notes

Microsoft Exchange has made changes that require special setup steps to be able to use SMTP without Oauth2, see info at links below.

<https://learn.microsoft.com/en-us/exchange/clients-and-mobile-in-exchange-online/authenticated-client-smtp-submission>

<https://techcommunity.microsoft.com/t5/exchange-team-blog/securing-authenticated-smtp-in-exchange-online/ba-p/1293154>

Please note we do not provide support for setting up your Microsoft accounts, this info is here as a courtesy only.

* * *

Troubleshooting Email sending issues

Issue: Email will not send at all through RTO Pro

1\. Check your SMTP settings, user name, password and SSL and port requirements for your email provider. Please note we do not provide email service only the means to send email through YOUR email provider, any questions about your email service should be directed to your email provider. 

2\. Verify you do not have a firewall blocking RTO Pro from sending emails. When sending emails the program "c:\rtowin\RTOProEmail.exe" is the program that sends emails, unless the email is generated through the manual send mail process in RTO Pro then it is sent by the program "c:\rtowin\rto-win.exe". Please make sure you have your firewall and any security configured to allow both of these programs internet access and email access. Note: The "c:\rtowin" is the default installation folder, yours may be different.

Issue: Some emails will send then sometimes they won't or when sending a lot of emails it will stop working.

1\. This could be caused by an internet problem, your internet may have gone down intermittently, your email provider's email service may be down at that minute.

2\. Your email provider may be blocking you due to going over their limit. Many email providers have maximum emails per second, minute and hour. Contact your email provider about this issue.
