from textual.app import App, ComposeResult
from textual.widgets import Button, Label
from textual.binding import Binding


class CssTester(App[None]):
    CSS_PATH = "test.css"

    ###
    BINDINGS = [Binding("ctrl+z", "suspend_process")]

    def compose(self) -> ComposeResult:
        yield Label("Do you love textual?", id="question")
        yield Button("Yes", id="yes", variant="primary")
        yield Button("No", id="no", variant="error")


    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.exit(message=event.button.id)


if __name__ == "__main__":
    app = CssTester()
    app.run()
