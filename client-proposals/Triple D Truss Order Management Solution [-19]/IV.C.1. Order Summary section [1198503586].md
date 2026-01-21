4.3.1. Order Summary section

Order Summary section:

  * Canceled (optional; checkbox; when checked, makes the record read-only for non-admin users; displayed above the section header; when checked, displays a red label: "This quote is canceled." or "This order is canceled."; defaults to unchecked)
  * "This whole order has passed both Delivery / Pickup Dates and therefore is considered complete." (displayed above the section header; displays in red text; visible if the current date is later than both the Delivery Date and Pickup Date)
  * New Delivery (link; located above the Order Summary section; opens a new Delivery record in a new tab with the Quote / Order field defaulted; note that this link can be used by all users)
  * Create Delivery (checkbox; visible if Status = "Order" and there are no linked Delivery records; with the following behaviors:
    * defaults to checked; 
    * when hidden (if Status = Quote or if there are any linked Delivery records), is unchecked;
    * if this record is not referenced on any Delivery records, on the first Save after this checkbox is visible and checked, the "Create & Link Delivery" Automatic Process runs - see corresponding spec)
  * <X> Linked Delivery(s) (link; located above the Order Summary section; with the following behaviors:
    * if there is only one linked Delivery record, opens that record;
    * if there are more than one linked Delivery records, opens a report of a linked Deliveries for the corresponding Quote or Order)
  * Canceled (optional; checkbox; when checked, makes the record read-only for non-admin users; displayed above the section header; when checked, displays a red label: "This quote is canceled." or "This order is canceled."; defaults to unchecked)
  * "This whole order has passed both Delivery / Pickup Dates and therefore is considered complete." (displayed above the section header; displays in red text; visible if the current date is later than both the Delivery Date and Pickup Date)
  * Bid Date (optional; date; defaults to current date)
  * Revised Date (optional; date; defaults to current date)
  * Update button (changes Revised Date to current date)
  * Status (required; drop-list of Quote, Order; defaults to Quote; 
  * Order Discount % (optional; number; two decimals)
  * Order Date (date; defaults to current date; required if Status = Order)
  * Order Total (auto-set and read-only; number; two decimals; sum of total truss price, total lumber price, and total metal price)
  * Salesperson (optional; drop-list of Salesperson type contacts; defaults to the current user if they are a Salesperson)
  * Sales Phone (read-only; the work number for the selected Salesperson)
  * Sales Fax (read-only; the fax number for the selected Salesperson)
  * Loading GSL (optional; number; no decimals; maximum of 3 digits)
  * Spacing (editable drop-list; default items include 16in, 2ft, and 4ft)
  * P. O. Number (optional; number; no decimals)
  * TCLL (optional; number; no decimals; maximum of 3 digits)
  * Residential / Commercial (checkbox; when checked, unchecks Agriculture)
  * Truss Order (checkbox; required if "Lumber Order" or "Metal Order" is not checked; when checked, makes Truss section visible)
  * TCDL (optional; number; no decimals; maximum of 3 digits)
  * Agriculture (optional; checkbox; when checked, unchecks Residential / Commercial)
  * Lumber Order (required if "Truss Order" or "Metal Order" is not checked; checkbox; when checked, makes Lumber section visible)
  * BCDL (optional; number; no decimals; maximum of 3 digits)
  * Metal Order (required if "Truss Order" or "Lumber Order" is not checked; checkbox; when checked, makes Metal section visible)
  * Attic Loading (optional; plain text field)


