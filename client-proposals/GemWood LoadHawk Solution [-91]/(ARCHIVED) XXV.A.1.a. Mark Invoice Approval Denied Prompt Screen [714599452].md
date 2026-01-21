25.1.1.1. Mark Invoice Approval Denied Prompt Screen

  


Requirements

This is a special prompt screen that opens from a link on the "Salesperson Invoice Review Email". Note that the Salesperson needs to be logged into the Solution on whichever device he uses to receive the email and mark it as approved/denied.

  


It contains the following:

  


  * Std Mark Invoice Approval Denied (screen header; standard)
  * Are you sure you want to run this import? (on-screen message; standard)
  * Import: <import path> (on-screen message; standard)
  * Approval Denied Comments (multi-line plain text field; defaults to the current entry in the "Approval Denied Comments" field on the selected Delivery Ticket)
  * Run Import (button; initiates the "Mark Invoice Approval Denied" background process - see corresponding spec) 



  


_EM: Tim Reitz 12/04/2024: Anything else needed for this spec? And where is the best place to locate it in the proposal?

_VA: Tim Reitz 12/04/2024: Make this a shared x30 for both (but can have separate links). Opening the link opens an ask prompt screen.

  * Approved? (drop list of "Yes" / "No")
  * Approval Denied Comments (visible and required if "Approval" = "Denied"; multi-line plain text...)
  * Run Import



Sets the checkboxes parallel to the Yes/No and the comments.

  


_VA: Tim Reitz 12/04/2024: Merge this with the other subsection.

  


Development Specification

Tim Reitz 12/04/2024: This is a simple x30.
