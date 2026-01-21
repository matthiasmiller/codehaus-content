23.1. Online Member Application Portal ("WSGI")

  


Requirements

New applicants can access a public-facing application page to apply online. The web-page will automatically create an application record in the SPE Management system.

  


The online member application will be for new members only. (Prefilled renewal applications will be created as PDFs to print and send by mail.)

  


Development Specification

Matthias Miller 12/08/2020: One possible design:

  * have a new record for incoming applications
  * show the application information on the left. show the contact and equivalent information on the right. allow creating a new contact, which creates a new contact that defaults to that info, or allow updating an existing contact
  * show the school information, and allow matching it up with actual schools or creating new schools in the system - then using that to create a new pending application (that links back to the form)



  


Alternatives

  * Automatically add contacts and schools but include Online Application #____ in the name to force them to be unique. Require them to be merged into existing contacts or to be cleaned up. Provide reports to help with this.


