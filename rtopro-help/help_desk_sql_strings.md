# http://www.rtopro.com/help/help_desk_sql_strings.htm

# Using SQL Strings to create custom reports / results.

<< [Click to Display Table of Contents](index.md) >> **Navigation:** [Help Desk](help_desk_pricingsetup.md) >

# Using SQL Strings to create custom reports / results.

|  [](nsf-and-accounting.md "Previous Topic") [](help_desk_pricingsetup.md "Parent Chapter") [](removing_an_inventory_item.md "Next Topic")  
---|---  
  
In RTO Pro you can use SQL strings to display records in the custom report layout where they can be organized, printed or exported in a number of different formats. To display records with SQL strings go to Revenue Menu option "E" or the Inventory Menu > Inventory Reports and click on the "View records with SQL string" button on the lower left of the screen.

Please note to request help with SQL strings click the green button on this screen, as displayed in the screen shot below. This will launch the Support Portal. You will be logged in automatically and be able to post requests for help. The forum is monitored by support. You will be notified of any replies to your posts by email to the email you have in your store setup, your store email address. Please note you will also need a RTO Pro web services user name and password, which you will already have if you are using any web services like webpay or web apps. If you do not have a web services account contact support, there is no charge for this while you have an active subscription of RTO Pro.

Below is a screen shot of the Custom SQL String report screen, see below for more info.

![clip0034](clip0034.png)

The image above is a screen shot of the Custom SQL String entry page. This is where you select a previously saved SQL string or enter a new SQL String. Below are descriptions of the elements on this screen.

1\. This is the actual SQL string that will run when you push the "F5" key or click the "F5 Run Selected" button. You can either type a SQL string in here, select a pre-saved SQL string from the list below or copy and paste a SQL string into this box. The string here can also be edited as needed before pushing F5. (see below for example SQL strings and what they can do)

2\. Saved SQL string descriptions are displayed here. To run a saved SQL string simply click the description of the string you wish to run, then push F5. You can also edit the description of a previously saved item by clicking in the description, editing as needed and pushing ENTER to save.

Save SQL String button: This will save the current SQL string with the selected description.

Save AS NEW button: This will save the current SQL string and allow you to enter a new description to go along with it. The description can be ANYTHING you like to describe what the SQL string is for or what you use it for. This is just for your reference.

To delete a saved SQL String record click on the box to the left of the record (with the > in the image above) and press the delete key on your keyboard.

Below are some examples of SQL strings and the results they will bring up (the SQL String is the part in blue, you can copy and paste them from here into your SQL string field).

A list of all inventory in your database:

inventory

A list of STOCK inventory in your database ordered by stock#:

INVENTORY where status = 'STOCK' order by stock

A list of all customers in your database:

customers

A list of all open contracts ordered by taxzone:

CONTRACTS where status like 'OPEN%' order by taxzone

If you want customer info also use the string below:

select * from CUSTOMERS inner join CONTRACTS on contracts.account = customers.account where contracts.status like 'OPEN%' order by contracts.taxzone

A list of open contracts who's due date has been moved more then 30 days (this query will take a few minutes to run):

select * from CONTRACTS where status like 'OPEN%' and contract in(select contract from HISTORY where transtype = 'D' group by contract having sum(nextdue - duedate) > 30)

A list of payments with a check number of 1791:

HISTORY where cknum = '1791'

A list with customer name, acct number, contract number and balance for all customers with open agreements.

select customers.name, customers.account, contracts.contract, contracts.contractamt - contracts.amtpaid as balance from contracts INNER JOIN customers ON contracts.account = customers.account where status = 'OPEN' order by contracts.contract

Open contracts with Club

contracts where clubfee > 0 and status = 'OPEN'

All contracts that have or had Club

contracts where clubfee > 0

A list of all petty cash payouts between 9/1/2009 and 9/25/2009

deposits where potype = 11 and transdate between '9/1/2008' and '9/25/2008'

Average payment amount for Monthly, open, RTO agreements.

select avg(pmt) from contracts where status = 'OPEN' and term = 'M' and contype = 'R'

Average payment amount for Weekly, open, RTO agreements.

select avg(pmt) from contracts where status = 'OPEN' and term = 'W' and contype = 'R'

Average payment amount for Bi-Weekly, open, RTO agreements.

select avg(pmt) from contracts where status = 'OPEN' and term = 'B' and contype = 'R'

All open contracts with customer name that are due on the 1st of any month.

select customers.name, contracts.* from contracts inner join customers on contracts.account = customers.account where extract(day from duedate)=1 and status = 'OPEN'

