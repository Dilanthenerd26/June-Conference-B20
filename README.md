# June-Conference-B20

Reminder Scheduler

A simple Python-based reminder system that supports multiple scheduled tasks with up to 3 reminders, spaced evenly. Designed for testing and educational use.
 Features:
Define multiple tasks with individual start times
Each task receives 3 reminders, spaced 5 seconds apart (in test mode)
User can press ENTER to mark a task as complete
All future reminders for completed tasks are cancelled
Non-blocking input using threading ensures smooth reminder delivery

How It Works:
Tasks are created with start times staggered by a few seconds.
Each task gets 3 reminders (default: 5 seconds apart).
When a reminder is triggered, you're prompted to press ENTER.
If you do, the task is marked complete and all future reminders are cancelled.
If you don’t, the next reminder still comes later.

Running the Script:
Prerequisites
Python 3.x

To Run:
Click the "Run code" Button

The link to our slides: https://www.canva.com/design/DAGqBsHNzOw/Tbjp1kvt_VVFXzlsOsPQCQ/edit?utm_content=DAGqBsHNzOw&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

