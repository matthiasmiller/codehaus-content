5.5.1. Invoice - Header Section

  


Requirements

  * "Header" standard section:
    * Invoice #<#> (located in the section header as the section label; number; auto-set sequentially; read-only; this number is the unique identifier for the record) 
    * Contact (required; drop list of all active Contacts)
    * Address (line 1; plain text; auto-sets to the primary address for the selected Contact, but remains editable)
    * ... (ellipsis button; opens a choice report to select an address from the selected Contact)
    * Line 2 (plain text; auto-sets to the primary address for the selected Contact)
    * City (plain text; auto-sets to the primary address for the selected Contact)
    * State (no label; drop-list of state abbreviations; auto-sets to the primary address for the selected Contact)
    * Zip (no label; plain text field for zip code; auto-sets to the primary address for the selected Contact)
    * Ship to Separate Address (checkbox; displays a second, identical set of address fields)
    * Invoice Date (required; date; defaults to the current date)
    * Status (required; drop list of "Canceled" / "Draft" / "Invoiced" / "Paid"; with the following details / behaviors: 
      * defaults to "Draft"; 
      * when set to "Paid", "Payment Date" is set to the current date)
    * Payment Date (date; required if "Status" = "Paid"; auto-sets to the current date when Status is set to "Paid"; does not auto-clear) 



  


  * Fund (custom; hidden; required, with the following behaviors: 
    * for auto-created invoices: read-only; auto-sets to the "Contact Fees Fund" or "Vehicle Fees Fund" for all rows in the Itemization embedded spreadsheet for the Invoice (note that this means that each Invoice is for items for a single Fund; 
    * for manually-created invoices: required; drop list of active Funds; editable by Admin users; set by the editable "Originating Fund" macro - see corresponding spec) 
  * Originating Fund (custom; macro; with the following behaviors: 
    * for auto-created invoices: 
      * if "Fund" is blank: displays the "Agent Fund" for the Agent of the current Invoice "Contact";
      * if "Fund" is not blank: displays the contents of the "Fund" field;
    * for manually-created invoices: editable; drop list of active Funds; editable for Admin users; sets the hidden "Fund" field) 
  * Current Agent (custom; read-only macro; dynamically displays the current Agent for the Invoice "Contact", updating any time the client's Agent changes) 



_CCI1: Tim Reitz 07/29/2025: Could you confirm whether the above 3 custom items are specced correctly? 

Murshid Rahman 08/19/2025: There is no "Fund" so basically there are 2 items. "Originating Fund" and "Current Agent" looks correct.

_CCI1: Tim Reitz 08/26/2025: Thanks for reviewing this! I do have a question: What field does "Originating Fund" set when editable? I think I was assuming there was a hidden stored field for it.

Murshid Rahman 09/03/2025: Apologies. There is actually a hidden fund stored field which I have missed earlier. So the spec might be something like below. Please edit as you like. 

  * Fund (custom; hidden; required, with the following behaviors: 
    * for auto-created invoices: read-only; auto-sets to the "Contact Fees Fund" or "Vehicle Fees Fund" for all rows in the Itemization embedded spreadsheet for the Invoice (note that this means that each Invoice is for items for a single Fund; 
    * for manually-created invoices: required; drop list of active Funds; editable by Admin users; set by the editable "Originating Fund" macro - see corresponding spec) 



  


Rest two customs look good.

  


TODO_VA: Tim Reitz 09/15/2025: Follow up.

  


Development Specification

Change Requests: 

  * Tim Reitz 07/29/2025: [[[IN10689](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10691&)]] - ZWA - Invoice Record - Clarify Agent and Fund Fields
  * Tim Reitz 08/23/2025: [[[IN9943](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9945&)]] - ZWA - Pre-ZWW - Vehicle Record - Fees & Credits - Add "Dismiss" Option for Fees



  


  


TODO_VA2: Tim Reitz 08/26/2025: Can fill out the specs for the Address choice reports once we have those fleshed out in the Snippet.
