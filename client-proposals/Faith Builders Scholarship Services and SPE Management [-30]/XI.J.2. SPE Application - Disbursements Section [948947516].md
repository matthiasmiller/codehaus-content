11.10.2. SPE Application - Disbursements Section

Disbursements:

Embedded spreadsheet (RG):

Columns:

  * Payee (drop-list of Scholarship Organization contacts; required)
  * Check Number (required)
  * Check Date (required)
  * Amount (required)



Buttons:

  * "+" \- insert row
  * "-" \- delete selected row



  


  * Funded (checkbox; auto-set and read-only; checked if Total Admitted is non-zero and is equal to Total Disbursements)
  * Total Disbursements (auto-calculated and read-only; sum of the Amount column in the RG)
  * Total Admitted (auto-calculated and read-only; total amount for all admitted member applications for the current record)
  * Total Accepted by SPE (auto-calculated and read-only; total amount for all accepted member applications for the current record)



  


Validation:

  * In the RG:
    * Warning on save: if Check Date does not fall within the selected tax year.
      * Warning Message: "Disbursement check date does not match the tax year. (Field: Check Date; <RowName>)"
    * Warning on save: if the sum of the Amount column does not match the sum of all designations on SPE Member Applications for the current record.



_TR Austin Priest 10/09/2024: I don't understand this one. Either it is not working or the wording is messed up. Trying on this record.

[https://testfbspe.apphosting.zone/Detail/Edit/2?RecordType=SPEApplications&NumberID=-161&State=0dmleaH-q~Q&](https://testfbspe.apphosting.zone/Detail/Edit/2?RecordType=SPEApplications&NumberID=-161&State=0dmleaH-q~Q&)

I can't seem to make this message go away "Total disbursement for "AA Scholarship Org #0921" does not match with the total contribution. (Field: Amount; Row: AA Scholarship Org #0921)"

TODO_NM: Tim Reitz 02/24/2025: Could you take a look at this?
