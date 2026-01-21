1\. Overview

  


Requirements

Eby Sawmill LLC (also referred to as "Eby's" in this design document) is looking for a better solution to track their incoming and outgoing logs, along with pricing and load information.

  


Eby Sawmill would like to streamline the data entry process when scaling (i.e. measuring and grading) incoming logs. This includes tracking information about the individual logs as well as their source. Eby's would like the ability to load the app before going offline, enter the information, then return to a data connection to save.

  


The second source of data entry is when exporting logs. Eby's would like a streamlined process for scaling and documenting these outgoing logs, and for documenting information about the outgoing shipments.

  


There also are various reporting tools and printouts.

  


This Solution has been given the nickname "EZ Tally".

  


Development Specification

Project Name: EZTally

Subdomain: eztally.apphosting.zone 

3LC: ZET

  


  


Link to draft on Google Docs (shared with clients): [https://docs.google.com/document/d/12KkuJIg4rwgnnqXymHqFkrkn8NSt8qkh/edit](https://docs.google.com/document/d/12KkuJIg4rwgnnqXymHqFkrkn8NSt8qkh/edit) 

  


Tim Reitz 08/30/2022: Note: EZ Tally is used elsewhere (e.g. [https://ezmileageclub.com/](https://ezmileageclub.com/), [https://ezmileageclub.freshdesk.com/support/solutions/36000114244](https://ezmileageclub.freshdesk.com/support/solutions/36000114244)).

  


  


TODO_TR: update snippets to include more details:

  * Records: required, field type
  * Reports:
    * Columns: linkage, totals,
    * Filters: required, field type, defaults, etc
    * each record to specify conditions for Copy, Delete, Merge
  * Permissions