Account, name and address info for all active customers:

select distinct(customers.account), name, address, apt, city, state, zip, hmphone from customers inner join contracts on customers.account=contracts.account where contracts.status='OPEN'

Account, name and address info for all inactive customers:

select distinct(account), name, address, apt, city, state, zip, hmphone from customers where account not in(select account from contracts where status='OPEN')

Contracts number, contract date, last transaction date, contract amount, amount paid and percent of contract amount paid for all agreements paid out between 1/1/2010 and 1/31/2010.

select contract,contractdate,lasttrans,contractamt,amtpaid,amtpaid / contractamt as percentpaid from contracts where status like 'PAID%' and lasttrans between '1/1/2010' and '1/31/2010'

A report with the first serial number on each agreement and the amount of rent paid on the contract for the specified dates.

select "SERIAL 1",sum(history.amount)AS RENT FROM CONTRACTS inner join history on history.contract=contracts.contract where history.transdate between'1/1/2010'and'3/25/2010'AND transtype in('R','P','C','B') group by"SERIAL 1"having sum(amount) >0

A list of customer records who have a deposit balance but do not have any open agreements:

select * from customers where deposit > 0 and account not in (select account from contracts where status like 'OPEN%')

Contract and account number for active contracts and days due date have been moved and money "lost" from moving the due dates. Note money is not truly lost from moving due dates if the customer goes to term.

select contract, account, sum(nextdue - duedate)as daysmoved, sum(total) as moneymoved from history where transtype='D' and contract in(select contract from contracts where status='OPEN') group by account, contract

Zip code survey, count of active customers in each zip code.

select zip, count(distinct(customers.account)) from customers inner join contracts on customers.account=contracts.account where contracts.status like'OPEN%' group by zip

A list of customers who only have 1 active rental agreement

select * from customers where account in(select account from contracts where status = 'OPEN' group by account having count(*)=1)

These are only a few examples of what can be done, you can write SQL strings to return just about any records you like from any of the data in RTO Pro.

The main database table names in RTO Pro are below:

cc

history

customers

contracts

inventory

To see all records in a table you can just type the table name as the SQL string. Once you see the entire table you can see the field names and use those in your SQL string. For instance you could use the following:

select transdate, receipt, account, contract from HISTORY where transdate = '8/20/2009'

The string above would only return the specified fields and only if the transdate = 8/20/2009

You could use the string below to show customer names and alternate names on for all customers who live in Eustis.

select name, altname from CUSTOMERS where city = 'EUSTIS'

If you want all customer info all customers who live in Eustis, use the string below.

CUSTOMERS where city = 'EUSTIS'

A list of active rental customers name, account number, contract, term, pmt amount, other charges due, due date, last transaction date, contract date, total # of payments, pmts left and balance

select customers.name, customers.account, contracts.contract, contracts.term, contracts.pmt, contracts.otherdue, contracts.duedate, contracts.lasttrans, contracts.contractdate, contracts.payments, (contracts.contractamt-contracts.amtpaid) / contracts.pmt as PmtsLeft, contracts.contractamt-contracts.amtpaid as balance from contracts inner join customers on contracts.account=customers.account where contracts.status='OPEN' and contracts.pmt>0

A list of all active customers with contract info and a field that displays days late.

select iif(current_date - duedate >0,current_date - duedate,0) as dayslate, customers.*,contracts.* from customers inner join contracts on contracts.account=customers.account where contracts.status like 'OPEN%'

The SQL string below will give you a list of dates of the month you have open contracts due on. For instance how many open contracts are due on the first of any month, how many open contracts due on the 2nd of any month etc.

select extract(day from duedate)as duedate, count(*)as concount from contracts where status like 'OPEN%' group by duedate

The SQL string below will display all reference info.

select reference1,refadd1,refadd2,refphone1, reference2,refadd2,refadd22,refphone2, reference3,refadd3,refadd23,refphone3, reference4,refadd4,refadd24,refphone4, reference5,refadd5,refadd25,refphone5, reference6,refadd6,refadd26,refphone6 from applications 

The SQL string below will display each paid off agreement and the maximum days late each of these agreements were during their lifetime.

select contract,max(dayslate)as maxlate from history where contract in(select contract from contracts where status like 'PAID%') group by contract

The SQL string below will give you name, address and phone for all customers who have rented anything in the inventory category "FURNITURE" since 1/1/2010

