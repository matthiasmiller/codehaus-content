9.9. Performance Reporting

  


Requirements

This report is used to view/track the following:

  * Need to be able to see how much activity is happening
  * Efficiency of their days



  


Context: 

  * Kuntry Kettle's pricing (e.g. jam) is based on the assumption that they can do 630 cases per day. They need to be able to confirm that they can actually perform that amount. 
  * Kuntry Kettle needs to be able to keep a throttle. For example, their production had never been this high before, but they had no context that anything special was happening. A few days a week, they might be doing 945 cases instead of 630. They need something they can measure, plan, and control activity by.



  


They've made some changes to the flow this year, and they can measure the amount of work vs. the work they had been doing last year.

  


This is based on a point system. It will include a number of graphs and reports.

  


Development Specification

Sample: 

PDF: [https://drive.google.com/file/d/1A23M4EtlKYdIPWWjztQgmr5FvhTK_LU7/view?usp=share_link](https://drive.google.com/file/d/1A23M4EtlKYdIPWWjztQgmr5FvhTK_LU7/view?usp=share_link)

  


  


TODO_IDD - Define # of points for changeovers on the Changeover SKU

  * For the jar and lid changeover, this should be a field defined on the order -- have a box to check when the order's entered, for changeover
  * Container Changeovers
  * Lid Changeover



Total changeovers on the sales order

  


Matthias Miller 12/07/2022: What qualifies as a production day?

  * Matthias Miller 12/07/2022: Any day that production happens is a production day
  * Matthias Miller 12/07/2022: The 1800 target points =
    * total operating expense
    * plans to run 216 days / year of production
    * divide operating expenses by 216 days == basis operating expense overhead
  * Then on the overhead



216 days, at 100 points per day, then divide that out monthly
