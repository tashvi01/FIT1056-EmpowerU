import tkinter as tk

class ProgressTracker:
    def __init__(self, master, student):
        self.master = master
        self.student = student

        # Initialize the progress label
        self.progress_label = tk.Label(master, text=self.get_progress_text(), bg="lightblue", font=("Arial", 14))
        self.progress_label.grid(row=0, column=0, padx=10, pady=10)

    def increment_progress(self):
        """Increment the student's progress and update the display."""
        self.student.increment_progress()
        self.update_label()

    def update_label(self):
        """Update the progress label with the current progress."""
        self.progress_label.config(text=self.get_progress_text())

    def get_progress_text(self):
        """Return the text to be displayed for the current progress."""
        completed, total = self.student.get_progress()
        return f"Quizzes Completed: {completed}/{total}"
