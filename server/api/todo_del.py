from flask import Blueprint, jsonify, Flask, render_template, redirect, request
from server.api.todo_view import todolist

app = Blueprint(
    'todo_del',
    __name__
)

@app.route("/deleteitem/<int:item_id>")
def delete_todoitem(item_id):

  todolist.delete_todoitem(item_id) 
  return redirect("/")

@app.route("/deletealldoneitems")
def delete_alldoneitems():
   todolist.delete_doneitem()
   return redirect("/")
