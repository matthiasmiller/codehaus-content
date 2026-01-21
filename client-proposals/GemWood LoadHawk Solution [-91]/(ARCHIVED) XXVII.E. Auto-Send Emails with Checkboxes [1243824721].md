27.5. Auto-Send Emails with Checkboxes

  


Requirements

Sean Miller 04/29/2025: Moved to [[[IN11422](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11424&)]] - ZGW - Auto-Send Emails with Checkboxes

  


  


The feature to auto-send emails on Save can be done for about $500-600 per email (in addition to the normal cost).

  


1\. Buyer Invoice Email: We had specced this out to automatically send the Buyer Invoice Email once the "Invoice Approved" checkbox was checked, with various additional features. We're now splitting this out as an optional add-on to help give more opportunities to reduce cost.

  


Estimated Cost: $500-600

  


Spec:

  


Item 1: Delivery Ticket Record:

  * Send Buyer Invoice Email on Save (visible if the selected Buyer Contact has at least one email address; checkbox; defaults to not checked; with the following special behaviors: 
    * editable if "Invoice Approved" is checked; 
    * is auto-checked when the "Invoice Approved" checkbox is checked; 
    * when checked, the "Buyer Invoice Email" is sent automatically on the first Save after it is checked; 
    * when the "Email Sent On" date is set, the label changes to "Resend Buyer Invoice Email on Save" and the checkbox is automatically unchecked, to prepare for another future send if desired; 
    * if manually unchecked, the email is not sent on Save, with a warning on Save if not checked when "Email Sent On" is blank: "Email will not send until the "Ready to Send" checkbox is checked.";
    * changes made here should be considered for the corresponding checkbox for the "Member Payment Issued Email" as well)  
  * "Invoice will be sent to the Buyer when "Save" is clicked." (message in orange text; visible if the "Send / Resend Buyer Invoice Email on Save" checkbox is checked and the record has not been saved since checking the checkbox) 



  


  * Buyer Invoice Email Body (visible if the selected Buyer Contact has at least one email address; button; opens a child screen with an editable "Email Body" memo that defaults to the text from the "Default Buyer Invoice Email Text" from Silverloom Settings, with expressions already evaluated; memo can include expressions; memo; can be edited by the user to customize the text on a per-Ticket basis) 
    * Note that this design could optionally be included instead of the existing "Additional Notes..." feature for emails. This approach is more expensive, but allows the user to view the email before sending. 
  * Email Sent On (visible if the selected Buyer Contact has at least one email address; auto-set and read-only; date; defaults to the current date when the "Buyer Invoice Email" is sent; if sent multiple times, this shows the most recent send date) 



  


  * Email Merge:



Overview: This email merge is used to send the Buyer Invoice after the Delivery Ticket has been entered into the Solution. This is sent from the Delivery Ticket record, on the first Save after the "Send / Resend Buyer Invoice Email on Save" checkbox is checked.

  


  


Item 2: Delivery Ticket Closed Email:

  


Estimated Cost: $500-600

  


Spec:

  * Delivery Ticket Record:
    * Send Delivery Ticket Closed Email on Save (visible if the "Closed" checkbox is checked; checkbox; with the following special behaviors:
      * is auto-checked when the "Closed" checkbox is checked;
      * when checked, the "Delivery Ticket Closed Email" is sent automatically on the first Save after it is checked;
      * when the "Email Sent On" date is set, the label changes to "Resend Delivery Ticket Closed Email on Save" and the checkbox is automatically unchecked, to prepare for another future send if desired; 
      * if manually unchecked, the email is not sent on Save, with a warning on Save if not checked when "Email Sent On" is blank: "Email will not send until the "Ready to Send" checkbox is checked.") 
    * Email Sent On (visible if the "Closed" checkbox is checked; auto-set and read-only; date; set on save to the current date when the "Delivery Ticket Closed Email" is sent; if sent multiple times, this shows the most recent send date) 
    * Delivery Ticket Closed Email Body (visible if the "Closed" checkbox is checked; button; opens a child screen with an editable "Email Body" memo that defaults to the text from the "Default Text for Delivery Ticket Closed Email" from Silverloom Settings, with expressions already evaluated; memo can include expressions; memo can be edited by the user to customize the text on a per-Ticket basis)
      * Note that this design could optionally be included instead of the existing "Additional Notes..." feature for emails. This approach is more expensive, but allows the user to view the email before sending. 
    * "Delivery Ticket Closed email will not be sent to the Member when "Save" is clicked." (visible if the "Closed" checkbox is checked and the "Delivery Ticket Closed Email is Ready to Send" checkbox is checked and "Email Sent On" is blank; message in orange text) 
    * "Delivery Ticket Closed email will not be sent to the Member." (visible if the "Closed" checkbox is checked and the "Delivery Ticket Closed Email is Ready to Send" checkbox is not checked and "Email Sent On" is blank; message in orange text) 



  


  * Email Merge:



