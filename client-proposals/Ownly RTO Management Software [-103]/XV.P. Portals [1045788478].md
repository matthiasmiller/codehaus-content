15.16. Portals

  


Requirements

  


  


Development Specification

Authentication:

  * Email Magic Link
    * One-time link sent to the email address of the user.
  * SMS OTP
    * 6-digit code sent to the number of the user.
  * Authenticator App
    * Uses Google Authenticator or similar app.



  


An authenticator app would be the most secure, and we could use one for the manufacturer portal, but Email Magic Link / SMS OTP would work well for the customer portal.

  


Endpoints:

If systems will be hosted at systemname.ownlyrto.com, I think portals should be at systemname.wsgi.ownlyrto.com/portal-name. A system for "affordable" would have their customer portal at affordable.wsgi.ownlyrto.com/customer-portal.

  


Source Control:

Each portal should have its own catalog, with components in the catalog's folder. I don't anticipate systems needing customization on their portals, but we could branch the repo for this.
