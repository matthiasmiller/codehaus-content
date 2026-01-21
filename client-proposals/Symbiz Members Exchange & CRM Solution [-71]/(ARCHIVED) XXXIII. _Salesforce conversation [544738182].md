33\. *Salesforce conversation

DONE_MM: discuss Salesforce side of things (see sheets that client sent; what do we need?, what questions do we have for the client?) 

Tim Reitz 04/06/2023: DONE_DH: Questions/comments: 

  * What information needs to go between the systems? 
    * Contacts: 
    * Groups: 
    *   * Which system is the source of truth for:
    * Active memberships?
    * Contact details?
    * Group membership? 
  * Would not be doing full 2-way syncing
  * Could do manual imports/exports for Phase 1 or phase 2, look at automation later



  


Tim Reitz 04/11/2023:

  * Currently using:
    * Salesforce for CRM
      * New leads
      * Members & various data points
      * Growth Rings
        * Who is a member of what group
        * Facilitator
        * Etc.
      * Who has paid, etc. (currently being manually entered)
      * Score card (weekly - new leads, new members, etc.)
    * Using QB for invoicing, payment processing (long-term goal of integrating this with Salesforce)
    * Not for emailing - but longer-term would be looking to do that once it's set up the way they want it
      * To date they haven't done mass emailing (would want to get there, especially industry-specific notices, etc.)
  * Where they would like to go with Salesforce:
    * Steve's bar is not very high
    * Wants to be able to easily access information about the members
    * Wants to have accurate metrics / KPIs / reports
    * Track and follow up with leads
  * What would be the source of truth?:
    * Note that we're talking about 3 programs here: QB, SF, AHZ
    * If allowing members to edit their own information in AHZ, the Member's Portal would need to be the source of truth for that
    * Probably would create leads in SF (so would be the source of truth for leads), but from the point of membership AHZ would be the source of truth for members.
    * Currently QB is the more accurate of the two, so Steve is using QB to get SF up to date
    *   * What they'd like to sync:



  


DONE_DH: communicate with client

DONE_BR: summarize and send over to client

Tim Reitz 04/11/2023: From conversation with Matthias. His proposal: 

  * Use AppHosting for CRM + Member's Portal (drop Salesforce) 
    * Think through all the pieces that we would need to add to AppHosting side to replace it (probably another call with Steve if it goes forward)
  * At some point build out integration with QB as needed 
  * Could push out email lists + segments to a 3rd party service (like Hubspot) if they want to do mass email / marketing 
    * If not looking to do mass marketing, could look at sending batches of emails directly from the AppHosting software. 



  


  * As far as managing complexity, it seems better to put it into a consolidated system. It might be about the same up-front cost, but longer-term there would be pay-off.



  


DONE_DH: Tim Reitz 04/25/2023: Have you all discussed/settled on this?

TODO_IDD: Tim Reitz 04/25/2023: Steve is in favor of consolidating. Questions: 

  * How much additional cost to add the features to AppHosting? 
    * Tim Reitz 04/25/2023: Telling him that it depends on complexity. We should get Steve on a call this week to discuss. 
  * How easy to use/learn/train new users? 
    * Tim Reitz 04/25/2023: Telling him that I think the net learning curve would be less having it all combined vs. needing to learn two systems, etc. Less bells and whistles than Salesforce, but we do push for useability.


