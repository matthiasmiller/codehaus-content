8.1.11. Sales Tax on Sales Forms

Seth Miller 01/27/2026: TODO_Seth

  


Sales tax on Sales Forms

  * jurisdiction, rates, liability, and reporting.



  


We are needing to report sales tax on sales forms. I wonder if we want to move the RG out to a new record:

  


\- Type (Contract / Sales Form)

\- Record ID (number)

\- Existing RG

  


We can then kick off an x30 to update it on change, but also run an x30 nightly to update all.
