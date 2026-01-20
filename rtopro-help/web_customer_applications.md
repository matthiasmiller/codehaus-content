# http://www.rtopro.com/help/web_customer_applications.htm

# Taking Customer Applications through the internet

# 

<< [Click to Display Table of Contents](index.md) >> **Navigation:** [Help Desk](help_desk_pricingsetup.md) >

# Taking Customer Applications through the internet

# 

|  [](help_topics_for_importing.md "Previous Topic") [](help_desk_pricingsetup.md "Parent Chapter") [](customer_import_fields.md "Next Topic")  
---|---  
  
There are 2 ways you can accept applications from the internet using RTO Pro, both of these options will be explained below.

1. Use the RTO Pro Web Services Application feature, see the page here for an example of how it could look, but of course your application page would have your logos, colors, banners etc. <https://rtowebpay.com/apps/default.aspx?id=0B440004450301>

This service is included with the RTO Pro support plan, there is no additional charge to use it. If you use this feature no programming on your website would be required, you would simply add a link or button on your website that directs your customers to the application page we design for you. When a customer submits an application online it would be imported into RTO Pro automatically.

If you wish to use this method call 352-383-9375 and we will set you up.

2\. Design and develop your own web page to accept applications online and do the programming and setup required yourself or hire a developer to do it for you. Using this option your applications would also be imported into RTO Pro automatically, but most stores would have to hire a developer in order to set their website up correctly to take the applications online.

If you wish to use this option the instructions are below that you would need to follow to set it up on your website. If you wish to make your own web page to accept applications we do not provide support for setting up your website, (S)FTP service or any other facets of the web applications development, setup or testing process. The only support we provide is the information on this page.

* * *

Please note this feature was designed for importing customer info, and optionally agreement and inventory info from a website, so you can build a website that you can accept customer applications and/or load agreements online. Any agreements imported will have a "PENDING" status, and will have to be loaded, like a pre-printed agreement is to make it an "OPEN" active agreement. For any dealers we have a service that allows you to accept applications online without building your own web application. For shed companies we have a service that allows your dealers to do load agreements online, and optionally have customers e-sign them at the dealers lot. 

For more info on our web applications service see this page: <http://www.rtopro.com/import_apps.aspx>

For more information on our Shed Dealer Web Portal see this page: <http://www.rtopro.com/sheddealer.aspx>

It is possible to setup a web page to allow your customers to enter applications for rentals / sales via the internet and to automatically import this application info into RTO Pro. Agreement and inventory info can also be imported so a complete customer application and order can be placed on your website and then imported into RTO Pro automatically. This help topic will walk you through the process of setting this up. Please note the programming and design on your website are not included in support with RTO Pro, you will have to get a web designer or create the web pages yourself. 

During the import process a PDF file can also be downloaded and attached to the customer's document imaging files. For this to work the PDF file must have the same file name as the XML or CSV file. For instance you could have saved on your server a file named "app001.xml" and "app001.pdf", the customer info would be imported from the "001.xml" file and the "001.pdf" file would be attached to that customer. Please note you must be using the new document imaging module to view the PDF files through document imaging, this is enabled in store setup.

There are 4 components required to allow applications via the internet, each are described below.

1\. In RTO Pro under the "Other" tab in Store Setup enable the application import feature in RTO Pro. To do this you will enter the FTP information that must be setup on your website to allow RTO Pro to download the applications. The file "c:\rtowin\ImportApplications.exe" is the program that will check for pending application entered online and import them into RTO Pro, so make sure you set your firewall to allow this program access to the internet. You must also choose the customer "Status/Rating" you want to assign to represent pending web applications.

When this feature is enabled your system will check every 15 minutes for pending applications(there is a button you can click to check for applications manually anytime you wish). When pending applications are received you will be notified. To view pending applications you can click on the "View Pending Web Applications" button on the payment screen or the Point of Sale menu in RTO Pro.

