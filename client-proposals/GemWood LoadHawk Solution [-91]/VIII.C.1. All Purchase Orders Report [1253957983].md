8.3.1. All Purchase Orders Report

  


Requirements

Overview: This is a custom two-pane report of all Buyer Purchase Order records in the Solution, with various filters. This is a "master" report, used to generate various other reports. 

  


Accessed from: 

  * Main Menu | Buyers | All Buyer Purchase Orders (opens the report directly, bypassing the filter screen)
  * Other menu options and/or report links



  


Title: Buyer Purchase Orders

  


Left Pane:

Columns: 

  * Buyer 
  * Buyer's PO # (link to open the record) 
  * PO Date 
  * Description 
  * Close Type
  * Replaced By (displays in red for PO's with "Status" = "Open")
  * Target # Loads 
  * Remaining Loads 
  * Attached PDF (link to open the attached Purchase Order PDF, when applicable; displays as "View PDF") 
  * Closed / Canceled Date 



  


Grouped by: Status (Open, Closed, Canceled)

  


Sorted by: 

  * First by: PO Date (most recent at the top) 
  * Second by: Buyer's PO # (alphabetically) 



  


Filters: 

  * PO Date Start (date; defaults to blank = all)
  * End (date; defaults to blank = all)
  * Buyer (optional; drop list of active Buyer-type Contacts; filters down as you type; defaults to blank = all) 
  * Buyer's PO # (optional; drop list of Buyer's PO #s for the selected Buyer in the following format: "<Buyer's PO #> (<PO Date>, <Buyer>)"; filters down as you type; defaults to blank = all)
  * Only Ready to Close (checkbox; defaults to not checked; if checked, the report displays only Open PO's that need to be closed; specifically: 
    * If "Close Type" = "Load-Based": "Status" = "Open" and "Remaining Loads" on the Purchase Order = "0" or negative; or  
    * If "Close Type" = "Date-Based": "Status" = "Open" and "Replaced By" on the Purchase Order not blank)
  * Status (optional; drop list of "Open / Closed / Canceled" list options and blank = all; defaults to "Open"; hidden if "Only Ready to Close" is checked)



  


Buttons: 

  * New Buyer PO (opens a blank new Purchase Order record)
  * Close Selected PO's (sets the "Closed" checkbox to checked for any selected "Open" Purchase Order records from the report) 



  


  


Right Pane: This is the "Delivery Tickets by PO" report (see corresponding spec), filtered to the most recently-selected Purchase Order in the left pane.

  


  


Menu Visibility: All users

  


Other Notes:

  * Rows with Status = "Closed" or "Canceled" are displayed in gray font.
  * This report is used as a "master report", run with various filter configurations for one or more other reports.



  


Development Specification

Mockup: [https://docs.google.com/spreadsheets/d/16F1i-TW_yIluSY_9LGCvitW-lurcpcU5JFg9O1Gct4I/edit?gid=2134231898#gid=2134231898](https://docs.google.com/spreadsheets/d/16F1i-TW_yIluSY_9LGCvitW-lurcpcU5JFg9O1Gct4I/edit?gid=2134231898#gid=2134231898)

Tim Reitz 01/04/2025: Updated. 

  


Change Requests:

  * Ben Reitz 10/09/2025: [[[IN12126](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-12128&)]] - ZGW - Add "GW Purchase Orders" Feature
  * 


  


Ellis Miller 12/18/2024:

  


Ask Prompts:

[ ] Buyer - use ActiveContactsByType

[ ] Buyer's PO - We will want POByBuyerDatePO.ndx (4-byte Buyer Contact List Num + 4-byte PO Date + 20 PO ID). This depends on Buyer ask prompt. Call NdxConcat. If Buyer is blank, use NdxAllKeys, otherwise use the Buyer ListNum + "...". Use a macro to construct the drop list text from the NdxKey parts so that we never have to hit the records at all (just NdxKey portions and ListString calls).

  


BID: 1 Day

  


TODO_PRICING: Tim Reitz 10/23/2024: Not included in official HLD estimate (we were expecting to completely do away with Purchase Orders).
