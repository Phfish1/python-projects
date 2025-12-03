from time import monotonic

from textual.app import App, ComposeResult
from textual.containers import HorizontalGroup, VerticalScroll
from textual.reactive import reactive
from textual.widgets import Button, Digits, Footer, Header


# Defines a custom widget
class TimeDisplay(Digits):
    """Do something"""

    start_time = reactive(monotonic)
    time = reactive(0.0)
    total = reactive(0.0)

    def on_mount(self) -> None:
        self.update_timer = self.set_interval(1 / 60, self.update_time, pause=True)


    def update_time(self) -> None:
        self.time = self.total + (monotonic() - self.start_time)


    """ A Special function that runs, each time the reactive() variable 'time' changes"""
    def watch_time(self) -> None:
        minutes, seconds = divmod(self.time, 60)
        hours, minutes = divmod(minutes, 60)
        self.update(f"{hours:02.0f}:{minutes:02.0f}:{seconds:05.2f}")

    
    def start(self) -> None:
        self.start_time = monotonic()
        self.update_timer.resume()

    
    def stop(self) -> None:
        self.update_timer.pause()
        self.total += monotonic() - self.start_time
        self.time = self.total

    def reset(self) -> None:
        self.total = 0
        self.time = 0


# Custom container widget to contain widgets apart of a StopWatch widget
class Stopwatch(HorizontalGroup):

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        time_display = self.query_one(TimeDisplay)
        
        if button_id == "b-start":
            time_display.start()
            self.add_class("started")
        elif button_id == "b-stop":
            time_display.stop()
            self.remove_class("started")
        elif button_id == "b-reset":
            time_display.reset()


    def compose(self) -> ComposeResult:
        yield Button("Start", id="b-start", variant="success")
        yield Button("Stop", id="b-stop", variant="error")
        yield Button("Reset", id="b-reset")
        yield TimeDisplay("00:00:00.00")


class StopwatchApp(App):
    CSS_PATH = "stopwatch.css"

    """ Binds KEYs to an action, followed by a description"""
    BINDINGS = [
        ("d", "toggle_dark", "Toogle dark mode"),
        ("a", "add_stopwatch", "Add"),
        ("r", "remove_stopwatch", "Remove")
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        
        yield VerticalScroll(Stopwatch(), Stopwatch(), Stopwatch(), id="timers")


    def action_add_stopwatch(self) -> None:
        new_stopwatch = Stopwatch()
        timers_container = self.query_one("#timers")

        timers_container.mount(new_stopwatch)
        new_stopwatch.scroll_visible()

    def action_remove_stopwatch(self) -> None:
        timers = self.query("Stopwatch")
        if timers:
            timers.last().remove()


    """ an "action_" method named toogle_dark"""
    def action_toggle_dark(self):
        self.theme = (
                "textual-dark" if self.theme == "textual-light" else "textual-light"
        )


""" the __name__ will change to equal '__main__' if this file is directly run"""
if __name__ == "__main__":
    app = StopwatchApp()
    app.run()
