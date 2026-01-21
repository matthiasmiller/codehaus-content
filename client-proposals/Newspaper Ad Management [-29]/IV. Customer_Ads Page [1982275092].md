4\. Customer/Ads Page

  


Requirements

The Customer/Ads Page will be based on AppHosting's built-in Contacts module, with heavy customizing to display customers and their ads, related tasks, linked contacts, and other information. This will be done in a 3-column layout, with the right-hand column probably being wider than the left-hand and middle columns. If a screen is not large enough to display all three columns, it will rearrange somewhat and shrink down to 2 columns. 

  


The Customer/Ads page will have a "Open Other Customer" option to open another Customer/Ads Page from one that is already open. See more details in the corresponding section of this proposal.

  


The Customer/Ads Page will have a Modification History link at the bottom. Clicking on this link opens the Modification History page, which displays creation and modification details for all data on the Customer/Ads Page.

  


Each login User will have a Customer/Ads Page as a contact page for internal linking and documentation.

  


The Main Menu will have a "New Customer" option that opens a new Customer/Ads Page.

  


Development Specification

Notes:

  * Note that John is trying to keep everything "at a glance". He doesn't like having buttons to click to open. He does feel like the current page is somewhat cluttered, so he would like to see if we can streamline it a bit. He has to see it to know if he'll like it or not. He thinks we should stick to the horizontal layout.
  * Most of the users would be using a 27" monitor. They all run dual monitors, with the ads management software open on one. 



Tim Reitz 12/08/2020: John has a 31" screen, most will run on 27"; he also 4K screens. He wants it to be standard for the standard 27" screen. 

Tim Reitz 03/23/2021: It looks like these are the two main resolutions for 27" monitors:

  * 1920x1080
  * 2560x1440



I'm not sure which ZPP is using, but we should probably try to get the three columns to fit on the smaller one. 

  * Tim Reitz 02/17/2021: I'm guessing that all the "warn on Save if blank" fields are going to be overwhelming / annoying once it's in action, especially if there are multiple ads in the works for the customer. But I guess it will settle down once they have the ad set up. 



  


  


Data Restrictions:

  * Full Admins: Full access
  * Publication Admins: Full access for assigned publication, but some items are Full Admin only
  * Standard Users: Full access for assigned publication, but some items are Full Admin only



  


This will probably use Organizations.
