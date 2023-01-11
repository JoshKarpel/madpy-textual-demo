from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widget import Widget
from textual.widgets import Button, Header, Static


class Stopwatch(Widget):
    def compose(self) -> ComposeResult:
        yield Button("Start", id="start")
        yield Button("Stop", id="stop")
        yield Button("Reset", id="reset")

        yield Static("00.00", id="time")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        match event.button.id:
            case "start":
                self.add_class("running")
            case "stop":
                self.remove_class("running")
            case "reset":
                self.remove_class("running")


class StopwatchApp(App):
    CSS = """\
    Screen {
        background: rgb(0,0,0);
    }

    Stopwatch {
        layout: horizontal;
        background: rgb(40,40,40);
        height: 5;
        margin: 1;
        min-width: 50;
        padding: 1;
    }

    Static#time {
        content-align: center middle;
        text-opacity: 60%;
        height: 3;
    }

    Button {
        width: 16;
    }

    Button#start {
        background: #4CAF50;
        dock: left;
    }

    Button#stop {
        background: #FF5722;
        dock: left;
        display: none;
    }

    Button#reset {
        background: #FFCA28;
        dock: right;
    }

    .running #start {
        display: none;
    }

    .running #stop {
        display: block;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()

        yield Container(Stopwatch(), Stopwatch(), Stopwatch())


if __name__ == "__main__":
    StopwatchApp().run()
