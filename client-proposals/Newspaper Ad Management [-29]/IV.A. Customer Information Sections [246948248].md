4.1. Customer Information Sections

  


Requirements

The following information needs to be tracked for Customers. Only the Customer Name and Publication should be required (error on Save if left blank). Some fields will show warnings on Save if blank, and some will not give any warnings if left blank.

  


Contact Section:

  * Active (checkbox; do not allow deactivation for Customers with current or future scheduled ads or with unpaid invoices or with remaining prepay credit)
  * Customer Name (required; text field)
  * Display Name (read-only; auto-filled from Customer Name, with the Publication Code added to the end)
  * Override Name (checkbox; when checked it allows editing the Display Name; still requires the Publication Code to be included at the end)
  * Primary Contact (warn on Save if blank; text field)
  * Publication (required; default to current publication and read-only for Standard and Publication Admin users; only editable for new records for Full Admin, defaulting to blank) 



  


Address Section:

  * Address Type (warn on Save if blank; default to Billing; editable)
  * Address (warn on Save if there is not at least one address specified; includes Address Line 1, Address Line 2, City, State, Zip)



  


Phone Section:

  * Phone and Fax
    * Phone 1 (warn on Save if blank; list of types to include Primary & Secondary; extensions could be added to the number field or to the Notes)
    * Phone 2 (optional; list of types to include Primary & Secondary; extensions could be added to the number field or to the Notes)
    * Fax (optional; if Fax phone type is selected, automatically make sure "1" is included on the front of the standard 10 digits) 



  


Email Section:

  * Email to Fax (if a Fax number has been entered; automatically shows the Fax number in email format @send.myfax.com; link to open fax email)
  * Email (optional)
  * Login Email (for system users; auto-filled)



  


Customer Information Section:

  * Invoice Preference (warn on Save if blank; choice of Email, Print, Fax; show an error if there is not a valid email address if Email is selected or a valid fax number if Fax is selected)
  * Discount Description (optional; drop list of all Discount Sales Items for the publication to which the Customer is assigned)
  * Discount % (auto-fill from Description; editable to override the default amount; applies to all ads for the Customer; these discounts are not run on individual ads or publication-wide, but the price for a specific ad can be changed on that ad's details)
  * Apply Discount (button; selecting this button will apply the current Discount % to all current and future scheduled runnings for the customer; this can then be edited on a per-run basis if desired)
  * Ad History (link; opens a new tab with a report that shows all past ads for that Customer - see the Ad History Report details in the Reports section of this proposal)
  * Manage Payments (link; opens separate tab to view and edit information for stored cards or add a new card or make a payment; see more details in the Payments section of this proposal)
  * Auto-Pay Invoices (read-only, auto-filled from the Manage Payments page; if checked, show the selected auto-pay card in the "Type Last 4, Exp" format)



  


Prepay/Credit Section: See more details in the corresponding section of this proposal. 

  


Invoices Section: This would be the standard AppHosting Invoices section, but it would also include the following customizations:

  * Statement (link to generate and view the current statement for the customer (PDF))
  * Email/Fax Invoices & Ad Images (see details in the Email/Fax Invoices & Ad Images section of this proposal)
  * Email/Fax Statement (see details in the Email/Fax Statements section of this proposal)



  


  


Misc. Notes:

  * The Customer Name will be tracked and displayed elsewhere in the database, but Primary Contact names and Linked Contacts are stored on the Customer page and will not be connected with any other contacts or records. However, they will show up on the All Contacts report (see the details of that report in this proposal).



  


  * Displayed Customer names will include the Publication Code for their assigned publication. For example, customers in the ads management for Gemeinde Brief would be saved in a format like "Timothy B Reitz [GB]" or "CodeCrafters, Intl. [GB]".



  


Development Specification

For Email to Fax: We should use a macro to format the number correctly, then after the number we should autofill "@send.myfax.com" and create a link. 

Matthias Miller 12/15/2020: We have a macro that formats a number as a 10-digit number (forget exactly where it is).

  


Include validation for valid email (if Invoice Preference = Email) or fax number (if Invoice Preference = Fax).

  


Tim Reitz 02/03/2021: Cache the associated Publication on all records that are linked to a Contact. This is required for restricted data. We will ensure that Publication is read-only on saved Contacts.
