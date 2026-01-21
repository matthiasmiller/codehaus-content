8.1.7. Settings: Tax Year

  


Requirements

Tax Year:

  * Default Tax Year End Date
    * (drop-list of months; defaults to December)
    * (drop-list of days of the month; defaults to 31)



  


Validation:

  * Error on save: if the end day is not a valid date for the selected month (e.g. February 30).



  


Development Specification

Niccolas Miller 01/16/2024:

Default Tax Year (AppHosting-Only) - this field is visible if ~HasOfficialSource.
