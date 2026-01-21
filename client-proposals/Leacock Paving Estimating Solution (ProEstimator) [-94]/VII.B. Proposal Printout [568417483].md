7.2. Proposal Printout

  


Requirements

Purpose/Overview: This is a customized, customer-facing PDF of the Proposal record. For Proposals that have not been marked as "Awarded", this includes all Groups on the Proposal, with their corresponding Sections. For Proposals that have been marked as "Awarded", this includes only the Groups that have been marked as "Awarded", with their corresponding Sections. This sometimes includes the "Customer Letter" as an additional page at the end.

  


Printed From: 

  * Draft Proposal PDF" link on the Proposal record
  * "Proposal PDF" link on the Proposal record
  * "Proposal + Customer Letter PDF" link on the Proposal record
  * Not automatically included in any emails for Phase 1 



  


File Format/Name: PDF:

  * If "Job Type" = "Residential": "Proposal <Proposal #> \- <Customer Last Name>, <Customer First Name> (<Customer Primary Address Line 1>; <Job Type>)"
    * Example: "Proposal 15001 - Byler, John (1234 Some St; Residential)"
  * If "Job Type" = any other: "Proposal <Proposal #> \- <Customer Name> (<Job Name>; <Job Type>)"
    * Example: "Proposal 15002 - ABC Builders (Ephrata Community Park; Commercial)" 



  


Fields to be Filled: 

  * Leacock Paving Info / Return Address section (hard-coded rather than filled; note that this information is visible in the top window of the window envelope - see corresponding envelope details):
    * Leacock Paving logo 
    * Return address, in the standard 2-line format:



"PO Box 5

