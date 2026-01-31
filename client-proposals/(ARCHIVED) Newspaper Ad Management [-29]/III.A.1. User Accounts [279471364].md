3.1.1. User Accounts

  


Requirements

As mentioned above, there will be three main type of user accounts:

  * Full Admin Users
  * Publication Admin Users
  * Standard Users



  


Full Admin Users will have complete access to all publications on the database and can set up new publications. 

  


Standard Users and Publication Admin Users will be required to always be associated with a publication. This will be managed by a Publication field on the user account to select the publication from a list of all publications being managed on the database. 

  


Publication Admin Users should be able to set up users for their own assigned publication. Full Admins will be able to set up users for any publication.

  


Development Specification

Matthias Miller 12/16/2020: Probably have a new permission for " [ ] Configure Publications"

  


New field - Publication: Make sure the user's Publication field is only editable by an administrative user who is not assigned directly to a publication (Full Admin User). To make this work, have to have a checkbox that indicates that the user has access to all publications (otherwise, data restrictions will make other users appear to have access)

  


Ellis Miller 04/20/2021:

  


TODO_CH: I think only Full Admin Users should actually be administrators. We should set up a user group for "Publication Admin User" that has the "Change user groups and profiles" permission and "Configure Publication", but is still a standard user. Does that sound right?

TODO_CH: How do we expect support accounts to be configured? Should we allow a support account to also not have a publication specified? Perhaps we do still want the UserCanAccessAllPublications setting.

  


TODO_CH: Note that users can see a list of other users. I presume we are OK with that.

  


[ ] Add UserCanAccessAllPublications checkbox

[ ] Editable: Logged-in user IsFullAdminUser

  


[ ] Add UserPublication list field.

[ ] Visible: NOT UserCanAccessAllPublications 

[ ] OnInit: Logged in user's Publication

[ ] Editable: Logged in user IsFullAdminUser AND CurrentUserCanAccessAllPublications

[ ] Field change expression blanks out UserPublication if UserCanAccessAllPublications

  


[ ] Add a permission to configure publications.

  


[ ] Add a PublicationIsPermitted( vPublication) macro that returns true if this publication is permitted:

UserCanAccessAllPublications OR vPublication = CurrentUserPublication

  


1 day.
