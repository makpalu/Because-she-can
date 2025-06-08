#Creating a todolist using classes and functions
from datetime import datetime
# class Todo():
#   def __init__(self, name, description):
#     print("Todo Class initialized")
#     self.todo_id = 1
#     self.name = name
#     self.description = description
#     self.priority_level = 0
#     self.deadline = datetime(2026, 12, 25, 0,0,0)
#     self.completed = False
#     self.movability = True

  # def print_information(self):
  #   print(f"id: {self.todo_id}; name: {self.name}; date: {self.deadline}")


class Todolist():
  def __init__(self, name, description):
    self.name = name
    self.description = description
    self.todos:list[Todo] = []


  def set_name(self, name):
    self.name = name

  def set_description(self, description):
    self.description = description

  def get_name(self):
    return self.name

  def get_description(self):
    return self.description

  def add_todo(self, todo):
    self.todos.append(todo)

  def get_todos(self):
    return self.todos

  def get_todo_names(self):
    # todo_names:list[str] = []
    # for todo in self.todos:
    #   todo_names.append(todo.get_name())
    # return todo_names
    return [todo.get_name() for todo in self.todos]

class Todo():
  def __init__(self, name, todo_id, priority_level, deadline, completed, movability):
    self.name = name
    self.todo_id = todo_id
    self.priority_level = priority_level
    self.deadline = deadline
    self.completed = completed
    self.movability = movability

#getters and setters for name
  def set_name(self, name):
    self.name = name

  def get_name(self):
    return self.name

#getters and setters for todo_id
  def set_todo_id(self, todo_id):
    self.todo_id = todo_id

  def get_todo_id(self):
    return self.todo_id

#getters and setters for priority_level
  def set_priority_level(self, priority):
    self.priority_level = priority

    if priority < 1:
      self.priority_level = 1
    elif priority > 4:
      self.priority_level = 4
    elif priority == int(priority):
      return self.priority_level

  def get_priority_level(self):
    return self.priority_level

#getters and setters for deadline
  def set_deadline(self, deadline):
    self.deadline = deadline

  def get_deadline(self):
    self.deadline

#getters and setters for completed
  def set_completed(self, completed):
    self.completed = completed

  def get_completed(self):
    return self.completed

#getters and setters for movability
  def set_movability(self, movability):
    self.movability = movability

  def get_movability(self):
    return self.movability




