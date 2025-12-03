from textual.app import App, ComposeResult
from textual.widgets import Button, Header, Label, Static
from textual.containers import Container, Vertical, Horizontal
from textual import on

# This must be imported for us refer the Key pressed event. `event.key`
from textual.events import Key




class MyApp(App[None]):
    CSS_PATH="style.css"
    TITLE="Infoblox TUI"
    SUB_TITLE="The right way to do system administration"


    def compose(self) -> ComposeResult:
        yield Header()

        yield Container(
                Static("One", classes="box"),
                Static("Two", classes="box"),
                Static("Three", classes="box"),

                id="c_main",
        )

        # Uses `with` for easier code readibility 
        with Container(id="c_sec"):
            yield Static("Four", classes="box")
            yield Static("Five", classes="box")
            
            with Horizontal():
                yield Static("Six", classes="box")

                with Vertical():
                    with Horizontal():
                        yield Static("Seven", classes="box")
                        yield Static("Eight", classes="box")
                    with Horizontal():
                        yield Static("Nine", classes="box")
                        yield Static("Ten", classes="box")

                yield Static("Eleven", classes="box")





    # Tells Textualize to listen to event, `Key` if "on" do:
    #       Tells App to pass event to and run, when given event is triggered
    @on(Key) 
   
    #
    # Whenever an event is triggered, it gets CLASSified by a type
    #       for example a key press event: event.key
    # `class Key(key, character)`
    #
    # Then we can specify a function to run if an event.key is triggered.
    # We pass the "@on" Declorator Factory the event Class type.
    #
    # Our handler function will be passed the Event Class
    #   (created by the event which was triggered, in our case Key)
    #

    def change_title(self, event: Key):     # Event Handler method
        self.sub_title = f"You pressed the '{event.key}' Key"



    

if __name__ == "__main__":
    app = MyApp()
    app.run()

