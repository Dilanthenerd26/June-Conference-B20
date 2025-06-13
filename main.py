import time
from datetime import datetime, timedelta
import threading
import queue

# --- CONFIGURATION ---
REMINDER_INTERVAL = 5  # seconds between reminders
REMINDER_COUNT = 3  # total reminders per task
TEST_INTERVAL = 5  # seconds between new tasks

# --- SETUP START TIME ---
current_time = datetime.now().replace(microsecond=0)

# --- TASK DEFINITIONS ---
tasks = {
    "Take Medication": current_time,
    "Have Breakfast": current_time + timedelta(seconds=TEST_INTERVAL),
    "Go for a walk": current_time + timedelta(seconds=2 * TEST_INTERVAL),
    "Have Lunch": current_time + timedelta(seconds=3 * TEST_INTERVAL),
    "Have Dinner": current_time + timedelta(seconds=4 * TEST_INTERVAL),
    "Go to Bed": current_time + timedelta(seconds=5 * TEST_INTERVAL),
}

# --- CREATE REMINDERS ---
reminders = []
for task_name, base_time in tasks.items():
    for i in range(REMINDER_COUNT):
        reminder_time = base_time + timedelta(seconds=i * REMINDER_INTERVAL)
        reminders.append((reminder_time, task_name))

reminders.sort()
completed_tasks = set()
input_queue = queue.Queue()


# --- BACKGROUND THREAD FOR USER INPUT ---
def wait_for_input():
    while True:
        input()
        input_queue.put("done")


threading.Thread(target=wait_for_input, daemon=True).start()

print("🔁 Reminder system started in TEST MODE.")
print("➡ Press ENTER when a task is completed to cancel future reminders.\n")

try:
    while reminders:
        now = datetime.now().replace(microsecond=0)
        due_reminders = [r for r in reminders if r[0] <= now and r[1] not in completed_tasks]

        if due_reminders:
            reminder_time, task = due_reminders[0]
            print(f"[{now.strftime('%H:%M:%S')}] 🔔 Reminder: {task} — Press ENTER to mark as done.")

            # Wait up to 10 seconds for user input (without blocking the loop)
            start_time = time.time()
            marked_done = False
            while time.time() - start_time < 10:
                if not input_queue.empty():
                    input_queue.get()
                    completed_tasks.add(task)
                    marked_done = True
                    print(f"✅ Task '{task}' marked as completed.\n")
                    break
                time.sleep(0.5)

            if not marked_done:
                print(f"⏰ No confirmation for '{task}'. Will remind again if scheduled.\n")

            # Remove this reminder
            reminders.remove((reminder_time, task))

            # Remove future reminders if task is done
            if task in completed_tasks:
                reminders = [r for r in reminders if r[1] != task]

        time.sleep(1)

except KeyboardInterrupt:
    print("\n🛑 Reminder system stopped.")