from textual.app import App, ComposeResult
from textual.widgets import Static, Button
from textual.containers import Container

from textual import on


class GridApp(App[None]):
    CSS_PATH = "style.css"
    

    def compose(self) -> ComposeResult:
        self.box_n = 0
        self.box_v = [
            "One",
            "Two",
            "Three",
            "Four",
            "Five",
            "Six",
            "Seven",
            "Eight",
            "Nine",
        ]

        with Container(id="c_buttons"):
            yield Button("Add Row", id="row_add")
            yield Button("Spawn Static", id="spawner")
            yield Button("Add Column", id="column_add")

        with Container(id="c_start"):
            for i in range(0, self.box_n):
                yield Static(self.box_v[i], classes="box")


    @on(Button.Pressed, "#spawner")
    def spawn_static(self, event: Button.Pressed) -> None:
        container = self.query_one("#c_start")
        
        if self.box_n < len(self.box_v):
            value = self.box_v[self.box_n]
        else:
            value = "other"
        
        container.mount(
                Static(value, classes="box")
        )

        
        self.box_n += 1

    
    @on(Button.Pressed, "#row_add")
    def add_row(self) -> None:
        container = self.query_one("#c_start")
        container.styles.grid_size_rows += 1
    
    @on(Button.Pressed, "#column_add")
    def add_column(self) -> None:
        container = self.query_one("#c_start")
        container.styles.grid_size_columns += 1


if __name__ == "__main__":
    app = GridApp()
    app.run()

