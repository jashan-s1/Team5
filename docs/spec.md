# THE MAVERICKS
28 September 2023
# Library Management System

## The Team
• Abhishek Dhureja
• Akash Kapoor
• Guru Singh Pal
• Jashandeep Singh
• Utsav Pandey
• Yuvraj Singh Cheema


## Introduction

Well, LMS is like your personal library. It helps keep track of all those things, so you can find what you want and borrow it hassle-free. So, if you're a librarian, it helps you organize the library like a pro. And if you're someone who loves reading, it makes finding and borrowing books a breeze. No more hunting for hours or wondering when your books are due back. LMS is all about making your library experience smooth and enjoyable. Let's dive in and see how it can improve your library adventures!

## Purpose
The purpose of a Library Management System (LMS) is to efficiently and effectively manage all aspects of a library's operations and resources.  It also helps in managing & tracking the daily work of the library such as issuing books, return books, due calculations, etc. This software-based system is designed to streamline the processes involved in cataloguing, organizing, circulating, and maintaining a library's collection of books, digital media, periodicals, and other materials.

## Requirement Analysis

Libraries are a large scale collection of books, music and other media. To manage such database special computer programs are required. 

We intend to make a library management program to track the media available, the application will have information about the media for the users including the title, publisher and author etc. For the admins the application will have features which allow them to edit the data entries of the media in the library.

**THE TARGET AUDIENCE:** The application intends to make the task of a Librarian easy, as well as allow an easy interface for the readers to manage borrowed books.

The app will be termed as successful if a new user can easily find their required media from the application


## Functional Specification

For a user the app will have a home page with previous searched and borrowed media. A search bar on top will allow the user to browse through content in the library.

### User Functions

**Check-In/Check-Out:**
1. Borrowing and returning items.
2. Due date calculation and notification.
3. Overdue fines and penalty management.

**Search and Discovery:**
1. Robust search functionality, including advanced search options.
2. Filtering and sorting options.
3. Availability status of items.

**User History:**
1. Keep a record of users' borrowing history.
2. View and export borrowing history.

**Notifications:**
1. Announcements and updates from the library.
2. Notifications for overdue items, fines, etc.

**Fine Management:**
1. Accept and track fine payments.

### Admin Functions

**User Management:**
1. User registration and authentication
2. User access control
3. Profile management

**Catalogue Management:**
1. Add, edit, and delete books and other library items.
2. Copy management (tracking multiple copies of the same book).
3. Categorization and classification of items by genre, author, subject, etc.

**Inventory Management:**
1. Track and manage the library's physical inventory.
2. Handle lost, damaged, or missing items.

**Fine Management:**
1. Configure fine rates and policies.
2. Accept and track fine payments.


### Scenarios

Assuming Isabella wants to borrow a book for Phineas, she will navigate to the appplication and search for the book, she can furter narrow down the results using specific authors, publishers or even use ISBN number to search for the book.

## External Interface

The application needs to communicate with the database in the backend to get the information about the books available


## Technical Spec

- The primary user of the app will be on Windows machines
- The app will be web based
- We will be using php for server side scripting
