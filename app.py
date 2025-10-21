#danh sách để lưu các công việc
tasks = []
def add_task(task_name):
    """Thêm một công việc mới vào danh sách."""
    task = {"name": task_name, "completed": False}
    tasks.append(task)
    print(f"Đã thêm công việc:'{task_name}'")
def list_tasks():
    """Liệt kê tất cả các công việc hiện có."""
    if not tasks:
        print("Không có công việc nào trong danh sách.")
    else:
        print("Danh sách công việc:")
        for i, task in enumerate(tasks, start=1):
            status = "[x]" if task["completed"] else "[ ]"
            print(f"{i}. {status} {task['name']}")
def complete_task(task_index):
    """Đánh dấu một công việc là hoàn thành."""
    if 0 < task_index <= len(tasks):
        tasks[task_index - 1]["completed"] = True
        print(f"Đã đánh dấu công việc '{tasks[task_index - 1]['name']}' là hoàn thành!")
    else:
        print("Chỉ số không hợp lệ, không thể đánh dấu hoàn thành.")
def delete_task(task_index):
    """Xóa một công việc khỏi danh sách theo chỉ số (1-based)."""
    if 0 < task_index <= len(tasks):
        removed = tasks.pop(task_index - 1)
        print(f"Đã xóa công việc: '{removed['name']}'")
    else:
        print("Chỉ số không hợp lệ, không thể xóa công việc.")
#---Điểm bắt đầu của chương trình---
if __name__ == "__main__":
    print("Chào mừng đến với ứng dụng To-Do List!")
    add_task("Học bài Git và GitHub")
    add_task("Làm bài tập thực hành ở nhà")
    print()
    list_tasks()
    print()
    complete_task(1)
    list_tasks()
    print()
    delete_task(2)   
    list_tasks()