select name,address,city,state,zip,hmphone from customers where account in(select account from contracts where contractdate >='1/1/2010' and ("MODEL 1"||"MODEL 2"||"MODEL 3"||"MODEL 4"||"MODEL 5"||"MODEL 6"||"MODEL 7"||"MODEL 8"||"MODEL 9"||"MODEL 10") in(select distinct(model) from inventory where category ='FURNITURE'))

The SQL string below will display all active agreements that have paid less than 2 normal payments(not including the down payment)

select * from contracts where status ='OPEN' and contract in (select contract from history where transtype='P' group by contract having count(*) < 2)

The SQL string below will display contracts closed as returned or repo, whose contract date was in 2012 and had less than 4 transactions (payments etc. all closed contracts have at least 2 transactions, the load and the close.)

select * from contracts where status in('RETURNED','REPOSSESION') and contractdate between '1/1/2012' and '12/31/2012' and contract in (select contract from history group by contract having count(*) < 4)

The SQL string below will give you total cash price by state for RTO contracts loaded in 2012.

select sum(cashprice),customers.state from contracts inner join customers on customers.account=contracts.account where contractdate between '1/1/2012' and '12/31/2012' and contype='R' group by state

The SQL string below demonstrates how you can use sub-queries, it will return the following info: Contract #, contract amount, pmts behind, $ behind, Total Amount paid, total rent paid in Jan 2013, Feb 2013 and March 2013 and the total amount left to pay (balance) for all OPEN rental agreements. The String below is broken down to make it easier to read, to use it in RTO Pro it must be entered as a single line.

select contracts.contract, contractamt, ((current_date-duedate)/30) as pmtsbehind,(((current_date-duedate)/30) * pmt) as moneybehind,contracts.amtpaid, b.SB as Jan2013, c.SC as Feb2013,d.SD as March2013, contractamt-amtpaid as futurepmts 

from contracts 

left join (select contract, sum(Amount) as SB from history where transdate between '1/1/2013' and '1/31/2013' and transtype<>'D' group by contract)b on contracts.contract=b.contract 

left join (select contract, sum(Amount) as Sc from history where transdate between '2/1/2013' and '2/28/2013' and transtype<>'D' group by contract)c on contracts.contract=c.contract 

left join (select contract, sum(Amount) as SD from history where transdate between '3/1/2013' and '3/31/2013' and transtype<>'D' group by contract)D on contracts.contract=d.contract 

where status='OPEN'

Another example of sub-queries. The string below will return the number of RTO contracts paid out and the number of RTO contracts picked up, returned or repoed(collectively called repo in these results), grouped by tax zone. So for each tax zone you could see the number of paid out contracts vs closed for other reasons. 

select contracts.taxzone, b.SB as paidout, c.SC as repo from contracts 

left join (select taxzone,count(*)as SB from contracts where status like 'PAID%' and contype='R' group by taxzone)b on contracts.taxzone=b.taxzone 

left join (select taxzone,count(*) as SC from contracts where (status like 'REPO%' or status like 'PICK%' or status like 'RET%') and contype='R' group by taxzone)c on contracts.taxzone=c.taxzone 

group by contracts.TAXZONE,b.SB,c.SC

The revenue summary report will display an EPO$ paid figure, to get detail on the amounts this includes you could use the SQL string below, edit dates as needed.

select history.amount as totpo,history.name,contracts.account,contracts.contract from contracts inner join history on contracts.contract = history.contract where contracts.status = 'PAID OUT EARLY' and contracts.lasttrans between '1/1/2013' and '5/20/2013' and contracts.contype in ('R','L','G','O') and history.transdate = contracts.lasttrans and history.receipt like 'C%' and history.refund=0

The SQL string below will return all customers who have paid out agreements, excluding paid out NSF's, and do not have any active agreements currently.

select CUSTOMERS.NAME,CUSTOMERS.ACCOUNT,CUSTOMERS.ADDRESS,CUSTOMERS.APT,CUSTOMERS.CITY,CUSTOMERS.STATE,CUSTOMERS.ZIP,CUSTOMERS.HMPHONE from customers inner join contracts on customers.ACCOUNT=contracts.ACCOUNT where contracts.STATUS like 'PAID%' and contracts.contype <>'N' and customers.account not in(select account from contracts where status like 'OPEN%')

The SQL string below will display customer info and rating, contract status, days late (for open agreements), balance and payment amount including tax (not including any clud DWF etc.) for all customers and agreements in your database.

