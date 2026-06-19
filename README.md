# ToDo-List (Updated)
A simple To-Do List using Django

![image](https://github.com/Rakkues/ToDo-List-Evo/blob/a566fa0e6d3176f412e5649d1bdfd650131d70ed/new_dashboard.png)

## Key Features Added
- **Full Task Editing**: You can now update or change any part of a task after creating it.
- **Detailed Time Tracking**: Instead of just typing text, you can choose the exact Days, Hours, and Minutes a task will take using simple dropdown menus.
- **File & Image Attachments**: You can upload photos or documents directly to any task to keep your notes together.
- **Search & Filter Controls**: You can search for tasks by typing keywords, or filter them by high/medium/low priority and completion status.

## Core Installation & Project Setup
1. Clone the project dependencies and navigate into your localized execution workspace:
   ```bash
   git clone [https://github.com/Rakkues/ToDo-List-Evo.git](https://github.com/Rakkues/ToDo-List-Evo.git)
   cd ToDo-List-Evo

2. Set Up the Virtual Environment by creating an isolated environment to keep the project files clean, and activate it:
   ```bash
   python -m venv venv
   venv\Scripts\activate

3. Install Packages & Prepare the Database. Install Django and the required image tool (Pillow), then run the setup commands to build your database file cleanly:
   ```bash
   pip install django pillow
   python manage.py makemigrations todo_list
   python manage.py migrate --run-syncdb

4. Launch the local web server so you can open the application in your browser:
   ```bash
   python manage.py runserver

## How to Use the Application

Once the server is running and you open the app in your browser, here is how to use the new features:

1. **Adding a Task**: Click the primary **"Add Task"** button. Fill out the task description, select a priority level, set an optional due date, choose the duration from the Days/Hours/Minutes dropdowns, and attach any files or images.
2. **Searching & Filtering**: Use the filter bar at the top of the task list to look up specific keywords, view only "Pending" or "Completed" tasks, or view tasks by priority level.
3. **Editing a Task**: Click the blue **Edit icon** on any task row to open the edit page. You can change any details, update the duration dropdowns, or change/clear your attached files. Click save to update the task.
