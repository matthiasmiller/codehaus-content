8.2. Quote / Order Printout

  


Requirements

TODO_AP: Ben Reitz 11/14/2025: Standardize the entire printout spec as needed.

  


Purpose/Overview: This is a PDF printout that contains all of the Quote or Order information from the corresponding Quote or Order record.

  


Printed From: 

  * "Print Quote" button on the Quote record
  * "Print Order" button on the Order record



  


File Format/Name:

  * If the record is a Quote record "Quote <Quote Number> (exported on <Current Date>).pdf"
  * If the record is a Order record "Order <Order Number> (exported on <Current Date>).pdf"



  


Fields to be Filled: 

  * Truss Page (visible if the "Truss Order" checkbox is checked on the corresponding record): see corresponding section of this proposal
  * Lumber Page (visible if the "Lumber Order" checkbox is checked on the corresponding record): see corresponding section of this proposal
  * Metal Page (visible if the "Metal Order" checkbox is checked on the corresponding record): see corresponding section of this proposal



  


Handling Page Breaks: 

  * Each of the above pages (Truss, Lumber, and Metal) will begin on a new page.
  * Begin breaking a page after 9 rows in the first table. If this table reaches 12 rows, begin the second table on a new page.



  


Other Notes:

  * Note that the letterhead is displayed at the top of every page of this printout, unless the page is the result of the second bullet point regarding page breaks above.



  


Development Specification

Change Requests:

  * Ben Reitz 05/08/2025: [[[IN10784](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10786&)]] - ZTD - Printouts - Auto-populate Metal Ft
  * Ben Reitz 05/08/2025: [[[IN10786](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-10788&)]] - ZTD - Order Record - Enter deposits on Quotes / Orders
  * Ben Reitz 05/08/2025: [[[IN11219](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-11221&)]] - ZTD - Order printout - Add Deposit info if printout is single page


