6\. Increase Ease of Printing

  


Requirements

It would be good to have a faster way to print the printouts (currently the user has to scroll to the bottom of the Quote/Order page to access the buttons):  

  * Add a button to the top frame of the quote/order detail screen, beside Save: Print Quote/Order 
    * This should have the same behavior as the existing Print Quote/Order button at the bottom of the detail screen. 
    * Note that this will always open the printout in the same tab. To get back to the order screen, the user will need to use the back button. 
  * Add the "Analysis" menu to the top right of the frame with 1 option: Print Packing List 
    * This should have the same behavior as the existing Print Packing List button at the bottom of the detail screen. 
    * Note that CCI, CH, and Triple D are aware that we can't change the menu title at this point but we might be able to change it in the future.



  


Time Estimate: 1 day

  


Development Specification

From [[[IN4858](https://zch.apphosting.zone/Detail/Edit/2?RecordType=Incidents&NumberID=-4860&)]] - ZTD - Increase Ease of Printing: 

  


Increase Ease of Printing: It would be good to have a faster way to print the printouts (currently the user has to scroll to the bottom of the Quote/Order page to access the buttons):  

  * Add a button to the top frame of the quote/order detail screen, beside Save: Print Quote/Order 
    * This should have the same behavior as the existing Print Quote/Order button at the bottom of the detail screen. 
    * Note that this will always open the printout in the same tab. To get back to the order screen, the user will need to use the back button. 
  * Add the "Analysis" menu to the top right of the frame with 1 option: Print Packing List 
    * This should have the same behavior as the existing Print Packing List button at the bottom of the detail screen. 
    * Note that CCI, CH, and Triple D are aware that we can't change the menu title at this point but we might be able to change it in the future.



  


  


Dev Spec: 

  * Create an list something like OrdersDtlRptMenu with one item with the same label and path as the Print Packing List button. See [[WS0001264]]
  * Add a detail property to the order detail screen with a TitleBarButtonPath / TitleBarButtonLabel setting for the Print Quote/Order button. See [https://clientscope.invtools.com/Detail/View/2?RecordType=WikiPages&NumberID=-999&InvestUrl=8-P&State=7Jyj3oFhF7k&](https://clientscope.invtools.com/Detail/View/2?RecordType=WikiPages&NumberID=-999&InvestUrl=8-P&State=7Jyj3oFhF7k&)



Estimate: 1 day.
