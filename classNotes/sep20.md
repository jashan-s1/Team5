Sep 20 : Afternoon Notes

## Basis of User Interface Design

**TODO:Prepare user interface for project, and update spec.md**

A beautiful UI may not be the best UI. A UI should be designed to be functional, and not just beautiful.

Purpose of UI is to perform task.

> A user interface is well designed when the program behaves the way the user thought it would.

A good UI makes user feel in control
A bad UI makes user feel confused

NSYS has bad UI but still in use.
- It is used because it is the only option available.
- It has a small userbase so they can be trained

**User does not want to use software, they use it when they need to get something done.**

### When new user uses software
- User is not a blank state
- Users have prior expectations
- If user has useed similar software they will expect it to work similarly
- The user will want the software to use common conventions
    (Do not reinvent the wheel, no need to redefine Ctrl + C)
- User will try to guess what how the UI will behave

### User Model & Program Model

User has a mental model of how the software will behave. 
Program should behave in a way that matches the user's mental model.
aka. 'program model' should match the user's 'mental model'.

> Mock UI: To simulate the UI without creating the program

- Stick to UI conventions of the Platform
- Check the conventions used by similar software
- Be consistent
    - Consistency helps people learn the UI faster
    - Don't be creative with UI
    - Use similar UI for similar tasks

**Don't give user too many options.**
McDonalds vs Subway

### Choices
- Choices are good and bad
- Don't explicitly ask user to make a choice
- Give the user good defaults
- Don't ask user to make a choice when it is not needed
**User cares about the task, not the software.**
- More choices > More Code > More cost > More bugs > More maintenance

### Users and manuals
**Users don't read the manual**
- Users only read the manual if
    - Only is task is critical
    - After they used the software and are stuck
- The average user might not even know that a manual exists
- Design the software so that it does not need a manual
- Do not force on-screen instructions

### Users have a general lack of skill
- People find it hard to control pointers
- People have trouble with double-click
- Make UI elements easy to click
- Provide keyboard shortcuts

### Golden Rule of UI
Single criteria for every application and user: **I must not look like a fool**

### Software reccomendation to design UI
- Figma
- Axure
- Pen and Paper
