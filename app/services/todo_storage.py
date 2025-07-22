import json
from pathlib import Path
from datetime import datetime

TODO_FILE = Path("todo_list.json")

def save_todo_to_file(todo: dict, file_path: Path = TODO_FILE):
    if file_path.exists():
        todos = json.loads(file_path.read_text())
    else:
        todos = []

    todo["created_at"] = datetime.now().isoformat()
    todo["done"] = False
    todos.append(todo)
    file_path.write_text(json.dumps(todos, indent=2))

def save_todos_to_file(todos, file_path=TODO_FILE):
    file_path.write_text(json.dumps(todos, indent=2))

def load_all_todos(file_path=TODO_FILE):
    if not file_path.exists():
        return []

    try:
        todos = json.loads(file_path.read_text())
        assert isinstance(todos, list)
        return todos
    except Exception as e:
        print("Failed to load todos:", e)
        return []

def load_todos_for_today(file_path: Path = TODO_FILE):
    if not file_path.exists():
        print(f"⚠️ No todo file found at {file_path}")
        return []

    todos = json.loads(file_path.read_text())
    today = datetime.now().date()

    return [
        todo for todo in load_all_todos(file_path)
        if todo.get("due") == today and not todo.get("done", False)
    ]