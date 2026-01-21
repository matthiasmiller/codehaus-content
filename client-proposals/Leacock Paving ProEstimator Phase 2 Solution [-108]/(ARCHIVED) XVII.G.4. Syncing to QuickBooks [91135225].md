17.7.4. Syncing to QuickBooks

  


Requirements

The sync will handle sending data from Silverloom to QuickBooks. 

  


Time cards will need to map to QuickBooks:

  * Customer/Job
  * Service Item
  * Payroll Item



  


  * Pushing time to QuickBooks
    * Through QB - so everything will stay there, so QB will be the tracking device
    * Report with a breakdown by Rate + Hours
      * Payroll by the day + week
        * Regular Rate + ____ + Hours
        * Category + Rate + Regular Hours + Overtime Hours
    * Overtime Calculations by Time of Week
      * i.e. prevailing wage by Friday Afternoon
    * Every 2 weeks (full calendar weeks)
    * NOTE: Presumably we will want to sync hours daily  so that hours can be tied out to a Job in QuickBooks.



  


  * Every Hour would go towards that Job in QuickBooks



  


Tim Reitz 12/04/2025: I think these are left over from the Tuesday notes - not sure if they should just be converted to "TOD O_IDD" items? 

TOD O_HLD - What service item does office staff use? 

TOD O_HLD - how do we push rate into QB?

  


  


Matthias Miller 12/04/2025: No longer needed

  


Development Specification

TODO_IDD: Figure out exactly how mapping translates to Service Item / Payroll Item

Recommending TransactionPro

Time Tracking| Name *| Time/Enter Single Activity - Name|   
| X| Char 209  
---|---|---|---|---|---  
Time Tracking| Transaction Date| Time/Enter Single Activity - Date|   
|   
| Date  
Time Tracking| Customer *| Time/Enter Single Activity - Customer: Job| '(16)| X| Char 41  
Time Tracking| Service Item *| Time/Enter Single Activity - Service Item|   
| X| Char 31  
Time Tracking| Payroll Item| Time/Enter Single Activity - Payroll Item|   
|   
| Char 31  
Time Tracking| Duration| Time/Enter Single Activity - Duration|   
|   
| Char 10  
Time Tracking| Class|   
| (4)|   
|   
  
Time Tracking| Billable|   
| (2),(6)|   
| Char 1  
Time Tracking| Notes| Time/Enter Single Activity - Notes|   
|   
| Char 4095  
  
  