select customers.name,customers.address,customers.city,customers.state,customers.zip,customers.account,contracts.contract,status,rating, iif(current_date - duedate >0 and status ='OPEN',current_date - duedate,0) as dayslate, contractamt-amtpaid as balance, cast(pmt * (1 + taxrate) as decimal(18,2)) as payment from customers inner join contracts on contracts.account=customers.account

The SQL String below will return IClocation, Days Idle, model, serial, stock and status for all STOCK inventory.

select iclocation,iif(transfer1 > '12/30/1899',current_date - transfer1,0) as DaysIdle,model,serial,stock,status from inventory where status ='STOCK'

The SQL string below will show contracts, pmt amount, total paid in 2013 and pmts paid in 2013 for all contracts that were paid on in 2013.

select contracts.contract, contracts.pmt,sum(history.amount)as tpaid,sum(history.amount) / contracts.pmt as pmtspaid

from contracts inner join history on contracts.contract=history.contract where history.transdate between '1/1/2013' and '12/31/2013' and contracts.pmt >0 

group by contracts.contract,contracts.pmt having sum(history.amount) >0

Below is an example of a SQL sub query. This SQL string will pull customer info for customers who do not have an active agreement and order it by their last action date in the "Actions" table.

select (select first 1 actiondate from actiontable B where B.account=A.account order by actiondate desc) as actiondate, name, address, apt,city,state,zip,hmphone,cell, contracts.* from customers A

left join contracts on A.account=contracts.account where A.account not in (select account from contracts where status='OPEN') order by actiondate

Below is a SQL string to return account, contract, cash price on contract, sum of cost, RBVtax and RBVbook of inventory on the contracts that are open (below it is broken into separate lines for the different sections of the SQL string, it would be entered as one line in RTO Pro).

select contracts.account, contracts.contract,contracts.cashprice, sum(inventory.cost) as cost,sum(inventory.balance) as RBVTAX, sum(inventory.rbvbook) as rbvbook

from contracts inner join inventory on inventory.contract=contracts.contract

where contracts.status='OPEN' 

group by contracts.account, contracts.contract,contracts.CASHPRICE

Customers and "how they heard about you" info, with contracts loaded between 1/1/2015 and 3/1/2015.

select applications.adsource,customers.account,contracts.contract,address,city,state,contracts.contractdate from contracts left join applications on applications.account=contracts.account

inner join customers on customers.account=contracts.account where contractdate between '1/1/2015' and '3/1/2015'

Below will return model, serial, cost, rental income and rent paid at time of close(paid on the close out receipt) for inventory paid out in 2014. The dates in the string below can be changed as needed.

select model,serial,stock,cost,rentalincome,history.amount as paidrentatclose from inventory left join history on history.contract=inventory.contract where status like 'PAID%' and transfer1 between '1/1/2014' and '12/31/2014' and history.transdate = inventory.transfer1 and history.receipt like 'C%' and history.refund=0

Below will give you a contract count for each payment term, for open RTO contracts.

select payments, count(*) from contracts where status ='OPEN' and contype='R' group by payments having count(*) > 0

Below will give you each salesman, their late and total active contract count and the late percentage.

WITH TOTALS AS (SELECT SALESMAN, cast(COUNT(*) as decimal(18,2)) AS T FROM contracts where status like 'OPEN%' GROUP BY 1), TOTALLATE AS (SELECT SALESMAN, cast(COUNT(*)as decimal(18,2)) AS TL FROM contracts WHERE CURRENT_DATE > DUEDATE and status like 'OPEN%' GROUP BY 1) SELECT TOTALS.SALESMAN,cast(TOTALLATE.TL as decimal(18)) as latecons, cast(totals.t as decimal(18)) as totalcons, Cast((TOTALLATE.TL *100) / TOTALS.T as VARCHAR(20)) || '%' as latepercent FROM TOTALS JOIN TOTALLATE ON TOTALS.SALESMAN = TOTALLATE.SALESMAN

Another example of sub queries is below. This shows all open contracts, due date, days late. extension days(days due date moved ahead), balance and deposit amount for all active contracts.

select A.account, name, B.contract,duedate,IIF(duedate < current_date,current_date-duedate,0) as dayslate, c.SB as extensiondays, contractamt-amtpaid as balance,deposit,B.store from customers A inner join contracts B on B.account= A.account left join (select sum(nextdue-duedate) as SB,contract from history where transtype='D' group by contract)c on B.contract=c.contract where status='OPEN'

This is another example of sub queries. This SQL string will display the number of paid out, repoed, returned and total contract count by tax zone.

select contracts.taxzone, b.SB as paidout, c.SC as repo, e.SD as returned, d.SA as totalcontracts 

