import sys
from pathlib import Path

# Add project root to sys.path
root_path = Path(__file__).resolve().parents[2]
sys.path.append(str(root_path))

import streamlit as st
import time
from app.services.todo_storage import load_all_todos, save_todos_to_file

st.set_page_config(page_title="PropPilot Todo Dashboard", layout="centered")

st.title("📝 PropPilot - Todo Dashboard")

# Load todos
todos = load_all_todos()

# Separate into pending and completed
pending_todos = [t for t in todos if not t.get("done", False)]
completed_todos = [t for t in todos if t.get("done", False)]

st.subheader("📌 Pending Tasks")
if not pending_todos:
    st.info("No pending tasks today. Nice work!")
else:
    for idx, todo in enumerate(pending_todos):
        st.markdown(f"- **{todo['task']}** (Due: {todo['due']})")
        if st.button("✅ Mark as Done", key=f"done_{idx}"):
            # Find index in full todo list
            original_idx = todos.index(todo)
            todos[original_idx]["done"] = True
            save_todos_to_file(todos)
            st.rerun()

# Divider
st.markdown("---")

# Add New Todo
st.markdown("## ➕ Add New Todo")
new_task = st.text_input("Task")
new_due = st.date_input("Due Date")

if st.button("Add Task"):
    new_todo = {
        "task": new_task,
        "due": new_due.isoformat(),
        "created_at": st.session_state.get("created_at", None)
    }
    todos.append(new_todo)
    save_todos_to_file(todos)
    st.success("Todo added.")
    st.rerun()

# Optionally show completed
if completed_todos:
    if st.checkbox("✅ Show completed tasks"):
        st.subheader("🎉 Completed")
        for todo in completed_todos:
            st.markdown(f"- ~~{todo['task']}~~ (Done)")