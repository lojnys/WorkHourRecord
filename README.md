# Work Hour Recorder

## Description
This application helps user keep track of the number of hours that they have worked.

## User Story
- As an user, I want to be able to number of hours worked, with corresponding hourly rate.
- As an user, I want to be able to add up number of hours, calculated by bi-monthly. 
- As an user, I want to be able to choose between the previous weeks.


## Daily Logs

*06/17/23*
- Added more models
- Finalized the UI
    - Added the "Welcome" label
    - Added the display for the previous weeks
    - Added the buttons and entries to add
- Added functionality of loading the json file 

*06/17/23*
- Added functionality of the "Add Amount" button and the "Set Week" button

*06/23/23*
- Added one more button for adding more work time slots
- Function of adding work time to the work time slot added
- Created 'test' folder for the tests
- Created a work time test using unittest

*07/01/23*
- Added tests
- Function of adding week
    - New window with a label and a button
    - button function of creating a WorkTimes and add to BiWeekly then dump to JSON
- Added function on closing
- Exported as an executable file
- addAmount()
    - Looks at notes - place of work, then organize/print the amount for each place
    - Ex. "Place 1: $50, Place 2: $400, ..."