from contracts 

left join (select taxzone,count(*)as SB from contracts where status like 'PAID%' and contype='R' group by taxzone)b on contracts.taxzone=b.taxzone 

left join (select taxzone,count(*) as SC from contracts where (status like 'REPO%' or status like 'PICK%') and contype='R' group by taxzone)c on contracts.taxzone=c.taxzone 

left join (select taxzone,count(*) as SD from contracts where (status like 'RET%') and contype='R' group by taxzone)e on contracts.taxzone=e.taxzone 

left join (select taxzone,count(*) as SA from contracts where contype='R' group by taxzone)d on contracts.taxzone=d.taxzone 

group by contracts.TAXZONE,b.SB,c.SC,e.SD,d.SA

The SQL string below will give you anybody who is set up to pay by autopay today or before.

SELECT contracts.account, contracts.contract, contracts.duedate, customers.name 

FROM contracts 

inner join customers on customers.account=contracts.account 

WHERE status like 'OPEN%' 

and ((autochargepmts > 0 and dateadd(day,-autochargeb4due,duedate) <= CURRENT_DATE ) or (autochargepmts < 0 and contracts.recupdate <= CURRENT_DATE)) 

ORDER BY name

The string below will display closed contracts with payment history info such as how many times paid on time and in different ranges of late payments.

select contract, contractdate, lasttrans as "Date Closed",

(select count(*) from history where contract=a.contract and transdate <= duedate) as early,

(select count(*) from history where contract=a.contract and dayslate between 1 and 10) as "1-10 DPD" ,

(select count(*) from history where contract=a.contract and dayslate between 11 and 20) as "11-20 DPD", 

(select count(*) from history where contract=a.contract and dayslate between 21 and 30) as "21-30 DPD" ,

(select count(*) from history where contract=a.contract and dayslate between 31 and 60) as "11-20 DPD" ,

(select count(*) from history where contract=a.contract and dayslate > 60) as "61+ DPD" ,

amtpaid / pmt as pmtspaid

from contracts a where status <> 'OPEN' and contype ='R'

The string below will give you customer name, address, phone and references for customers with open contracts. It also shows the payment amount, due date and term of the contract.

select name,address,city,state,zip,hmphone,wkphone,cell,work1,reference1,refadd1,refadd2,refphone1, 

reference2,refadd2,refadd22,refphone2, reference3,refadd3,refadd23,refphone3, 

reference4,refadd4,refadd24,refphone4, reference5,refadd5,refadd25,refphone5, 

reference6,refadd6,refadd26,refphone6,

pmt,duedate, term

from customers left join applications on applications.account=customers.ACCOUNT left join contracts on contracts.account=customers.ACCOUNT

where contracts.status='OPEN'

The string below will return the percent of all closed R type contracts that are paid out, for each store. This is for central server companies.

select a.store, 

cast(cast(sum(b.PO) as decimal(10,3)) / cast(sum(c.TOT)as decimal(10,3)) * 100 as decimal(10,3)) as PERCENTPAIDOUT

from contracts a

left join (select store,count(*) as PO from contracts where status like 'PAID%' and contype='R' group by 1)b on b.store=a.STORE 

left join (select store,count(*) as TOT from contracts where contype='R' and status <>'OPEN' group by 1)c on c.store=a.STORE 

group by a.store

The string below will return the number of Pick up/Returns/Repo's, Paid Out, Chargeoffs, Total Closed, Number Active contracts, grouped by number of payments, for RLO and G type contracts.

select payments, (SELECT COUNT(*) FROM contracts WHERE (status = 'PICKED UP' or status = 'RETURNED' or status = 'REPOSSESION') and (contype ='R' or contype = 'L' or contype = 'O' or contype = 'G') and payments=a.payments) as PU_Repo

,(SELECT COUNT(*) FROM contracts WHERE (status = 'PAID OUT' or status = 'PAID OUT EARLY') and (contype ='R' or contype = 'L' or contype = 'O' or contype = 'G') and payments=a.payments) as PaidOut

,(SELECT COUNT(*) FROM contracts WHERE (status = 'CHARGE OFF' or status = 'SKIP' or status like '%WRITE OFF') and (contype ='R' or contype = 'L' or contype = 'O' or contype = 'G') and payments=a.payments) as chargeof

,(SELECT COUNT(*) FROM contracts WHERE status <> 'OPEN' AND status <> 'PRINTED-CANCEL' AND status <> 'PRINTED' and (contype ='R' or contype = 'L' or contype = 'O' or contype = 'G') and payments=a.payments) as totalclosed