Gordonville, PA 17529"

  * Leacock Paving phone number: "717-768-7281"
  * Leacock Paving website: "[www.leacockpaving.com"](http://www.leacockpaving.com") 



  


  * "Proposal Info" section ("Proposal" label):
    * "(DRAFT)" (visible immediately following the "Proposal" label if "Ready to Send to Customer" checkbox is not checked (i.e. if the printout is generated from the "Draft Proposal PDF" link)) 
    * Proposal # (displays the "Proposal #")
    * Proposal Date (displays the "Proposal Date")
    * Valid Through (displays the "Proposal Valid Through" date)
    * Sales Rep (displays the name of the Sales Rep, in the "FirstName LastName" format (not the Display Name))



  


  * "Customer Details" section:
    * Customer Name (no label; with the following details / behaviors: 
      * displays the name of the Customer: 
        * for Organizations: displays the "Name" from the Contact record (not the Display Name); 
        * for Individuals: displays the name from the Contact record in the "FirstName LastName" format (not the Display Name); 
      * visible in the lower envelope window \- see corresponding envelope details)
    * Customer Address (no label; displays the "Customer Address", in the standard multi-line format without the addressee name; visible in the lower envelope window \- see corresponding envelope details below)



  


  * "Job Details" section:
    * Job Name (no label; displays the "Job Name")
    * Job Address (no label; displays the "Job Address", in the standard multi-line format without the addressee name)



  


  * "Job Contact" section:
    * Job Contact Name (no label; displays the "Job Contact")
    * Job Contact Phone (no label; displays the "Job Contact Phone")
    * Job Contact Email (no label; displays the "Job Contact Email")



  


  * "Itemization" section:
    * "Standard Items" (table with the following:)  
      * Visibility/inclusion: 
        * if "Proposal Result" ≠ "Awarded", visible if there are any Groups for Sections with "Section Inclusion Type" = "Standard" in the "Groups" embedded spreadsheet on the Proposal record; 
        * if "Proposal Result" = "Awarded", visible if there is at least one Standard Group with "Group Awarded" checked; 
      * Table Heading: This heading has a dark yellow background (RGB: 243, 185, 44), with the column names;
      * Rows:
        * Includes a "Section heading" row for each included Section (see details in the "Section" column spec below), in the same sequence as the Groups embedded spreadsheet on the Proposal record.; 
        * Includes one row for each included Group, each under its corresponding Section (see details in the "Item" column spec below).;
      * Columns: 
        * Section (allows for text wrapping, if the displayed text is longer than the width of the column; displays the following:
          * for "Section heading" rows: displays Sections in bold font, for any Groups that should be included (see the spec for "Group" rows in the "Item" column below) in the following format:
          * for "Group" rows: displays checkboxes that correspond to the "Group Awarded" checkbox on the Groups embedded spreadsheet: unchecked if not awarded; checked if awarded;
          * for "Section Total" rows: N/A (blank) 
          * note that this spec is also used for the Section column on the Work Order printout)
        * Item (note that this displays Group details, but is labeled as "Items" here, since Groups are the itemization that the Customer sees; allows for text wrapping, if the displayed text is longer than the width of the column; displays the following:
          * for "Section heading" rows: N/A (blank);
          * for "Group" rows: displays Groups in standard font; with the following additional details:
            * in the following format: "<Group Description>";
            * with the following visibility conditions:
              * If "Proposal Result" ≠ "Awarded": Includes all Standard Groups from the Proposal;
              * If "Proposal Result" = "Awarded": Includes only Standard Groups with the "Group Awarded" checkbox checked; 
          * for "Section Total" rows: N/A (blank))
        * Amount ($) (displays the following:
          * for "Section heading" rows: N/A (blank);
          * for "Group" rows: displays the "Group Printout Price $" for the corresponding Group;
          * for "Section Total" rows: N/A (blank)) 
      * Standard Items Total ($) (same visibility as the "Standard Items" table (see spec above); with the following details: 
        * if "Proposal Result" = "Awarded": displays the sum of all "Group Printout Price $" values for the Standard Groups; 
        * if "Proposal Result" = "Awarded": this label is "Awarded Standard Items Total ($)", and the displayed value is the sum of the "Group Printout Price $" values for all "Awarded" Standard Groups) 



  


  


  * "Alternates" (table; like the "Standard Items" table, with the following differences: 
    * Visibility/inclusion: 
      * if "Proposal Result" ≠ "Awarded", visible if there are any Groups for Sections with "Section Inclusion Type" = "Alternate" in the "Groups" embedded spreadsheet on the Proposal record; 
      * if "Proposal Result" = "Awarded", visible if there is at least one Alternate Group with "Group Awarded" checked; 
    * Rows: 
      * Includes a "Section Total $" subtotal row for each included Section (see details in the "Item" and "Amount ($)" column specs below).;
    * Columns: 
      * Section: 
        * for "Section heading" rows: displays Sections in bold font, for any included Groups, in the following format: "<Section Inclusion Type> <Opt / Alt #>: <Section Name>"; example: "Alternate 1: Heavy Duty Paving"; 
      * Item: 
        * for "Group" rows: has the following visibility conditions:
          * If "Proposal Result" ≠ "Awarded": Includes all Alternate Groups from the Proposal;
          * If "Proposal Result" = "Awarded": Includes only Alternate Groups with the "Group Awarded" checkbox checked; 
        * for "Section Total" rows: displays "<Section Inclusion Type> <Opt / Alt #> Total", aligned to the right-hand side of the column; 
      * Amount ($): 
        * for "Section Total" rows: displays the "Section Total $" for the corresponding Section)
    * Awarded Alternates Total ($) visible if there is at least one Alternate Group with "Group Awarded" checked; displays the sum of the "Group Printout Price $" values for all "Awarded" Alternate Groups)



  


  


  * "Options" (table; like the "Alternates" table, with the following differences:)  
    * Visibility/inclusion: 
      * if "Proposal Result" ≠ "Awarded", visible if there are any Groups for Sections with "Section Inclusion Type" = "Option" in the "Groups" embedded spreadsheet on the Proposal record; 
      * if "Proposal Result" = "Awarded", visible if there is at least one Option Group with "Group Awarded" checked; 
    * Columns: 
      * Section: 
        * for "Section heading" rows: displays Sections in bold font, for any included Groups, in the following format: "<Section Inclusion Type> <Opt / Alt #>: <Section Name>"; example: "Option 1: Heavy Duty Paving"; 
      * Item: 
        * for "Group" rows: has the following visibility conditions:
          * If "Proposal Result" ≠ "Awarded": Includes all Option Groups from the Proposal;
          * If "Proposal Result" = "Awarded": Includes only Option Groups with the "Group Awarded" checkbox checked; 
        * for "Section Total" rows: displays "<Section Inclusion Type> <Opt / Alt #> Total", aligned to the right-hand side of the column; 
      * Amount ($): 
        * for "Section Total" rows: displays the "Section Total $" for the corresponding Section)
    * Awarded Options Total ($) (visible if there is at least one Option Group with "Group Awarded" checked; displays the sum of the "Group Printout Price $" values for all "Awarded" Option Groups)



  


  


  * "Proposal Details" section (no label; located below the Itemization table):
    * Total Awarded Items ($) (visible if "Proposal Result" = "Awarded"; displays the "Total Proposal Price $")
    * "A <value of "Proposal Deposit %" from Silverloom Settings>% deposit is due with acceptance." (text; visible if "Deposit Required" is checked) 
    * Deposit ($) (visible if "Deposit Required" is checked and "Proposal Result" = "Awarded"; displays the "Deposit Amount $") 
      * Note that the location of this field has been changed -- see the mockup. 
    * Oil Index (no label; displays the "Proposal Oil Index" from the Proposal, in bold font) 



  


  * "Unit Price Details" section (visible if the "Include Unit Price Details" checkbox is checked):
    * Unit Price Details (no label; displays the contents of the "Unit Price Details" field) 



  


  * "Proposal Notes" section:
    * Proposal Notes (no label; displays the contents of the "Proposal Notes" memo)



  


  * "Terms & Conditions" section:
    * Terms & Conditions (no label; displays the contents of the "Proposal Terms and Conditions" memo from Silverloom Settings)



  


  * "Customer Letter" section: Includes the "Customer Letter Printout" text as a separate page at the end of this printout, when generated from the "Proposal + Customer Letter PDF" link on the Proposal record. Note that this is coded separately from the main "Customer Letter" Printout, so changes made there should be made to this page as well. 



  


  


