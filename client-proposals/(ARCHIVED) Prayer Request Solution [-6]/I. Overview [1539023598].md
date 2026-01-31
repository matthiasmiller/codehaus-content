1\. Overview

  


Requirements

Inbound Emails & Admin System

The prayer requests will be sent to a special email address that will import these emails into a database.

  


These will be imported into an admin system that includes:

  * Full Name (from import)
  * First Name
  * Email
  * Location
  * Prayer Request (unformatted text)
  * Moderation (Pending, Approved, or Denied)



  


This admin system will have a moderation report that will show:

  * First Name
  * Location
  * Prayer Request



  


From there, you'll be able to open individual requests to edit them.

  


This report will have a "Deny Selected", "Approve Selected", and "Approve All" button.

  


Users

We will have a list of approved email addresses. These people will receive these requests and be able to access the system.

  


Outbound Emails

We will send emails to all users. You will be able to schedule emails in advance. They will automatically be sent out automatically at 5 AM. (This will create new login tokens for the users, as well as refresh the homepage with the current prayer requests.)

  


Each email can embed a link (unique to each user) that gives each user direct login access.

  


Portal

The portal will be an encrypted site showing a list of the current prayer requests. This will include the Name, Location, and Prayer request. They will be ordered from newest to oldest.

  


Each request will have an "I Prayed" button. When clicked, the button will become disabled and show a green checkmark beside it. The prayer request will also show how many people have prayed for the request.

  


The right pane will have a list of dates (Month + Year)  on the right to allow going back to prior requests.

  


The web design will be a simple, straightforward design.

  


The portal will stay logged in until the token expires. We will have a log out link in case they are logged in on a public computer.

  


Questions

  * What email address should these outbound emails be coming from?
  * Will you moderate between emails? When should they show up on the website?
  * Do you need some kind of template for the outbound emails>



  


Always displays

  


  * Show the last two weeks on the home page
  * Show the number of PEOPLE 
  * Do not show the PRAY button more than once.



  


  


FUTURE:

  * Add a star to a prayer request



  


Development Specification

  * We need to have a token for each person that expires in 3 weeks.