,(SELECT COUNT(*) FROM contracts WHERE status = 'OPEN' and (contype ='R' or contype = 'L' or contype = 'O' or contype = 'G') and payments=a.payments) as totalactive

from contracts a where (contype ='R' or contype = 'L' or contype = 'O' or contype = 'G') group by payments

The string below is the same as above, but it adds average number of days open for each close type.

select payments, (SELECT COUNT(*) FROM contracts WHERE (status = 'PICKED UP' or status = 'RETURNED' or status = 'REPOSSESION') and (contype ='R' or contype = 'L' or contype = 'O' or contype = 'G') and payments=a.payments) as PU_Repo

,(SELECT COUNT(*) FROM contracts WHERE (status = 'PAID OUT' or status = 'PAID OUT EARLY') and (contype ='R' or contype = 'L' or contype = 'O' or contype = 'G') and payments=a.payments) as PaidOut

,(SELECT AVG(LASTTRANS-CONTRACTDATE) FROM contracts WHERE (status = 'PAID OUT' or status = 'PAID OUT EARLY') and (contype ='R' or contype = 'L' or contype = 'O' or contype = 'G') and payments=a.payments) as PaidOutDAYS

,(SELECT COUNT(*) FROM contracts WHERE (status = 'CHARGE OFF' or status = 'SKIP' or status like '%WRITE OFF') and (contype ='R' or contype = 'L' or contype = 'O' or contype = 'G') and payments=a.payments) as chargeof

,(SELECT AVG(LASTTRANS-CONTRACTDATE) FROM contracts WHERE (status = 'CHARGE OFF' or status = 'SKIP' or status like '%WRITE OFF') and (contype ='R' or contype = 'L' or contype = 'O' or contype = 'G') and payments=a.payments) as chargeofDAYS

,(SELECT COUNT(*) FROM contracts WHERE status <> 'OPEN' AND status <> 'PRINTED-CANCEL' AND status <> 'PRINTED' and (contype ='R' or contype = 'L' or contype = 'O' or contype = 'G') and payments=a.payments) as totalclosed

,(SELECT AVG(LASTTRANS-CONTRACTDATE) FROM contracts WHERE status <> 'OPEN' AND status <> 'PRINTED-CANCEL' AND status <> 'PRINTED' and (contype ='R' or contype = 'L' or contype = 'O' or contype = 'G') and payments=a.payments) as totalclosedDAYS

,(SELECT COUNT(*) FROM contracts WHERE status = 'OPEN' and (contype ='R' or contype = 'L' or contype = 'O' or contype = 'G') and payments=a.payments) as totalactive

from contracts a where (contype ='R' or contype = 'L' or contype = 'O' or contype = 'G') group by payments

The string below may be useful for the NBSRA survey for shed rental companies. It breaks down the number of open and closed contracts by payment count ranges and the number of days open for closed contracts in each payment count range.

select first 1

(select count(*) from contracts where status ='OPEN' and contype ='R' and payments between 24 and 35) as Open24

,(select count(*) from contracts where status <>'OPEN' and status not like 'PRINT%' and contype ='R' and payments between 24 and 35) as closed24

,(select AVG(LASTTRANS-CONTRACTDATE) from contracts where status <>'OPEN' and status not like 'PRINT%' and contype ='R' and payments between 24 and 35) as closed24days

,(select count(*) from contracts where status ='OPEN' and contype ='R' and payments between 36 and 47) as Open36

,(select count(*) from contracts where status <>'OPEN' and status not like 'PRINT%' and contype ='R' and payments between 36 and 47) as closed36

,(select AVG(LASTTRANS-CONTRACTDATE) from contracts where status <>'OPEN' and status not like 'PRINT%' and contype ='R' and payments between 36 and 47) as closed36days

,(select count(*) from contracts where status ='OPEN' and contype ='R' and payments between 48 and 59) as Open48

,(select count(*) from contracts where status <>'OPEN' and status not like 'PRINT%' and contype ='R' and payments between 48 and 59) as closed48

,(select AVG(LASTTRANS-CONTRACTDATE) from contracts where status <>'OPEN' and status not like 'PRINT%' and contype ='R' and payments between 48 and 59) as closed48days

,(select count(*) from contracts where status ='OPEN' and contype ='R' and payments between 60 and 100) as Open60

,(select count(*) from contracts where status <>'OPEN' and status not like 'PRINT%' and contype ='R' and payments between 60 and 100) as closed60

