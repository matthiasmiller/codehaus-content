30\. Investor Deal Room

  


Requirements

Contains visible question and answer thread (classified ad page to opportunities or available funds)

  


TODO_CH: How do we do the question and answer thread?

  


Every comment will be a record that is tied to an investment opportunity or a parent comment. This should prevent edit collisions.

There would also be a report that has all threads but is sorted by the thread with most recent activity. This would be an auto-updating report.

  


Group by: thread

Sorted by: most recent comment ID

There would be a "reply" link that would open a new window

Index records and create a new report every 30 days?

  


Comment record

\- Comment ID (auto-number)

\- Parent ID (number; optional for new thread)

\- Investment Opportunity ID (if linked to IO)

\- Author (list of contacts)

\- Date / Time (stored in GMT, shown in local time)

\- Comments

  


Report:

\- Model to collect all comments in last X days (i.e. 30)

\- Report to show all comments in those threads

\- Group by thread ID, reverse sorted by latest comment date

\- Inline "Reply" links that open a New Comment record that automatically links back to the selected comment

\- Consider also a "New Comment" link ala FB threads

  


Development Specification

View: [https://www.figma.com/proto/n7VfJH7fKIeadeGdOmQhae/Symbiz-Wireframe?page-id=0%3A1&node-id=950%3A14678&scaling=min-zoom&starting-point-node-id=9%3A3](https://www.figma.com/proto/n7VfJH7fKIeadeGdOmQhae/Symbiz-Wireframe?page-id=0%3A1&node-id=950%3A14678&scaling=min-zoom&starting-point-node-id=9%3A3)

  


View: [https://www.figma.com/proto/n7VfJH7fKIeadeGdOmQhae/Symbiz-Wireframe?page-id=0%3A1&node-id=646%3A4753&scaling=min-zoom&starting-point-node-id=9%3A3](https://www.figma.com/proto/n7VfJH7fKIeadeGdOmQhae/Symbiz-Wireframe?page-id=0%3A1&node-id=646%3A4753&scaling=min-zoom&starting-point-node-id=9%3A3)
