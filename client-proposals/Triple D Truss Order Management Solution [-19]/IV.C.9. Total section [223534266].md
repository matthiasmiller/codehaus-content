4.3.9. Total section

Total section (located below the Metal section if Metal section is visible; if Metal section is not visible but Lumber section is visible, located below Lumber section; otherwise located below Truss Prints section):

  * Read-only table with the following:
    * Columns:
      * Order Total (auto-set and read-only; displays Qty * Unit Price for all rows in the corresponding RG for the current row in the table)
      * Calculated Total (auto-set and read-only; displays Qty * the unit price looked up from the SKU for all rows in the corresponding RG for the current row in the table)
      * Difference (auto-set and read-only; displays the difference between the Order Total and the Calculated Total; displays in gray text if 0, green text if negative, and red text if positive)
    * Rows:
      * Total Truss Price
      * Total Lumber Price
      * Total Metal Price
      * Sub Total (sum of the rows above for Order Total, Calculated Total, and Difference Columns)
  * Update Weights & Prices (button; visible if the Difference column is not zero; resets Unit Weight and Unit Price to the default for the selected SKU for all RG rows)
  * <x.xx>% Discount (visible if "Order Discount %" is not blank; label displays the entered discount %; auto-set and read-only; displays product of Order Discount & and Sub Total  for the Order Total column)
  * <State> <x.xx>% Tax (with the following details:
    * Taxable checkbox: Turns on/off the tax calculation for the order; defaults to checked, including tax for the order; if unchecked, the tax amount is set to "$0.00", but the other tax-related details remain visible;
    * "<State>": Auto-set and read-only, displaying the abbreviation for the selected Delivery State;
    * "<x.xx>%": Required; defaults to the Current Rate for the selected Delivery State; remains editable;
    * validation warning on the field and on every Save if the entered tax rate does not match the Current Rate for the selected Delivery State: "The entered rate (<x.xx>%) does not match the current <ST> rate (<x.xx>%).";
    * Calculated tax amount field in line with the Order Total column: Displays the amount of tax for the order, based on the Sub Total - Discount * Tax Rate)
  * Total (sum of Sub Total, -Discount Amount, and Tax)
  * Deposit Amount (located below Total field; optional; number field allowing 2 decimals; defaults to blank)
  * Deposit Comments (located to the right of the Deposit Amount field; multi-line plain text field, large enough for approximately 60 characters; note that this field should be small, similar to the Job Information memo)
  * Remaining Balance (located below "Deposit Amount"; auto-set and read-only; number; 2 decimals; displays the value of "Total" \- "Deposit Amount")
  * Print Order (button; visible if "Truss Order", "Lumber Order", or "Metal Order" is checked; displays as "Print Quote" if Status = Quote; opens the Quote / Order Printout as a PDF in a new tab)
  * View in Word (link; located to the right of the "Print Order" button; visible if "Truss Order", "Lumber Order", or "Metal Order" is checked; downloads the Quote / Order Printout as a Word file)
  * Print Standard Packing List (button; visible if "Truss Order", "Lumber Order", or "Metal Order" is checked; opens the Standard Packing List Printout as a PDF in a new tab)
  * View in Word (link; located to the right of the "Print Standard Packing List" button; visible if "Truss Order", "Lumber Order", or "Metal Order" is checked; downloads the Standard Packing List Printout as a Word file)
  * Print Yard Packing List (button; located beneath "Print Standard Packing List" button; visible if "Truss Order", "Lumber Order", or "Metal Order" is checked; opens the Yard Packing List Printout as a PDF in a new tab)


