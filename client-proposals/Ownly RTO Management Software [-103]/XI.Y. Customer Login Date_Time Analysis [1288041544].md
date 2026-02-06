11.25. Customer Login Date/Time Analysis

In the login date/time RG, break it into a time bucket.

  * if Mon-Fri from 8a to 8p, put it into one of these buckets
    * 8a-10a
    * 10a-12p
    * 12p-2p
    * 2p-4p
    * 4p-6p
    * 6p-8p
  * Otherwise, put it into:
    * After Hours



  


  * on the customer record, add a macro to find the most popular login times. If there are multiple:
    * If there's only 1-2 during business hours, show that
    * If there's 3 or more during business hours, show the first one and X more, like "4p-6p and 3 more"
    * If it's only during business hours, show After Hours


