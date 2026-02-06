4.3. Tax Return PDF Documents

  


Requirements

This is included in the "Tax Return PDF Documents with Automation" proposal price. System automation will split the Tax Return PDF into separate pages with fielded text. It will optionally create separate member PDF's with redacted SSNs and EINs to provide to members. This is split out separately as "Creating Redacted PDF's". This option is currently listed with a price range. If Faith Builders is interested in pursuing this option, we will do further research to provide a fixed cost proposal.

  


This record will track the PDFs for each tax year. It will have these primary fields:

  * SPE (required)
  * Tax Year (required)
  * Original Tax Form PDF (required)
  * Ready to Process (checkbox, after PDF is uploaded)



  


Duplicate records for the same SPE and tax year are not allowed.

  


When the Ready to Process checkbox is checked, the PDF will be split into multiple parts (one redacted PDF per member). These will be stored on this record.

  


This will validate that:

  * The list of members in the PDF matches the all admitted members for that SPE and tax year (matching by SSN/EIN).
  * The Contribution Amount and Tax Credit Amount matches all approvals for the member within the SPE for that tax year.



  


The redacted PDFs will mask SSNs and EINs with "XXX-XX-1234" and will be sent out by email.

  


The redacted PDF file names will be "MemberName SPE TaxYear.pdf".

  


Faith Builders will supply a sample PDF for development purposes.

  


Development Specification

We will have settings for:

  * Number of Pages Per Section (number field)
  * Member Name (takes parameter with Section Text)
  * Validate Section (takes parameter with Section Text)



Target: 2 days

  


The Validate Section will use the section text to determine the member, then look up the applications, and search the text to confirm the contribution and tax credit amounts match.

  


Ellis Miller 02/08/2021: 

[ ] Detail screen: according to layout

[ ] Custom DB Level with numeric ID's

Josh will give us a generic "PDF Document" record. This extracts the text out of a PDF (it wouldn't work with a PDF full of images -- this is not OCR)

[ ] SPE and Tax Year are FB-specific fields added to this record.

[ ] First set of fields are simple with Required: True.

[ ] Original Pages RG

The main RG is supplied by Josh. We add columns for Section and Macro.

[ ] The section and member are auto-evaluated macros.

[ ] What happens if the validation fails (no member or amounts don't match)? We will show an error on screen: "The final output cannot be generated because...."

[ ] Validation: for duplicate items. Need FormsBySpeAndYear.ndx

[ ] TODO_CH: Add Contribution Amount and Tax Credit Amount on the mockups.

Target: 3 days

  


[ ] Default Validation Expressions

Target: 1-5 days?? Bidding at 3.5 because of uncertainty.

  


[ ] PDF to Text:

[ ] User attaches, checks checkbox, and saves. Josh, consider warning if attachment without checkbox.

[ ] This is a generic record that hits a generic trigger to turn PDF into text.

[ ] Josh will save the text into the RG.

[ ] We will then run validation and if it clears, we will produce the redacted PDF's and attach those using Josh's script.
