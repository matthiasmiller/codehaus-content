8.1.9. Sales Tax on Sales Invoices

Seth Miller 01/27/2026: TODO_Seth.

  


Sales tax on Sales Forms

  * jurisdiction, rates, liability, and reporting.



  


Seth Miller 02/04/2026: TODO_Sean for basic fielding. [[PC0189763]]

Seth Miller 02/04/2026: TODO_Seth for caching liability. [[PC0189765]]

  


We are needing to report sales tax on sales forms. I wonder if we want to move the RG out to a new record:

Seth Miller 02/04/2026: Jasper coded this.

  


\- Type (Contract / Sales Form)

\- Record ID (number)

\- Existing RG

  


We can then kick off an x30 to update it on change, but also run an x30 nightly to update all.
