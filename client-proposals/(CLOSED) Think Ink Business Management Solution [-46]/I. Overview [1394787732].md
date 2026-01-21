1\. Overview

  


Requirements

Think Ink, LLC has been in business for about 10 years. Originally they sold ink and toner, focusing on after-market supplies. As time went on, people started asking for printers as well. Now, Think Ink provides printer sales and rentals as well as printer supplies and service. 

 

Currently Think Ink is using Classic Accounting and using LibreOffice base as a front end, and all their information is stored in the same database with their own tables. Most of it is pulling information from it, but it’s not relational -- there are separate modules that store the billing and other data.

 

Currently Think Ink does a lot of their reporting with SQL Queries in Excel with Power Queries -- they can easily create data to use.

 

They get 30-40 invoices a day. Because they buy the same item from different vendors, their costs are always changing, and try to follow through with shipping on the client invoice to get the actual cost.

 

MPS (Managed Print Services) customers are billed either monthly or quarterly. MPS printers for customers with internet connection have reporting software that sends back page counts and allows Think Ink to remotely manage the printers. MPS printers for customers without internet must have their page counts reported manually by the customer or a Think Ink employee (or estimated on occasions, if the customer is late in reporting). Currently they aim to collect page counts on the first day of the month, and try to do the invoicing by the 10th. It takes some time to get all the manual ones collected. Collecting and entering manual page counts is a big pain point.

  


Development Specification

Project Name/Nickname: Think Ink

Domain: think.apphosting.zone

3LC: ZTK

Link to Accounting Module Proposal: [https://zch.apphosting.zone/Detail/Edit/2?RecordType=ClientProposals&NumberID=-82&StateID=7wApu0wR1jTC&ShowTitleBar=true&#](https://zch.apphosting.zone/Detail/Edit/2?RecordType=ClientProposals&NumberID=-82&StateID=7wApu0wR1jTC&ShowTitleBar=true&#)
