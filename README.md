# Neobis_ToDo_Project

This is a simple Todo app built with Django that allows users to manage their tasks. Users can add, edit, mark as completed, and delete tasks using the web interface.

## Requirements

* Python 3.x
* Django 3.x

## Installation
1. Clone the repository to your local machine:
 ```
git clone https://github.com/your_username/todo_app.git
cd todo_app
  ```

Steps and commands for Linux machine are the same but use python3 instead of python.

2. Create and activate a virtual environment (optional but recommended):
 ```
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```
3. Install the required dependencies:
```
pip install -r requirements.txt
```
4. Apply migration to setup the database:
```
python manage.py makemigrations
python manage.py migrate
```

5. Start the development server:
```
python manage.py runserver
```
6. Open your web browser and navigate to http://localhost:8000/ to access the Todo app.

## Usage

* #### Add Task:
On the main page, enter the title and description of the task in the provided input fields and click the "Add" button to create a new task.
* #### Edit Task:
To edit a task, click on the "Edit" button next to the task you wish to modify. This will take you to the edit page, where you can update the title and description of the task. Click the "Update" button to save the changes.
* #### Mark as completed:
To mark a task as completed, click on the "Mark as completed" button next to the task on the main page. The task will then be marked as done and displayed with a green label.
* #### Mark as Not Completed:
If a task is marked as completed, you can click on the "Mark as not completed" button to change its status back to undone.
* #### Delete Task:
 To delete a task, click on the "Delete" button next to the task on the main page. This will remove the task from the list.

## File Structure
* ##### ToDo/models.py:
  Defines the ToDo model for tasks.
* ##### ToDo/views.py:
  Contains the views for handling different actions, including adding, editing, marking as completed, and deleting tasks.
* ##### ToDO/templates/ToDo/index.html:
  Main page template displaying the list of tasks.
* ##### ToDO/templates/ToDo/edit_todo.html:
  Template for editing task details.
* ##### ToDO/templates/ToDo/description.html:
  Template displaying the description of a specific task.
* ##### ToDo/urls.py:
  Contains URL patterns for mapping views to URLs.



