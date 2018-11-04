from flask import Blueprint, jsonify, Flask, render_template, redirect, request
from server.api.todo_view import todolist

app = Blueprint(
    'todo_add',
    __name__
)

##
# 追加処理
##
@app.route("/additem", methods=["POST"])
def add():
    title = request.form["title"]
    if not title:
        return redirect("/")
    ## タイトル追加
    todolist.add(title)
    return redirect("/")