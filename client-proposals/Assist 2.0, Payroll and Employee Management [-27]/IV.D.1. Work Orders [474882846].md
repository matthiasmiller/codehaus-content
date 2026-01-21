4.4.1. Work Orders

  


Requirements

Assist doesn't immediately need to associate work orders with buildings. However, eventually it will need to track work orders for logistics. For this reason, it will associate work orders with a specific building.

  


Work orders do NOT affect profitability numbers because they can happen long after a building is built. There's no way to track them in profitability numbers without shifting historic numbers.

  


Instead, work orders are simply removed from payroll the week that they occur. They are distributed across employees based on their production hours and the total hours that they worked. Because they are removed from the employees' production bonus and not otherwise accounted for in the profitability tracking, they are implicitly accounted for in the profitability tracking.

  


For now, Burkholder Management will enter the work order by searching for the building, then entering them in an embedded spreadsheet such as:

Effective Date| Payroll Week| Total Cost| Amount Deducted from Employees| Completion Date| Reason  
---|---|---|---|---|---  
11/9/2020(Automatically set to the Monday of the prior week)| 11/8/2020 - 11/14/2020(selected; show current week, following week, or blank for none)| $| Automatically copied from Total Cost but can be manually adjusted| 10/28/2020  
|   
  
  
  


NOTE: This approach will allow us to use work orders regardless of the production bonus type. We decided to do this for simplicity of implementation and management.

  


Development Specification

Josh: We're planning to do this as an RG, and we can break it out into a separate record if we want to for the sake of logistics.
