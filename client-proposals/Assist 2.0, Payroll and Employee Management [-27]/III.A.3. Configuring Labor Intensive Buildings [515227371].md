3.1.3. Configuring Labor Intensive Buildings

  


Requirements

Certain buildings will add additional amounts to the production pool. For example, cottages and dog kennels are more time consuming to build, so they may add $1.00-1.50/sf to the production pool. (Note that this does not increase the total production for the week. It simply increases the size of the pool after the initial pool is calculated.)

  


These settings will be customized on the AppHosting.zone Settings record using an expression. This will likely be adjusted and configured by Josh.

  


This would use an embedded spreadsheet such as:

Reason| Expression  
---|---  
User-configurable list, such as "On-site", "Dog Kennel", "Cottage", etc.| Configurable setting that Josh sets up based on the building  
  
  


  


Development Specification

Matthias Miller 12/22/2020: From Duane. I don't see this being an issue: According to Mark, Josh has configured some rules already for shops doing production % whereby certain types of buildings multiply their production amount by a different % than the default. Mark and Gabe’s concern is that we take this into account when designing the labor-intensive buildings. My answer to this was that Josh will be establishing the rules on how buildings add to the pool and that since he has already done this, doing it again should not be a problem.

  


  


Add a string CompanyBuildingBonusPoolAmtExpr expression field. It has Expression requirements: 

  * Building level
  * Number



  


Always visible.

  


Bid: 2 hours
