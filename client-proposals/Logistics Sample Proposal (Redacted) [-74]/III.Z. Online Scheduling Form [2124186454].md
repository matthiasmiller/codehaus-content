3.26. Online Scheduling Form

  


Requirements

We will provide a form that you will be able to embed on your website.

  


It will prompt for:

  * Name
  * Address
  * Phone Number
  * How should we confirm the schedule if we can accommodate your request?
    * Text Me
    * Call or Email
  * Email
  * Detailed Description
  * Pictures (note that it's optional, but providing them increases the likelihood that we'll be able to accommodate their request)
  * Pickup Date (availability is determined by zip code, per settings above)
  * Receipt
    * Paper
    * Email
    * None
  * Comments



  


If they submit the form without providing pictures, show a note on the followup screen:

  


Providing pictures is optional. However, it increases the likelihood that we'll be able to accommodate your request. You can text us pictures from your cell phone:

  


Mobile: [                        ]  [Text Me]

  


This will send a message from the client number saying:

  


"Thank you for your pickup request! Simply reply to this message with pictures of your pickup items."

  


NOTE: We are intentionally excluding the requested pickup time. Staff will be in touch with them to see if they have any specific requirements.

  


Development Specification

Matthias Miller 09/03/2020: We have two options:

  * Using questionnaires, similar to ZNH's public staff application
  * Using a hard-coded WSGI



  


The challenge with the questionnaire is that you need to be able to import that information onto a stop. The upside is that we can re-use this feature.
