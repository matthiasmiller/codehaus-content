8.1. Review Ads

  


Requirements

Before going to publication, all current ads should be reviewed. The "Review Ads" feature will allow a user to review the ads for a selected Publication Date.

  


Clicking on "Review Ads" opens a multi-pane report that defaults to the current Publication Date. It will show all ads that have a running scheduled for that date. 

  


Left Pane:

This pane shows all customers with at least one ad scheduled for the current Publication Date. If a customer has multiple ads for the current date, each ad will be on a separate line of this pane. 

  


It will have the following columns: 

  * Customer (link to the Customer/Ad Page; open on the same tab)
  * Ad Title
  * Publication (only visible for Full Admins; can be viewed by scrolling to the right)



  


This pane would have no grouping and would be sorted alphabetically by Customer.

  


It would have the following filters: 

  * Publication Date (default to current)
  * Customer (default to blank = all)
  * Publication (only for Full Admins; list of publications; default to blank = all)



  


Middle Pane:

This will show some of the ad information for the selected Ad Title. There will be 26 lines in this pane, to show a full year of publication dates for a bi-weekly publication. This would be the current publication date and the next 25 in the future, including ones not selected for running the ad.

  


It will have the following columns: 

  * Ad Size (editable, changes current and future scheduled runnings)
  * Ad Color (editable, changes current and future scheduled runnings)
  * Discount % (editable, defaults to whatever discount % is set on the Customer/Ads Page; editing here changes current and future scheduled runnings)
  * Publication Date (the current publication date in bold font and at the top of the list)
  * Run? (editable; checkbox; checking a box schedules the ad for that publication date; unchecking a box un-schedules the ad for that date)
  * Ad File Name (read-only)
  * Index Name (editable, changes current and future scheduled runnings)
  * Index Page # (editable on a per-Publication Date basis)



The main section of the pane will show to here; the user must scroll to the right to see the remaining columns: 

  * Ad Title (read-only)
  * Ad Price (editable)
  * Actual Ad Dimensions (read-only)
  * Special Placement Page Location (read-only)
  * Special Placement Page Number (read-only)
  * Charge for Special Placement? (read-only)



  


This pane would have no grouping and would sort by Publication Date.

  


Right Pane: 

This pane only shows one item:

  * Ad Image Preview (for the selected Ad Title; show the actual preview from the Ad Details)



  


Development Specification

Have a hidden editable macros on the ad Schedule that look up the Ad Size, Ad Color, and Multi-Run Discount % with OnChange expressions to update the Ads RG. 

  


Tim Reitz 03/23/2021: We need to see if we can get this to fit on a 27" screen without needing lef/right scrolling (adjusting font sizes, scaling down image preview, etc.).