Handling Page Breaks: This printout sometimes extends beyond a single page; in those cases, the following guidelines are considered:

  * Main Proposal printout:
    * Itemization section: Can split between any rows, but do not split a row (i.e. if the text is long enough to wrap to multiple lines);
    * Other sections: Can split between sections, but do not split the sections (i.e. proposal details, memo contents, etc.)
  * "Customer Letter" portion: See "Customer Letter Printout" spec for details



  


  


Other Notes:

  * Note that printout templates may be subject to limitations of the PDF templating library. CCI will communicate with the client in places where the template library requires significant changes from the original design.
  * Includes page numbers at the bottom of the page, in the "Page __ of __" format. 
  * Includes the default "Powered by Silverloom Business Suite" footnote at the bottom of the page.



  


Development Specification

Change Requests: 

  * Tim Reitz 11/11/2025: [[[IN12288](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-12290&)]] - ZLP - Phase 1 - Proposal Printout Changes
  * 


  


  


Mockup: 

  * Docs: [https://docs.google.com/document/d/1-PwL9TmMTSrQa83v72NqHUNh9HsJFHTyaNsp2DFQYTU/edit?tab=t.0](https://docs.google.com/document/d/1-PwL9TmMTSrQa83v72NqHUNh9HsJFHTyaNsp2DFQYTU/edit?tab=t.0)
    * Note that the layout in the mockup is approximate and will need to be adjusted to match the specified envelope window measurements. 



Tim Reitz 11/11/2025: See the updated mockups PDFs: 

  * Proposal Printout Mockup 11-11-25 (not awarded): [https://drive.google.com/file/d/1TuaeflQ3c-pZQHKW3nCtu143ynjiLqsl/view?usp=sharing](https://drive.google.com/file/d/1TuaeflQ3c-pZQHKW3nCtu143ynjiLqsl/view?usp=sharing) 
  * Proposal Printout Mockup 11-11-25 (awarded): [https://drive.google.com/file/d/1J24arJNAi5KxAzHeY2cV3dq8ynRDMah0/view?usp=sharing](https://drive.google.com/file/d/1J24arJNAi5KxAzHeY2cV3dq8ynRDMah0/view?usp=sharing)



  


  


  * Sheets (old): [https://docs.google.com/spreadsheets/d/17EkeRk4ZweyAWVPRgcPgdjPlGqZpSTkrt-jl4uNLh90/edit?gid=1892281902#gid=1892281902](https://docs.google.com/spreadsheets/d/17EkeRk4ZweyAWVPRgcPgdjPlGqZpSTkrt-jl4uNLh90/edit?gid=1892281902#gid=1892281902)



  


Samples from the client: 

  * [https://drive.google.com/drive/folders/1JMICvruaxi8hSLQQyCsVMyBVFrIhsbil](https://drive.google.com/drive/folders/1JMICvruaxi8hSLQQyCsVMyBVFrIhsbil). 
  * #2: 



  


Ellis Miller 06/17/2025: 

NOTE: Formatted similarly to an invoice/estimate.

  


NOTE: If you see ways to simplify this, let us know.

  


[ ] For the yellow header on the Itemization table, use the following yellow color: 

  * #F3B92C 
  * RGB: 243, 185, 44



  


[ ] Use AlignRight for "Section Total" in the Item column.

  


BID: 4 DAYS