,(select AVG(LASTTRANS-CONTRACTDATE) from contracts where status <>'OPEN' and status not like 'PRINT%' and contype ='R' and payments between 60 and 100) as closed60days

from contracts

The string below will give customer deposit balances as of 12/31/2015 (the dates can be changed to any date). Note this would only be accurate if all deposits were paid through transactions, not through any manual editing or converted data.

SELECT NAME, ACCOUNT, (select sum(deposit) from history where transdate < '1/1/2016' and account= a.ACCOUNT) as depositbalanceÂ 

from customers a 

where (select sum(deposit) from history where transdate < '1/1/2016' and account= a.ACCOUNT) >0

Â 

List of customer / contracts with back rent due from the feature to move due date full term for partial payments

SELECT name, customers.ACCOUNT, contracts.CONTRACT, DUEDATE, CONTRACTDATE, STATUS, BACKRENTDUE

FROM CONTRACTS 

inner join customers on customers.account=contracts.account 

where status = 'OPEN'

The SQL string below uses sub queries as columns to return contract balances for contracts less than 1 year old, more than 1 year old and balance for contracts 30+ days overdue

select first 1

(select sum(contractamt-amtpaid) from contracts where contractdate > current_date -365 and status = 'OPEN') as "bal<1yr",

(select sum(contractamt-amtpaid) from contracts where contractdate < current_date -365 and status = 'OPEN') as "bal>1yr",

(select sum(contractamt-amtpaid) from contracts where current_date - duedate > 29 and status = 'OPEN') as "cbalpastdue"

from contracts

The SQL string below returns various contract details and shows an example of using IIF in the select clause.

select contractdate, contract, contracts.account, customers.name,

contractamt, pmt, payments, cast((contractamt-amtpaid) / pmt as decimal(18,2)) as pmtsleft, contractamt-amtpaid as balance, duedate,

iif(duedate < current_date,current_date - duedate,0) as dayslate, 

iif(duedate < current_date, datediff(MONTH, duedate, current_date), 0) as "MonPMTSPastDue",

iif(duedate < current_date, datediff(MONTH, duedate, current_date) * pmt, 0) as "RentPastDue"

from contracts

inner join customers on customers.account=contracts.account

where status ='OPEN' and contype='R'

Below will display contracts currently open and ones closed in 2017, along with amount paid on the contracts in 2017. 

select a.contract,a.status,customers.name, a."DESCRIPTION 1", a.contractdate, a.lasttrans, a.contractamt, b.AP 

from contracts a

inner join customers on customers.ACCOUNT =a.ACCOUNT

left join (select contract,sum(amount) as AP from history where transdate between '1/1/2017' and '12/31/2017' group by contract )b on b.CONTRACT = a.contract

where a.status ='OPEN' or a.lasttrans between '1/1/2017' and '12/31/2017'

group by 1,2,3,4,5,6,7,8

Below will list name, account, contract for RTO and LTO contracts that were active at end of day on 12/31/2015

select customers.name, customers.account,contracts.contract

from CONTRACTS

left join customers on customers.account=contracts.ACCOUNT

where contype in('R','L') and CONTRACTS.CONTRACTDATE <= '12/31/2015'

and (contracts.status='OPEN' or lasttrans > '12/31/2015')

and status not like 'PRINT%'

Below is a SQL String requested by a shed rental dealer to get commission that was paid as 7% of what they consider the rental fee(the % that does not come off cash price for EPO). The first line shows detail records, the 2nd line is totals by discount percentage. The dates, salesman and vendor name should be edited to match what you are looking for.

select inventory.vendor, contracts.salesman, history.transdate, contracts.PAYOFFDISCOUNT, ((history.AMOUNT * contracts.PAYOFFDISCOUNT)*.07) as commission, history.AMOUNT as rentpaid 

from history 

inner join contracts on contracts.contract=history.CONTRACT

inner join inventory on inventory.contract=history.CONTRACT

where contracts.contype='R' and transdate between '1/1/2018' and '1/31/2018'

and contracts.salesman ='SALESMAN'

and inventory.vendor='VENDOR'

select contracts.PAYOFFDISCOUNT, sum((history.AMOUNT * contracts.PAYOFFDISCOUNT)*.07) as commission, sum(history.AMOUNT) as rentpaid 

from history 

inner join contracts on contracts.contract=history.CONTRACT

inner join inventory on inventory.contract=history.CONTRACT

where contracts.contype='R' and transdate between '1/1/2018' and '1/31/2018'

and contracts.salesman ='SALESMAN'

