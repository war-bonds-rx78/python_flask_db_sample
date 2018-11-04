from flask import Blueprint, jsonify, Flask, render_template, redirect, request
from server.dao.todo_dao import TodoList

app = Blueprint(
    'todo_view',
    __name__
)

todolist = TodoList()

# 
# トップ画面
#
@app.route("/")
def show_todolist():
    # 値取得
    return render_template("showtodo.html", todolist=todolist.get_all())