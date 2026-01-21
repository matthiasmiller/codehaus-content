4.3.2. Paid Time Off

  


Requirements

This would be an embedded spreadsheet that is automatically populated to:

  


  


Default PTO Hourly Rate:| Actual PTO Hourly Rate:| PTO Amount:  
---|---|---  
  
  


  


Hrs| Min| Day| Reason| Comment  
---|---|---|---|---  
0| 0| Monday| Vacation|   
  
0| 0| Tuesday| Vacation|   
  
0| 0| Wednesday| Vacation|   
  
0| 0| Thursday| Vacation|   
  
0| 0| Friday| Vacation|   
  
0| 0| Saturday| Vacation|   
  
  
  


Vacation days would be manually entered as 8 hours.

  


Holiday hours will be entered automatically with a "Holiday" reason. They can be manually adjusted on a per-time card basis.

  


The time card record will show a read-only PTO Hourly Rate above the embedded spreadsheet. For hourly employees, this will be calculated based on the prior 13 weeks of employment. It will be calculated using the current base rate, plus the average hourly bonus paid for the past 13 weeks. For salaried employees, it will show their weekly salary divided by 40.

  


For hourly employees with paid time off, the Hourly Rate in the spreadsheet will be prepopulated to the calculated hourly rate. For salaried employees or employees without paid time off, it will be prepopulated to 0.

  


These numbers can be manually adjusted if needed. Two example situations include:

  * Employees who do not normally receive paid time off, but receive it in a specific situation due to personal hardship
  * Salaried employees who take an unpaid day off (these would be entered with a negative hourly rate)



  


Paid time off will NOT contribute to overtime.

  


Development Specification

Update the x30 from prior step:

  * Automatically fill in the RG with one day each for Monday through Saturday
  * If this is a holiday and employee's current compensation includes holidays, set the hours to 8 and the Reason to Holiday.



  


To determine holidays, we'll need to create a CompanyIsProdDay( vDate) macro that uses the existing CompanyProdDayInc macro. => CompanyProdDayInc(CompanyProdDayInc(vDate,1),-1) = vDate. (If it's not a production day, it's a holiday). We'll evaluate CompanyIsProdDay on the ContactEmpCompCompany.

  


Bid: 4 hours
