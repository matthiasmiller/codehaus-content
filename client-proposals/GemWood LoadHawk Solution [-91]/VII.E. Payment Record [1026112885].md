7.5. Payment Record

Overview: The Payment record is a custom record, and is used to track details about payments from Buyers to GemWood and from GemWood to Members. This is done via two separate "detail screens" or views, specific to the category:

  * Buyer Payment Detail Screen (also referred to as simply "Buyer Payment" or "Buyer Payment record")
  * Member Payment Detail Screen (also referred to as simply "Member Payment" or "Member Payment record")



  


Modification History: This contains the following standard features for modification tracking: 

  * Created: (name, date, and time stamp) 
  * Last Modified: (name, date, and time stamp)
  * Modification History (link to open the report for the record)



  


Data Access: 

  * Visibility: Visible to all users
  * Editability:
    * If "Status" ≠ "Complete" or "Canceled": Editable for users with the "Edit Payments" Permission
    * If "Status" = "Complete" or "Canceled": Only the following items remain editable, for users with the "Edit Payments" Permission (all other editable fields become read-only), utilizing the "Limited Editing Mode" feature:
      * Buyer Payment:
        * "Complete" checkbox (but note that its other editability condition(s) still apply)
        * "Canceled" checkbox (but note that its other editability condition(s) still apply)
        * Editable fields in the "Documentation" section
      * Member Payment:
        * "Complete" checkbox (but note that its other editability condition(s) still apply)
        * "Canceled" checkbox (but note that its other editability condition(s) still apply)
        * "Add'l Notes for Member Payment Email"
        * Editable fields in the "Documentation" section



  


Special Considerations:

  * Copy Record: Disallow (but note that the copy feature could be considered and added in the future)
  * Delete Record: Allow deletion if Status = "Canceled"
  * Merge Record: Disallow



  


Other Notes:

  * N/A


