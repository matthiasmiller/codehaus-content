7.4.10. Delivery Ticket - Additional Details Section

  * Additional Details section:
    * Delivery Ticket Canceled (checkbox; with the following details: 
      * editable for users with the "Manage Financials" Permission; 
      * when checked, the "Canceled by User & Date" field below is set; 
      * read-only if the "Closed" checkbox is checked; 
      * validation error on the field if there are any non-Canceled Member Payments or Buyer Payments linked to the Ticket: "Ticket cannot be canceled because there are non-Canceled Member and/or Buyer Payments linked to it." (note that an error on the field is used instead of making this read-only so that the user can have an explanation for why it cannot be canceled in this situation); 
      * validation warning on Save if this is checked and "Remaining Loads" for the PO is not 0: ""Remaining Loads" for the PO is not 0. Please review the PO and re-open if necessary.")
    * Canceled by User & Date (no label; read-only macro; with the following details: 
      * visible if the "Canceled" checkbox is checked; 
      * displays details about the user who checked the checkbox, as well as the date and time when the checkbox was checked, in the following format: "<User ID> <mm/dd/yyyy h:mm:ss> <AM/PM>")



  


  * Other Notes: 
    * The standard "Created" and "Last Modified" fields and "Modification" link at the bottom of the record screen display as part of this section.


