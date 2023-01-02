from textual.app import App, ComposeResult
from textual.widgets import Header


class StopwatchApp(App):
    def compose(self) -> ComposeResult:
        yield Header()


if __name__ == "__main__":
    StopwatchApp().run()
