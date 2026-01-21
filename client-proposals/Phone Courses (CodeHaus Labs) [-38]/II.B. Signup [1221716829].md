2.2. Signup

  


Requirements

Courses will be advertised through print or email media. To access them, callers will send an email to [signup@codehaus.academy](mailto:signup@codehaus.academy) or by fax to (719) 800-0020.

  


This will automatically respond with instructions to call the main training line of (719) 800-0040 and enter a 6-digit PIN.

  


If you call a phone number that is not an active directory, or it's a directory that does not have any courses, it will say:

This directory has not been configured. Goodbye.

  


When you call the number for the first time, it will give the welcome and say:

Before you get started, we want to make sure you can easily get information about your courses. This includes things such as the course directory, course materials, and other related information.

  


To get this information by email, press 1.

For fax, press 2.

For postal mail, press 3.

To speak with a customer service representative, press 0.

  


And then, based on the respective answer:

  * Please send an email to [signup@codehaus.academy](mailto:signup@codehaus.academy). You will receive an automated reply with a 6-digit sign-up code. If you have received this code, you may enter it now.



  


  * Please send a fax to 111-222-3333. You will receive an automated reply with a 6-digit sign-up code. If you have received this code, you may enter it now.



  


  * Postal mail may be subject to shipping and handling charges. To continue, please state your full name and address.



  


When they enter the code, it creates a new account and associates their email/fax with that phone number. It will say:

Thank you for joining the CodeHaus Training Network.

  


You will be receiving a CodeHaus Academy course directory soon.

  


If sending a course directory by fax for the calling phone number, it will hang up and say, "Please call back when you have received your fax. Goodbye."

  


Development Specification

[ ] The 6-digit code will not include any zeros. This will allow Twilio to use a "stop on digit".
