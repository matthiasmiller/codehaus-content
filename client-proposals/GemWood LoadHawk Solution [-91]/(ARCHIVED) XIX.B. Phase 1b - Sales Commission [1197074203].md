19.2. Phase 1b - Sales Commission

_VA: 

Tim Reitz 10/09/2024: All of the below items have been incorporated into the proposal spec. 

Let's archive this section at some point. 

\-----------------

HLD notes: 

  


Sales Commission:

  * Records
    * Contacts
      * [X] Contact Type - Salesperson
      * [X] Sales Commission % (number; 2 decimals; visible for Members section)
    * [X] Silverloom Settings - Default Salesperson
    * [X] Delivery Ticket
      * Salesperson (default to "Default Salesperson"; required; list of Salesperson; warn if changing after commission is paid)
      * Sales Commission Payment Date
      * Sales Commission % (read-only; calculated and stored when entering commission payment date)
      * Sales Commission Payment $ (read-only; calculated and stored when entering commission payment date)
  * [X] Report - Unpaid Commission
    * Include:
      * Closed Delivery Tickets with unpaid commission
    * Filter:
      * Salesperson (blank = all)
    * Group by Salesperson
    * Report on closed Delivery Tickets with unpaid commission:
      * Ticket #
      * Buyer
      * Member
      * Ticket Total $
      * Commission %
      * Commission $
    * Button to apply payments (sets payment date and freezes commission totals)
  * [X] Report - Paid Commission
    * Same as the above, but filters by date range, groups by date, including paid commission


