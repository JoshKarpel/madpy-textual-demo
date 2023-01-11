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


class StopwatchApp(App):
    def compose(self) -> ComposeResult:
        yield Header()

        yield Container(Stopwatch(), Stopwatch(), Stopwatch())


if __name__ == "__main__":
    StopwatchApp().run()
