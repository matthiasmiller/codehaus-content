7.7.1. Vehicle - Vehicle Summary Section

  * Vehicle Summary section:
    * Vehicle Description (read-only macro; displays the following for the current record: "<VIN> (<Year> <Make> <Model> \- "<Vehicle Name>")", i.e. "5FNRL5H66FB112445 (2015 Honda Odyssey - "Mary's minivan")"; note that if any of these fields are blank, that portion is completely excluded) 



  


  * VIN (required; plain text field that accepts numbers and letters; with the following details / behaviors:
    * unique identifier for the record; 
    * any letters entered in lower case are automatically capitalized;  
    * editability:
      * if the "Non-Standard VIN - Admin-Only" checkbox is not checked: editable for users with the "Full Access" Permission;
      * if the "Non-Standard VIN - Admin-Only" checkbox is checked: editable only for users with the "Full Access" Permission;
    * when set, the following field(s) are affected:  
      * "VIN Validated": checkbox is set to checked if all "VIN validating" validations for the "VIN" field are met; checkbox is set to not checked if any of the criteria are not met; 
    * always includes the following validations:
      * error on the field if set to a VIN that already exists on a saved Vehicle record in the Solution: "This VIN already exists on another Vehicle record.";
      * warning on the field if changed from non-blank: "Changing the VIN will cause related vehicle details to change.";
    * includes the following "VIN validating" validations if "Vehicle Year" = "1983" or later, or if the "Non-Standard VIN - Admin-Only" checkbox is not checked (based on the guidelines specified at [https://en.wikipedia.org/wiki/Vehicle_identification_number](https://en.wikipedia.org/wiki/Vehicle_identification_number)): 
      * error on Save if the VIN is not 17 characters long: "The VIN should be 17 digits long. Please contact a Master Administrator if a non-standard VIN is needed."; 
      * error on Save if the letters "I", "O", and "Q" are included in any part of the VIN: "The following letters are not valid VIN characters: I, O, Q. Please contact a Master Administrator if a non-standard VIN is needed.";
      * error on Save if the following characters are included in the 10th digit of the VIN: "U", "Z", or "0" (zero): "<character> is not a valid VIN year code. Please contact a Master Administrator if a non-standard VIN is needed."; 
      * error on Save if the check digit (the 9th digit) is not valid: "The entered check digit for the VIN is not valid. Please contact a Master Administrator if a non-standard VIN is needed."; 
    * includes the following additional validations if "Vehicle Year" = "1983" or later, or if the "Non-Standard VIN - Admin-Only" checkbox is not checked: 
      * error on Save if the entered "Year" for the Vehicle record does not match the VIN year: "The VIN year is <Year 1> or <Year 2>, but the vehicle year is <Vehicle Year>. Please contact a Master Administrator if a non-standard VIN is needed."; 



Tim Reitz 12/09/2025: How much work would it be to also have these validations for Make and Model? 

Tim Reitz 12/09/2025: Or, should we have Year, Make, & Model be read-only for standard VINs (set via the API)? (and editable if "Non-Standard..." is checked). 

TODO_: Tim Reitz 12/10/2025: Let's go this route. 

  * __)



  


  * VIN Validated (checkbox; with the following details / behaviors: 
    * auto-set and read-only; 
    * is automatically set to checked or not checked based on the "VIN" field - see corresponding spec; 
    * note that this does not take the "Year", "Make", or "Model" fields into account, so if those are set to values that do not match the entered VIN information, this checkbox remains checked as long as the VIN validation criteria are met) 



TODO_: Tim Reitz 11/20/2025: I think we want to take a different approach here and take Year / Make / Model into account.

Tim Reitz 12/09/2025: If we do an automated / API integration approach, this could happen more automatically based on the results of the API ping. 

  


  * Non-Standard VIN - Admin-Only (checkbox; with the following behaviors / details:
    * visible to and editable for users with the "Full Access" Permission;
    * visible for other users if checked;
    * checking this checkbox makes the "VIN" field read-only for users without the "Full Access" Permission, and suppresses most of the usual validations on the "VIN" field - see corresponding spec) 



  


  * View Vehicle Details (visible if "VIN Validated" is checked; link; opens the URL specified in the "VehicleVINDecoderURL" System Switch, with the "VIN" for the current Vehicle passed through)



  


  * Year (__
  * Make (__
  * Model (__



_EM.: Tim Reitz 09/15/2025: How can we utilize openvindecoder.com to auto-set Year, Make, Model? (e.g. [https://www.openvindecoder.com/?vin=5FNRL5H66FB112445](https://www.openvindecoder.com/?vin=5FNRL5H66FB112445))

_VA: Tim Reitz 10/31/2025: Per Ellis, 

  * Probably will cost $1,500-3,000 to do this 



_GZ: Tim Reitz 10/31/2025: Are you interested in this, or prefer to manually enter Year, Make, Model? 

_EM: Tim Reitz 11/06/2025: Glen thinks it would be nice to pursue this now. 

Tim Reitz 12/11/2025: Per Ellis, we'd essentially create a WSGI for this. Take the VIN, send it to the API, and return the value(s) to a separate "VIN record", and display it in the Vehicle record. ZWA/ZWW might want to start using this too. 

_VA: Tim Reitz 12/11/2025: Send Ellis an email to discuss with Josh. 

Tim Reitz 01/14/2026: Done today -- forwarded the email I sent to Jonathan (below).

Tim Reitz 12/09/2025: Who should research options & approach? 

_VA: Tim Reitz 12/10/2025: Could you take up to 60 minutes to research VIN decoders and pick the best 1-3 that you think will be best to integrate with via API? 

Tim Reitz 01/14/2026: Sent Jonathan an email today (subject: "Research for Vehicle Tracking IDD - VIN Decoder API").

TODO_JB (research): Tim Reitz 01/16/2026: See the email I sent on this (subject in the line above). 

  


TODO_: Tim Reitz 11/06/2025: Glen would like to pull in / access as much information as possible - factory window sticker info, etc. 

  


  * Have a separate VIN record in the background that would update in the background. 


  * Color (optional; drop list of "Vehicle Colors" list items; note that in the future, this could be enhanced to pull in the color automatically based on an online lookup tool)



  


  * License Plate (optional; plain text; with the following details / behaviors:
    * automatically removes dashes and automatically capitalizes lower-case letters;
    * warning on Save if blank and "Current Owner" is not blank: "Vehicle license plate is missing.";
    * note that in the future this could be changed to be required if "Current Owner" is not blank, with an override feature to bypass the requirement)



  


  * Vehicle Name (optional; plain text; allows for tracking a specific name or description that is easier to visually identify than the VIN)