Overview: This email merge is used to notify a Member that a Delivery Ticket has been marked as "Closed". It is sent from a Delivery Ticket record, on the first Save after the "Send / Resend Delivery Ticket Closed Email on Save" checkbox is checked.

  


  


Item 3: Member Payment Issued Email:

  


Estimated Cost: $500-600

  


Spec:

  * Member Payment Record:
    * "Payment will be marked as Closed and the Member Payment email will be sent to the Member when "Save" is clicked." (message in orange text; visible before the first Save for the record if the "Send Member Payment Issued Email on Save" checkbox is checked) 
    * "Payment will be marked as Closed when "Save" is clicked, and the Member Payment email will not be sent to the Member." (message in orange text; visible before the first Save for the record if the "Send Member Payment Issued Email on Save" checkbox is not checked) 



  


  * Member Payment Issued Email Body (button; opens a child screen with an editable "Email Body" memo that defaults to the text from the "Default Text for Member Payment Issued Email" from Silverloom Settings, with expressions already evaluated; memo can include expressions; memo can be edited by the user to customize the text on a per-Ticket basis) 
    * Note that this design could optionally be included instead of the existing "Additional Notes..." feature for emails. This approach is more expensive, but allows the user to view the email before sending. 
  * Send Member Payment Issued Email on Save (checkbox; defaults to checked; with the following special behaviors:
    * when checked, the "Member Payment Issued Email" is sent automatically on the first Save after it is checked;
    * when the "Email Sent On" date is set, the label changes to "Resend Member Payment Issued Email on Save" and the checkbox is automatically unchecked, to prepare for another future send if desired; 
    * if manually unchecked, the email is not sent on Save, with a warning on Save if unchecked when "Email Sent On" is blank: "Email will not send until the "Ready to Send" checkbox is checked.";
    * changes here should be considered for the corresponding checkbox for the "Buyer Invoice Email" as well) 
  * Email Sent On (auto-set and read-only; date; defaults to the current date when the "Member Payment Issued Email" is sent; if sent multiple times, this shows the most recent send date) 



  


  * Email Merge:



Overview: This email merge is used to notify a Member that payment has been issued. It is sent from a Member Payment record, on the first Save after the "Send / Resend Member Payment Issued Email on Save" checkbox is checked.

  


Development Specification

[ ] BD:Send Email on Save behavior

[ ] The "Send Delivery Ticket Closed" is a temporary field that the user checks.

[ ] When saving if the temp field is checked, use field change expressions to:

[ ] Increment a hidden numeric field DeliveryTktEmailSentCount 

[ ] Set the "Email Sent On" date field to Today

[ ] Clear the temporary "Send Delivery Ticket Closed" checkbox so that it can be used again (we depend on the counter for actual behavior).

[ ] If the Counter is >= 1, then label the field as "Re-send" 

4 HOURS

  


BD: Email Trigger (review by USA)

[ ] Create an email trigger to send the email if the counter is incremented. See "Buyer Invoice Email" SECTION 

2 Hours (trigger w/o template work)
