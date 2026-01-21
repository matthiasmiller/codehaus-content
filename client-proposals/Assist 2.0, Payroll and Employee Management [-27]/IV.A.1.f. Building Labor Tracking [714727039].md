4.1.1.6. Building Labor Tracking

  


Requirements

Each company can track building labor with one of two methods:

  * By Station
  * By Employee



  


Each company will have a single setting (without historical tracking) that controls how building labor information gets entered. (Assist does not need to store historical settings because it will be saving the calculated labor cost values.)

  


When the Building Labor Tracking Method is "By Station", the company will include an embedded spreadsheet of stations. The station will be an editable list, customizable for each company. The order in the spreadsheet would define the order of the stations.

  


Development Specification

  * CompanyLaborTrackingTypes unchangeable list with two options above.
  * Company: CompanyLaborTracking list field: Required
  * On Company, add a CompanyProdStations RG visible if "By Station"
    * Company Station list field (ProductionStations). Users can add to the list from the RG. Include Move Up and Move Down buttons.



  


Bid: 4 hours
