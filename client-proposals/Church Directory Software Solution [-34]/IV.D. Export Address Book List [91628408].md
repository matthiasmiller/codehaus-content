4.4. Export Address Book List

  


Requirements

  * Accessed from Church Directory | Directory | Export Address Book List
  * Clicking this menu option begins the download process for the file, like the other export menu options
  * File details: 
    * Format: Excel
    * Columns: 
      * Name (displays the name of the individual or couple in the following formats: 
        * If individual: "LastName, FirstName MiddleName"
        * If married with both living: "HusbandLastName, FirstName MiddleName, (WifeFirstName MiddleName MaidenName)"
        * If married with husband deceased for the current marriage, include an asterisk before the husband's name: "*HusbandLastName, FirstName MiddleName, (WifeFirstName MiddleName MaidenName)"
        * If married with wife deceased for the current marriage, include an asterisk before the wife's name: "HusbandLastName, FirstName MiddleName, (*WifeFirstName MiddleName MaidenName)" 
        * If there are any second/third marriages: Only the current marriage is included; previous marriage(s) are disregarded
      * Address (displays the contents of the Address field from the Person record, i.e. "123 Long St")
      * City (displays the contents of the City field from the Person record)
      * State (displays the contents of the State field from the Person record)
      * Zip (displays the contents of the Zip field from the Person record)
      * Phone (displays the contents of the Phone field from the Person record)
    * Records to include: Husband and wife (or singe head of household, as applicable) for all active households (including a deceased spouse for current marriages, as specified above)



  


Development Specification

Austin Priest 06/28/2023: [[[IN7982](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-7984&)]] - ZPP - Directory - Address Book List Export

  


  


  


Matthias Miller 05/04/2021: 

[ ] Head of household blank if head is deceased

[ ] NOTE: Inactive households if both are deceased (warning?)

Ellis Miller 05/07/2021: TODO_CH: Sometime the last item needs clarification.

Matthias Miller 05/07/2021: Clarified here. We have a warning.

  


Bid 4 hours
