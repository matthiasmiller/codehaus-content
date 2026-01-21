7.2.2. Contact Record - Personal Details Section

  


Requirements

  * Personal Details custom section (visible if Contact Type = Member; visible to all users with some further restrictions as noted; editability noted below):
    * User Photo (read-only memo that displays the uploaded photo) 
    * Edit Photo (visible in Edit mode; button; visible to and editable for the Member and all uplines; opens a child screen to upload a photo - see Child Screen details) 
    * Short Bio (multi-line plain text field; editable for the Member and all uplines; warning on Save if blank: "Short Bio is blank.")
    * Church Affiliation (editable for Member and all uplines; warning on Save - validation message: "Church Affiliation is blank."; drop list of Church Affiliation items and blank; with an ellipsis button for Super Admins to edit / add new items)
    * Growth Ring Group(s): (auto-set and read-only; comma-separated list of Growth Ring Group Descriptions for all groups of which the Contact is a member; displays as a link that opens the Open Growth Ring Groups for Member Report)
    * Find Group (link; visible to uplines if the Member is not part of any group; opens the Growth Ring Groups report, where the upline can open the desired Group to add the Member) 
    * Facilitator for: (auto-set and read-only; comma-separated list of Growth Ring Group Descriptions for all groups for which the Contact is a Facilitator; displays as a link that opens the All Growth Ring Groups Report, filtered to that Facilitator)
    * Regional Rep for: (auto-set and read-only; comma-separated list of Region Names for all regions for which the Contact is a Regional Rep; displays as a link that opens the Configure Regions Report, filtered to that Regional Rep)



  


  * Update Photo Child Screen: This child screen contains the following:
    * Instructions text: "To upload a photo, copy and paste a .jpg or .png file into field below, or use the Insert Image button on the field's toolbar. If there are multiple photos in the field, the first one will be displayed as the user photo. To remove photos, click Delete Photo(s). " 
    * Delete Photo(s) (button; clicking this button will delete any photos in the Photo memo)
    * Photo (editable memo) 
    * Other notes:
      * The user would need to click a "Close" button or press the Escape key to exit the child screen.



  


Development Specification

Change Requests: 

  * Tim Reitz 04/09/2024: [[[IN9565](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9567&)]] - ZSB - Contact Record - Clarify Visibility & Editability
  * Tim Reitz 04/10/2024: [[[IN9550](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9552&)]] - ZSB - Contact & GR Goals - Items from Deployment walkthroughs
  * Tim Reitz 06/10/2024: [[[IN9880](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-9882&)]] - ZSB - Contact Record - Improve UI for User Photo
  * Tim Reitz 07/20/2024: [[[IN8988](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-8990&)]] - ZSB - Contact Record - Personal Details section visibility
  * 


  


  


Dev spec for uploading the photo:

  * Have a OnChange for the memo that uses  the ArchivedDocumentImage function (for attachments) or the actual memo contents (for inserted images), then run it through MemoThumbnail, save it into the read-only User Photo image. (I think this should work, but I haven't tested for sure.)



  


BID: 1 DAY
