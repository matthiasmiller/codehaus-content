9.9. Meeting Goals Worksheet Printout

  


Requirements

Purpose/Overview: This is a PDF printout that contains the fields on the Life Vision and Annual Goals sections on the Contact record, as well as the Goals for a Member's next upcoming Meeting. It can be printed with fields filled from the Contact and Growth Ring Goals records, or it can be printed blank and filled out by hand.

  


Printed From: 

  * The "Print Meeting Goals Worksheet" link on a Growth Ring Meeting record (generates the PDF with the specified fields below, based on the selected Member (see corresponding spec))
  * The "Print Meeting Goals Worksheet" link on a Growth Ring Goals record (generates the PDF with the specified fields below filled with the Goals from the corresponding record)
  * Members Menu | My Next Meeting Details | Print Meeting Goals Worksheet (generates the PDF with the specified fields below filled for the current user's next Meeting)
  * Group Facilitation | My Group Management | Print Meeting Goals Worksheet (blank) (generates a blank version of the PDF)
  * Admin | Growth Ring Group Management | Print Meeting Goals Worksheet (blank) (generates a blank version of the PDF)
  * Dashboard | My Current Goals | Print Meeting Goals Worksheet (generates the PDF with the specified fields below filled for the current user's next Meeting)



  


File Format/Name:

  * Blank: "Meeting Goals Worksheet.pdf"
  * Filled: "Meeting Goals for <Member Name> <Meeting Date>.pdf"



  


Fields to be Filled: 

General Information fields:

  * Name (FirstName LastName format, without the Contact ID)
  * Date (m/d/yyyy; Meeting Date for the Meeting linked to the corresponding Growth Ring Goals record)



  


Life Vision field (from the Member's Contact record):

  * By age <Age>, which is only <Years> years from now, I envision <Life Vision text>



  


Annual Goals section (from the Member's Contact record):

  * Year
  * Set Date
  * Review Date
  * Annual Goals table (shows 6 rows):
    * Life Branch (one row for each Life Branch, including "Other")
    * Description (displays the goal for the corresponding Year and Life Branch) 



  


Monthly Focus Actions section:

  * "Month 1 (Meeting: <Meeting Date>)"  table (shows 6 rows; with the following behaviors:
    * if the "Include Last Meeting's Goals" checkbox is unchecked, auto-fills from the Growth Ring Goals record for the Member's next Meeting;
    * if the "Include Last Meeting's Goals" checkbox is checked, auto-fills from the Growth Ring Goals record for the Meeting before the Member's next Meeting):
      * Life Branch (one row for each Life Branch, including "Other", from the corresponding Growth Ring Goals record)
      * Description (displays the "Description" for the corresponding row on the Growth Ring Goals record; if the text is too long to fit within the field, the text should be truncated)
      * Yes (displays as "X" if "Achieved" = "Yes" for the corresponding row on the Growth Ring Goals record)
      * No (displays as "X" if "Achieved" = "No" for the corresponding row on the Growth Ring Goals record)
        * If "Achieved" column on the Growth Ring Goals record is not "Yes" or "No", the "Yes" and "No" columns on the printout are blank.
      * $$ Penalty (displays the "Penalty" for the corresponding row on the Growth Ring Goals record)



  


  * "Month 2 (Meeting: <Meeting Date>)" table (shows 6 rows; with the following behaviors:
    * if the "Include Last Meeting's Goals" checkbox is unchecked, this table is blank;
    * if the "Include Last Meeting's Goals" checkbox is checked, auto-fills from the Growth Ring Goals record for the Member's next Meeting):
      * Life Branch (same as the spec for the corresponding column in Month 1 table)
      * Description (same as the spec for the corresponding column in Month 1 table)
      * Yes (same as the spec for the corresponding column in Month 1 table)
      * No (same as the spec for the corresponding column in Month 1 table)
      * $$ Penalty (same as the spec for the corresponding column in Month 1 table)



  


Handling Page Breaks: Page break between "Quarterly Lead Measures" and "Monthly Focus Actions" sections

  


Other Notes: 

  * Sample: [https://drive.google.com/file/d/1YyqwHGT93mIG-_61ib9z7yFDyl9Wj5d0/view?usp=drive_link](https://drive.google.com/file/d/1YyqwHGT93mIG-_61ib9z7yFDyl9Wj5d0/view?usp=drive_link)
  * Note that this printout should be entitled "Meeting Goals Worksheet" to match the software link names.



  


Development Specification

Change Requests:

  * Ben Reitz 09/17/2025: [[[IN10074](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10076&)]] - ZSB - Growth Ring Goals - Add "Meeting Goals Worksheet" printout (prev. Add "Print Goals" button)


