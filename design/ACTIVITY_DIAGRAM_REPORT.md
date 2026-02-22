# CP Assignment #6 – Activity Diagram Report

This document contains UML Activity Diagrams derived from User Acceptance Test (UAT) scenarios.  
Each diagram models system behaviour, user interactions, validation logic, decision paths, and alternate flows.

----------------------------------------------------------------
## AD-01 – (To be completed)
Related UAT Test Case: TC-01

Purpose:
(To be completed)

----------------------------------------------------------------
## AD-02 – Edit Workout Plan
Related UAT Test Case: TC-02 Edit Workout Plan

Purpose:
This diagram illustrates the workflow for editing an existing workout plan. The user logs into the system, navigates to stored workout plans, and selects a plan to modify. The system loads the plan and allows the user to edit exercise parameters such as sets and repetitions. The system validates the input before saving changes. Valid updates are stored in the database, while invalid inputs trigger validation errors and prevent data updates.

Key Behaviours Modeled:
- User interaction with stored plans
- System validation logic
- Decision paths for valid vs invalid input
- Database update process
- Alternate error flow

----------------------------------------------------------------
## AD-03 – (To be completed)
Related UAT Test Case: TC-03

Purpose:
(To be completed)

----------------------------------------------------------------
## AD-04 – Prevent Starting Empty Workout Plan
Related UAT Test Case: TC-04 Prevent Starting Empty Workout Plan

Purpose:
This activity diagram models the validation process executed when a user attempts to start a workout. After selecting a workout plan, the system checks whether the plan contains exercises. If exercises exist, the system creates a workout session and loads exercises. If no exercises are found, the system blocks the workflow, displays an error message, and redirects the user back to editing. This diagram emphasises defensive system behaviour and error prevention.

Key Behaviours Modeled:
- Precondition validation
- Decision-based control flow
- Session creation logic
- Alternate error handling path
- User recovery flow

----------------------------------------------------------------
## AD-05 – Organising Workouts by Day
Related UAT Test Case: TC-05 Organising Workouts by Day

Purpose:
This diagram represents how users schedule workout plans by assigning them to specific days of the week. The system loads existing plans, the user selects a plan, and chooses a day. The system validates scheduling constraints before persisting changes. Valid schedules update the dashboard, while invalid configurations trigger scheduling errors. The diagram captures both normal and exception flows.

Key Behaviours Modeled:
- Dashboard interaction
- Scheduling workflow
- Validation rules
- Database persistence
- Alternate validation failure flow

----------------------------------------------------------------
## AD-06 – (To be completed)
Related UAT Test Case: TC-06

Purpose:
(To be completed)

----------------------------------------------------------------
## AD-07 – (To be completed)
Related UAT Test Case: TC-07

Purpose:
(To be completed)

----------------------------------------------------------------
## AD-08 – (To be completed)
Related UAT Test Case: TC-08

Purpose:
(To be completed)

----------------------------------------------------------------
## AD-09 – (To be completed)
Related UAT Test Case: TC-09

Purpose:
(To be completed)

----------------------------------------------------------------
## AD-10 – (To be completed)
Related UAT Test Case: TC-10

Purpose:
(To be completed)
