import sys
from typing import Callable
from rich.progress import Progress, BarColumn, TextColumn, TimeElapsedColumn, TimeRemainingColumn

class ProgressBar:

    def __init__(self, text: str, count: int, transient: bool = True, callback: Callable[[int, int], None] | None = None):
        self.text = text
        self.count = count
        self.transient = transient
        self.callback = callback
        if self.text:
            self.progress = Progress(
                TextColumn("[progress.description]{task.description}"),
                BarColumn(bar_width = None),
                "[progress.percentage]{task.percentage:>3.0f}%",
                TimeElapsedColumn(),
                TimeRemainingColumn(),
                transient = transient,
            )
            self.task_id = self.progress.add_task(text, total = count)

    def __enter__(self):
        if self.text:
            self.progress.start()
            sys.stdout.flush()
        self.run_callback(0)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.text:
            if not self.transient:
                self.progress.update(self.task_id, completed = self.count)
            self.progress.stop()
        self.run_callback(self.count)

    def update(self, value: int):
        if self.text:
            self.progress.update(self.task_id, completed = value)
            sys.stdout.flush()
        self.run_callback(value)

    def run_callback(self, value: int):
        if callback != None:
            callback(value, self.count)

    def new_task(self, text: str, count: int):
        self.text = text
        self.count = count
        if self.text:
            self.progress.update(self.task_id, description = self.text, total = count, progress = 0)


