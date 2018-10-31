from server.models.models import ToDoItem
from server.config.db_connection import begin, close, commit

class TodoList:

    def add(self, title):
        item = ToDoItem(title=title, done=False)
        session = begin()
        session.add(item)
        commit(session)
        close(session)

    def get_all(self):
        session = begin()
        item = session.query(ToDoItem).all()
        close(session)
        return item