and inventory.vendor='VENDOR'

group by contracts.PAYOFFDISCOUNT

Below shows account, name, address info, cash price, last tran, status, times over 30 days late, stock and serial, for contracts paid out in a date range.

select a.ACCOUNT,customers.name,customers.ADDRESS,CUSTOMERS.CITY,customers.STATE,customers.ZIP, customers.CELL,customers.HMPHONE,

a.CASHPRICE,a.PMT,a.LASTTRANS,a.STATUS, 

(select count(*) from history where history.DAYSLATE > 30 and contract=a.contract) as lateover30,

inventory.stock, INVENTORY.SERIAL

from contracts a

left join customers on customers.account=a.ACCOUNT

left join INVENTORY on INVENTORY.CONTRACT = a.CONTRACT

where a.status like 'PAID%' and a.CONTYPE ='R' 

and a.LASTTRANS between '1/1/2018' and '12/1/2018'

The string below lists paid out contracts and the total paid on the day they were paid out.

select a.account,a.contract,a.status, a.LASTTRANS, (select sum(amount) from history where transdate = a.LASTTRANS and contract=a.CONTRACT and transtype<>'D') as lastpmt,a.CONTYPE

from contracts a

where a.STATUS like 'PAID%' and a.contype='R' and a.store=1

group by 1,2,3,4,5,6

The SQL string below gives you a lot of the info that ison the customer inquiry screen, listed by account number for all of your customers.

select name, account,

(select count(*) from history where account = a.account and dayslate between 16 and 30 and transtype <> 'D') as "16to30dayslate",

(select count(*) from history where account = a.account and dayslate between 31 and 60 and transtype <> 'D') as "31to60dayslate",

(select count(*) from history where account = a.account and dayslate >60 and transtype <> 'D') as "60dayspluslate",

(select count(*) as concount from contracts where (status = 'SKIP' or status = 'CHARGE OFF') and account = a.account) as skipchargeoffcount,

(select count(*) as concount from contracts where status like 'REPO%' and contype <> 'N' and account = a.account) as repocount,

(select count(*) as concount from contracts where status like 'PAID%' and contype <> 'N' and account = a.account) as paidoutcount,

(select count(*) as concount from contracts where (status = 'PICKED UP' or status = 'RETURNED') and contype <> 'N' and account = a.account) as pickedupcount,

(select sum(amtpaid) from contracts where contype in('R','L','T','G','O') and status <> 'PRINTED' and status <> 'PRINTED-CANCEL' and account = a.account) as rentpaid,

(select sum(amtpaid) from contracts where contype = 'S' and account =a.account) as retailsales

from customers a

Below is a SQL string that uses a UNION to create a sub total line by store/state. You can see this same functionality if you group by store and state in the records viewer if you run this SQL without the UNION section.

SELECT a.store, t.state, cast(a.TRANSDATE as varchar(20)) as "TranDate",a.RECEIPT,a.CONTRACT,a.NAME, cast(a.ACCOUNT as varchar(20)) as "Account", cast(a.DUEDATE as varchar(20)) as "DueDate",

cast(a.DAYSLATE as varchar(20)) as "DaysLate", a.AMOUNT, a.OTHER, a.TAX, a.TOTAL , a.OPERATOR, cast(a.REFUND as varchar(5)) AS VOID, cast(c.pmt as varchar(10)) as STD_PMT, 

cast(c.PAYOFFDISCOUNT as varchar(10)) as "PayoffDiscount"

FROM HISTORY a JOIN CONTRACTS c on (c.Contract = a.contract) join TAXZONES t on (c.Taxzone = t.zone) 

WHERE Transdate >= '1/1/2022' 

and Transdate <= '1/30/2022'

Union

SELECT a.store, t.state, 'TOTAL',' ' as "4" , ' ' as "5" ,' ' as "6", ' ' as "7",' ' as "8",' ' as "9", SUM(a.AMOUNT) as RENT, SUM(a.OTHER) as OTHER, SUM(a.TAX) as TAX, SUM(a.TOTAL) as TOTAL , ' ' as "14", ' ' as "15", ' ' as "16", ' ' as "17"

FROM HISTORY a JOIN CONTRACTS c on (c.Contract = a.contract)

join TAXZONES t on (c.Taxzone = t.zone)

WHERE Transdate >= '1/1/2022'

and Transdate <= '1/30/2022'

GROUP BY a.STORE, t.state

To learn more about SQL string there are many sites online with instructions below is one that is very good.

<http://www.w3schools.com/sql/default.asp>
