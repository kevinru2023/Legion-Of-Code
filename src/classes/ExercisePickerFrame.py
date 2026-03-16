"""
C-06: ExercisePickerFrame
Auth: Nolan Flores
"""

import json
import tkinter as tk
import webbrowser
from tkinter import ttk

from models.Workout import Workout


class ExercisePickerFrame:
    def __init__(self, parent):
        with open("data/exercises.json") as f:
            self._exercises = json.load(f)

        self.frame = ttk.LabelFrame(parent, text="Select Exercise")
        self._listbox = tk.Listbox(self.frame, height=7, exportselection=False)
        for name in self._exercises:
            self._listbox.insert("end", name)
        self._listbox.pack(fill="both", expand=True, padx=5, pady=5)
        self._listbox.bind("<<ListboxSelect>>", self._on_select)

        self._btn = tk.Button(self.frame, text="", fg="#1155cc", bg="#efefef", state="disabled", relief="flat", cursor="hand2", font=("Helvetica", 9, "underline"))
        self._btn.pack(anchor="w", padx=5, pady=(0, 4))

    def _on_select(self, _):
        sel = self._listbox.curselection()
        if not sel:
            return
        url = self._exercises[self._listbox.get(sel[0])]["video_id"]
        self._btn.config(text="View Exercise Tutorial", state="normal", command=lambda: webbrowser.open(url))

    def get_workout(self) -> Workout | None:
        sel = self._listbox.curselection()
        if not sel:
            return None
        name = self._listbox.get(sel[0])
        ex = self._exercises[name]
        return Workout(
            name=name,
            reps=ex["reps"],
            sets=ex["sets"],
            rest_time=ex["rest_time"],
            video_id=ex["video_id"],
            muscle_group=ex["muscle_group"],
        )