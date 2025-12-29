from textual.app import App, ComposeResult
from textual.widgets import Static, Button, Header, RichLog
from textual.containers import Container

from textual import on
from textual.events import Key


class GridApp(App[None]):
    CSS_PATH = "style.css"
    BINDINGS = [
        ("h", "display_help", "Display Help Tips"),
    ]
    
    
    def compose(self) -> ComposeResult:
        self.searching = False

        with Container(id="c_start"):
            yield Static(f"Box: 1", classes="box", id="left_box")
            yield Static(f"Box: 2", classes="box", id="main_box")
            yield Static(f"Box: 3", classes="box", id="right_box")

            #yield Static(f"Box: 4", classes="box")
            #yield Static(f"Box: 5", classes="box")
        
        with Container(id="status_box"):
            yield Static(f"Status Box: 1")
            yield Static(f"Type / to search...", id="search_bar")
            yield Static(f"Status Box: 3")

    
    # Togles Help menu
    def action_display_help(self) -> None:
        if self.query("#help_menu"):
            self.query("#help_menu").remove()
            return

        helper_container = Container(
            Static(f"I will help you!", classes="help_text"),
            Static(f"I will help you!", classes="help_text"),

            id="help_menu",
        )

        helper_container.border_title = "Help Menu "
        self.mount(helper_container)

    


if __name__ == "__main__":
    app = GridApp()
    app.run()
