6.4.1. View Tracts Report

  


Requirements

Overview: The View Tracts report shows Tracts, with various filters, including an option to view completed tracts.

  


Accessed from: Main | Tracts | View Tracts (bypasses the filter screen to open the report directly) 

  


Title: Tracts

  


Columns: 

  * Tract Name (link to record)
  * Landowners (all landowners for the tract, listed on separate lines)
  * Loggers (all loggers for the tract, listed on separate lines)
  * Purchase Type
  * Expiration Date
  * Forester (visible if "Purchase Type" filter = "Flat Payments")
  * State
  * County



  


Grouped by: (show only the ones for which the corresponding filter is selected)

  * Harvest Started
  * Harvest Paused
  * Contract Signed
  * Harvest Complete (in gray)
  * Quote
  * Archived (in gray)



  


Sorted by: Tract Name

  


Filters: 

  * Active Status (multi-select drop list of Harvest Started, Harvest Paused, Contract Signed, and Quote, keeping the same sequence as the groupings above; blank = all; default to only Harvest Started)
  * Show Archived/Complete (checkbox; defaults to cleared; if filled, Tracts with Status of Archived and Harvest Complete show on the report) 
  * Tract Name (if "Show Archived/Complete" is not filled, list of active Tract Names; if "Show Archived/Complete" is filled, list of all Tract Names; filters down as you type; defaults to blank = all)
  * Purchase Type (list of Tract Purchase Types; defaults to blank = all)
  * Landowner (list of Landowner-type Contacts; filters down as you type; defaults to blank = all)
  * Loggers (list of Logger-type Contacts; filters down as you type; defaults to blank = all)
  * Forester (visible if "Purchase Type" = "Flat Payments"; drop list of Forester-type contacts; filters down as you type; defaults to blank = all) 
  * State (list of abbreviations for States that are in use on Tracts; filters down as you type; defaults to blank = all)
  * County (list of Counties that are in use on Tracts; filters down as you type; defaults to blank = all)



  


Buttons: 

  * New Tract (opens a new blank Tract record)



  


Menu Visibility: Users with the Edit and Delete Tracts permission (menu option grayed-out for other users)

  


Other Notes:

  * N/A



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/1dTtbRX16DEGhyGuz1Hj0tnGKDl701ZDBgeaD-feIVoc/edit#gid=339938566](https://docs.google.com/spreadsheets/d/1dTtbRX16DEGhyGuz1Hj0tnGKDl701ZDBgeaD-feIVoc/edit#gid=339938566)

  


Ellis Miller 12/20/2022: 

[ ] Let's have the actual TractStatuses list be ordered as defined in the "Tract Detail Sections" (in chronological order). Use a macro to order the droplist and groupings here. 

[ ] Need to add ordering macro

[ ] Need to filter Archived and Show Complete out of list.

  


[ ] States helper list: AllTractStates -- Use a TractState.ndx with a BinString of the State field.

{ Convert to a pipe-list of list numbers and sort that to remove duplicates. }

Assign vUniqueListItems = SortPipeList(TractStateNdxConcat(NdxAllKeys, BinStringToNum(NdxKey)));

{ Convert to list values and sort those. }

SortPipeList( ListSubstitute( vUniqueListItems, ListString(....));

  


[ ] Counties helper list: AllTractCounties -- Do same thing as above.

  


BID: 1 Day because of complex helper lists
