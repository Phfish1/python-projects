from textual.app import App, ComposeResult
from textual.widgets import Static, Button
from textual.containers import Container


class GridApp(App[None]):
    CSS_PATH = "style.css"
    
    
    def compose(self) -> ComposeResult:

        with Container(id="c_start"):
            yield Static(f"Box: 1", classes="box", id="left_box")
            yield Static(f"Box: 2", classes="box", id="main_box")
            yield Static(f"Box: 3", classes="box", id="right_box")

            #yield Static(f"Box: 4", classes="box")
            #yield Static(f"Box: 5", classes="box")

        yield Static(f"Status Box: 6", classes="box", id="status_box")


if __name__ == "__main__":
    app = GridApp()
    app.run()
