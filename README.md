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
