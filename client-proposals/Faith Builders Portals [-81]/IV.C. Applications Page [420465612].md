4.3. Applications Page

Filters:

  * Application (droplist of all SPE Business Applications for the business, displaying the application date; if there are multiple applications for a single date, letters such as a, b, and c will be appended to the date to avoid duplicates.)



  


Additional Fields:

  * Commitment Year (read-only display of the Year # field from the Member Application record)
  * Status (read-only display of the Application status: Completed, Denied, Awaiting payment, Approved, In progress)
    * TODO_JB: which statuses should allow editing? 
  * Payment Request Date (read-only display of the Payment Due Date field from the Member Application record.



  


Link to Secure Handoff (visible if the Status = "Awaiting Payment")

  * There will be a note at some point in the handoff alerting the user that the Status will not change immediately after submitting payment.



  


Fields displayed above the School Designations table:

  * Total Contribution (displays the sum of the Amount column)
  * Est. Tax Credit (displays 90% of the Total Contribution amount)



  


Columns in School Designation table: (editable until the application is paid)

  * School (droplist of all schools not currently in the designation table, as well as "Other school")
  * School Name (fillable and required if "Other school" is selected)
  * School Contact Name (fillable and required if "Other school" is selected)
  * School Contact Phone (fillable and required if "Other school" is selected)
  * School Contact Email (fillable and required if "Other school" is selected)
  * Amount (read-only)



  


Joinder Agreement:

  * Only visible for unpaid year 1 of 2 applications.
  * Becomes visible if the total contribution amount changes from the last time the joinder agreement was completed.
  * Filling out the joinder agreement and clicking save will fill the new Joinder Agreement Filed field on the Member Application record.



  


Notes:

  * Designations are only editable for unpaid applications.
  * Total Contribution amount is only editable for unpaid applications that are not year 2 of 2 applications.
  * Error displayed if the designations don't add up the the Total Contribution amount.