2\. A web page on your website that will collect the customer application information. What information you collect is up to you however the field names in the XML files must match the field names that are described at the bottom of this help topic or they will not import into RTO Pro (in our example code the input text names from the HTML file become the XML field names). Note RTO Pro DOES NOT create your web pages for you. See below for a sample HTML file or [click here](web_customer_applications.md#samplehtmlcode).

3\. A CGI or script file to handle the posted data and save it to an XML file, this could be included in your web page instead of a separate script file. See below for a sample Perl script file or [click here](web_customer_applications.md#sampleperlscriptfile). To see a sample XML file (the file your script will create) [click here](web_customer_applications.md#samplexmlfile). The script file should be programmed to save the XML file in a password protected folder so the files are not accessible to anybody on the internet. This folder is where you setup the FTP account to connect to.

4\. An FTP or SSH/SFTP account on the server that hosts your website that will enable RTO Pro to connect to the folder XML files are saved and retrieve the XML files that are created when a customer fills out an application online. You enter the FTP account info in Store Setup in RTO Pro under the "Other" tab. Please note SSH/SFTP (Secure FTP) is recommended since personal info such as social security numbers can be included in the customer application data.

To see this feature in action enter the test FTP info below in your store setup, and enter some sample customer data on this page: <http://rtopro.com/testxml.html>

Test FTP info:

FTP Address: [ftp.rtopro.com](ftp_rtopro_com.md)

FTP User name: [xmltest@rtopro.com](mailto:xmltest@rtopro.com)

FTP password: xml12red

Please note if there are other users testing at the same time you may get info they entered or they may get info you enter.

The program in RTO Pro that actually connects via (S)FTP to your web server to retrieve the online application files is "importapplications.exe", it will be in the RTO Pro installation folder. Be sure you have your firewall configured to allow this program to access the internet or it will not be able to retrieve the applications.

Please note when using FTP/SFTP to retrieve files from your server the files must be XML format and be named "app???.xml" (the ??? can be any number or other characters but should be something to make each file name unique) . 

[Click here to see the list of fields that can be imported](customer_import_fields.md)

* * *

Sample Perl script file

#!/usr/bin/perl

use strict;

use CGI;

use CGI::Carp 'fatalsToBrowser';

# instantiate a CGI object

my $obj = new CGI;

# start some basic HTML output

print $obj->header,

$obj->start_html,

qq(<ul>);

my $f_lock = '2';

my $f_unlock = '8';

my ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime(time);

$year += 1900; ## $year contains no. of years since 1900, to add 1900 to make Y2K compliant

$mon += 1; ## Month stars at 0 for January

my $file_name ="App$year-$mon-$mday-$hour-$min-$sec.xml"; # this is the unique part of the file name with the date, time and seconds included... "App2012-01-30-1-35-15.xml"

#open a new XML file for writing, this uses a subfolder "webapps"... note this folder should be password protected so it cannot be accessed publicly

open(OUTPUTFILE,">>../webapps/$file_name") or 

die "Failed to open OPF, $!\n";

# get an exclusive lock on that file

flock OUTPUTFILE, $f_lock;

# seek to the end of the existing content

# incase a previous process wrote to the file

# after the open and now

seek OUTPTUFILE, 0, 2;

# get an array of the passed CGI parms

my @params = $obj->param;

print "The following information has been submitted:";

# get a value for each parm and print them

print OUTPUTFILE "<application>\n";

foreach my $key (@params) 

{

my $value = $obj->param($key);

print "<li>$key : $value";

print OUTPUTFILE "<$key>$value</$key>\n";

}

print OUTPUTFILE "</application>\n";

# unlock the file 

flock OUTPUTFILE, $f_unlock;

# gracefully close your HTML

print qq(</ul>), $obj->end_html;

* * *

Sample XML File

Below is a sample of what the XML file your script creates should look like. The XML file name should be formatted as follows: "AppYYYY-MM-DD-H-M-S.xml" so if the file was created on 1/30/2012 1:35:15 it should be named:"App2012-01-30-1-35-15.xml". As long as the file name starts with "App" and ends in ".xml" you can use any numbering system you wish for the rest of the file name, as long as every application submitted has its own unique file name.

The "<?xml version="1.0" standalone="yes" ?>" line is optional. The "<application>" parent tag can be any tag name you like as long as the actual record tags are underneath a parent tag.

Below the sample contents of the XML file (with only 3 customer fields, yours will have as many customer data fields as you wish see [customer data that can be imported](customer_import_fields.md)).

<?xml version="1.0" standalone="yes" ?>

<application>

<name>DOE,JOHN</name>

<address>2000 Anystreet</address>

<city>Anytown</city>

</application>

* * *

Sample HTML code

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">

<head>

<meta content="text/html; charset=utf-8" http-equiv="Content-Type" />

<title>Contact Information *Required to</title>

<style type="text/css">

* {outline:none;}

.style1 {

color: #FF0000;

}

.style2 {

margin: 0;

padding: 0;

}

</style>

</head>

<body>

<p class="style2">Contact Information

<font color="#FF0000">

*Required</font></p>

<form action="http://www.rtopro.com//cgi-bin/apptoxml.pl" enctype="multipart/form-data" method="post" class="style2">

<table style="width: 100%">

<tr>

<td style="width: 126px" class="style2">First Name<span class="style1">*</span></td>

<td class="style2">

<input type="text" name="firstname" style="width: 206px" class="style2"/></td>

</tr>

<tr>

<td style="width: 126px" class="style2">Last Name<span class="style1">*</span></td>

<td class="style2">

<input type="text" name="lastname" style="width: 206px" class="style2"/></td>

</tr>

<tr>

<td style="width: 126px" class="style2">Co-Renter First Name</td>

<td class="style2">

<input type="text" name="altfirstname" style="width: 206px" class="style2"/></td>

</tr>

<tr>

<td style="width: 126px" class="style2">Co-Renter Last Name</td>

<td class="style2">

<input type="text" name="altlastname" style="width: 206px" class="style2"/></td>

</tr>

<tr>

<td style="width: 126px" class="style2">Address</td>

<td class="style2">

<input type="text" name="address" style="width: 206px" class="style2"/></td>

</tr>

<tr>

<td style="width: 126px" class="style2">City&nbsp; </td>

<td class="style2">

<input type="text" name="city" style="width: 206px" class="style2"/></td>

</tr>

<tr>

<td style="width: 126px" class="style2">State</td>

<td class="style2">

<input type="text" name="state" style="width: 206px" class="style2"/></td>

</tr>

<tr>

<td style="width: 126px" class="style2">Zip Code</td>

<td class="style2">

<input type="text" name="zip" style="width: 206px" class="style2"/></td>

</tr>

<tr>

<td style="width: 126px" class="style2">Work</td>

<td class="style2">

<input type="text" name="work1" style="width: 206px" class="style2"/></td>

</tr>

<tr>

<td style="width: 126px" class="style2">Comments / Order info</td>

<td class="style2">

<input type="text" name="comments" style="width: 206px" class="style2"/></td>

</tr>

</table>

<input type="submit" value=" Submit " style="width: 106px" class="style2"/>

</form>

<p class="style2">&nbsp;</p>

</body>

</html>
