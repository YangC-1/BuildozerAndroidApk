# This is a sample Python script.

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class MainApp(App):
    def build(self):
        main_layout = BoxLayout(orientation="vertical")
        self.solution = TextInput(
            multiline=False, readonly=True, halign="center", font_size=25, font_name='DENG.ttf'
        )
        main_layout.add_widget(self.solution)
        buttons = ["choose", "one", "u", "like"]
        for label in buttons:
            button = Button(
                text=label,
                pos_hint={"center_x": 0.5, "center_y": 0.5},
            )
            button.bind(on_press=self.on_button_press)
            main_layout.add_widget(button)

        return main_layout

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        self.solution.text = "WNH 你大爷 麻溜来参加老子的婚礼！"


if __name__ == "__main__":
    app = MainApp()
    app.run()
