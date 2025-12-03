from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal
from textual.widgets import Static, Button, Header, Label


class CssTester(App):
    # Widgets can be modified using inline CSS or a file
    #   * Widgets can be selected using CSS Selectors! 

    #
    # Textual uses a kind of DOM model (Document Object Model)
    # Similar to HTML, but without Documents
    #

    # 
    # We create a Derived Class from App, `CssTester()` which initialiy creates a child
    # called `screen()`, this will contain all our widget within that Screen.
    #

    # Whatever we "yield" within the compose method goes under Screen()

    # Each Widget CAN have child widgets.
    #   This is the usual case with prebuilt widgets
    #   Or you can specify child widgets yourself
    #   Additionaly create custom widgets


    # This example uses inline CSS, you can also specify a CSS file: `CSS_PATH = '<path>'`
    #   A seperate CSS File is prefered, it allows LIVE EDITING ! (using the Textual devtools `textual run --dec <file.py>`
    CSS = """
    Header {            /* This is a Selector, specifying which Widget to apply rules to */
        dock: top;      /* Defines a CSS Rule, with the Rule-Name: `dock` and Rule-Value: `top` */
    }

    #c1_dialog {         /* Selector for our containor identified by its ID: `c_dialog` */
        height: 100%;
        margin: 4 8;
        background: $panel;
        border: tall $background;
        color: $text;
    }

    #c2_dialog {
        height: 100%;
        margin: 4 8;
        background: white;
        border: tall blue;
        color: gray;
    } 

    #c2_dialog Button {         /* Selects ALL the descendants of c2_dialog that are Buttons */
        width: 100%;
        height: auto;
        background: green;
    }

    #c2_dialog>* {
        background: red;        /* Uses the `>` selector to ONLY select direct children and the `*` selector to sellect ALL (all direct children) */
        width: 100%;
        height: auto;
    }

    #c2_dialog>Horizontal {
        dock: bottom;
    }
   
    Button {
        width: 1fr;
    }

    Button:hover {              /* a Pseudo selector, applying CSS to a in a specific state */
        background: blue;
    }


    .question {
        text-style: bold;
        height: 100%;
        content-align: center middle;
    }

    .buttons {
        width: 100%;
        height: auto;
        dock: bottom;
    }

    """


    #
    # If an Object/Widget has MULTIPLE selector being applied to it.
    #   Textual will use CSS specificty to decide which Rules to use.
    #
    #   A Selector can have multiple selectors it is decided by most:
    #       1. ID Selectors    Button {
    #       2. Most Class / Pseudo Class selectors
    #       3. If only Type selectors are specified, the Selector with the most Type Selectors wins
    #

    # self.QUESTION = "Do you like me?..."

    def compose(self) -> ComposeResult:

        yield Header()

        # Simple variable decleration (should honestly be global tho...), cannot be defined under the class unless using self.<var-name>
        QUESTION = "Do you like me?..."

        # Creates a Container that takes in any amount of child widgets `*children`
        #   Not all widgets takes in child widgets, eg: `Button()`

        # * Lines children Verticaly
        yield Container(
            Static(QUESTION, classes="question"),
            # * Lines children Horizontaly
            Horizontal( 
                # `*children` Child Widgets of Horizontal
                Button("Yes", variant="success"),
                Button("No", variant="error"),

                classes="buttons",
            ),

            id="c1_dialog",
                
        )

        yield Container(
            Static("Hello man :)", classes="question"),
            Label("Did you select me...!"),

            Horizontal(
                Button("Yeah <3"),
                Button("...No"),
            ),

            id="c2_dialog",
        )

if __name__ == "__main__":
    app = CssTester()
    app.run()


