1\. Summary

  


Requirements

Objective: To import accounts from the Sheds Unlimited website to SharpSpring.

  


Expectations

Because of Eric's proficiency with Drupal, I'm proposing that we allow him to do all the work required within Drupal. I've already discussed this with him. This includes:

  


  * API interfaces for:
    * All accounts across time (including First Name and Email Address)
    * Accounts created in the past 7 days
    * (Optional) All saved images with URLs, associated email address, and recency (for example, timestamp)
    * (Optional) All accounts with saved images from the past 7 days
  * A separate user account via OAuth2 (recommended), Basic authentication, or token authentication.
  * (Optional) Custom fields in SharpSpring to store the URLs for the most recently saved images



  


Syncing Behavior

If the lead does not exist in SharpSpring, we will create it with:

  * The website first name
  * The website email
  * The lead source "Saved Photos"
  * (Optional) Link to the 1 or 2 most recently saved images



  


If the lead already exists in SharpSpring, we will update the first name and lead source if they are blank. We will always update links to the saved images (optional).

  


Wildcards

One of the major wildcards of this project are the cost of integration with Drupal. With everything else, we already have the major building blocks that we need.

  


The other significant wildcard for this project is the design of the saved images. This proposal assumes that we only want to save the most recent 1 or 2 saved images.

  


Cost

I estimate the base cost for this project to be $2000-2500.

  


If you choose to also sync saved images, I anticipate that to cost an additional $500-1000. It will likely be less expensive to bundle this with these other changes because it will consolidates testing and development.

  


Development Specification

From Chris:

  


We have customers creating accounts on the website so they can save their photos. What I'd like is to be able to bring into SharpSpring the email address so we can begin sending email to people based on their account setup. 

  


I would like: 

  


1\. First Name (Eric might need to make some changes on the account setup first)

2\. Email

3\. A link to go back and view their "Liked" photos

  


I'd like to be able to pull in the photos they liked and have them sent in an email as well. Not sure how to make this work. 

  


If we can get points 2 and 3 integrated as a starter, that would be great. 

  


And I realize all this will cost more :)

  


Could you tell me about how much time you estimate this could take?

  


From Chris:

  


What I'm looking for is a way to send email to people who have created accounts to save photos and then send email based on that. 

  


Here are some of my thoughts:

  


1\. This should be lead source: Saved Photos

2\. I'd like First name, and Email address.

3\. Could we have a link that would send them directly to their personal page showing what they've saved?

4\. I'm trying to figure out if we can actually pull in the photos they saved and send the first one or two in an email, but have not been able to figure out how to do this. That is not the most important right now, but if we could at least pull in their account link so it could be sent to them in followup emails.

  


Matthias Miller 02/20/2018: 

[ ] Will they want to import accounts that don't have a first name?

Matthias Miller 02/20/2018: Per Eric, SharpSpring probably requires a first name.

Matthias Miller 02/20/2018: This would simply limit the creation of new accounts.

  


[ ] If the email address is in SharpSpring, do we update the Lead Source, or only for newly created ones?

  


Matthias Miller 02/20/2018: In Drupal, they have a flag as a generic item for content, that is associated with a user. This links it back to the content. Currently this is only enabled for photos.

  


Matthias Miller 02/20/2018: The link to the Saved Photos could just be hardcoded to [https://shedsunlimited.net/user](https://shedsunlimited.net/user)

  


  


Matthias Miller 02/20/2018: Drupal uses a lot of what they call views (similar to what WordPress - wp-query)

  


Matthias Miller 02/20/2018: See services API and restfull API -- we will probably want to use token authentication.

  


Matthias Miller 02/20/2018: They are running on Drupal 7

* Can create a view

* Recommend separate user account with restricted access
