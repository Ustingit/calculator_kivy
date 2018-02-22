from kivy.app import App
from kivy.uix.button import Button

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

from kivy.config import Config

Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '400')


class BoxApp(App):

    def update_label(self):
        self.lbl.text = self.formula

    def add_number(self, instance):
        if self.formula == "0":
            self.formula = ""
        self.formula += str(instance.text)
        self.update_label()

    def add_operation(self, instance):
        self.formula += str(instance.text)
        self.update_label()

    def calculate(self, instance):
        self.lbl.text = str(eval(self.lbl.text))
        self.formula = "0"

    def clear(self, instance):
        self.formula = "0"
        self.update_label()

    def undo(self, instance):
        self.formula = self.formula[:-1]
        self.update_label()

    def build(self):
        self.formula = "0"
        bl = BoxLayout(orientation='vertical', padding=25)
        self.lbl = Label(text="0",
                    font_size=40,
                    halign='right',
                    size_hint=[1, 0.4],
                    text_size=[300 - 50, 400 * .4 - 50],
                    valign='center')
        bl.add_widget(self.lbl)
        gl = GridLayout(spacing=1,
                        cols=4)

        gl.add_widget(Button(text="9", on_press=self.add_number))
        gl.add_widget(Button(text="8", on_press=self.add_number))
        gl.add_widget(Button(text="7", on_press=self.add_number))
        gl.add_widget(Button(text="/", on_press=self.add_operation))

        gl.add_widget(Button(text="6", on_press=self.add_number))
        gl.add_widget(Button(text="5", on_press=self.add_number))
        gl.add_widget(Button(text="4", on_press=self.add_number))
        gl.add_widget(Button(text="*", on_press=self.add_operation))

        gl.add_widget(Button(text="3", on_press=self.add_number))
        gl.add_widget(Button(text="2", on_press=self.add_number))
        gl.add_widget(Button(text="1", on_press=self.add_number))
        gl.add_widget(Button(text="-", on_press=self.add_operation))

        gl.add_widget(Button(text="0", on_press=self.add_number))
        gl.add_widget(Button(text=".", on_press=self.add_operation))
        gl.add_widget(Button(text="=", on_press=self.calculate))
        gl.add_widget(Button(text="+", on_press=self.add_operation))

        gl.add_widget(Button(text="(", on_press=self.add_operation))
        gl.add_widget(Button(text=")", on_press=self.add_operation))
        gl.add_widget(Button(text="<<", on_press=self.undo))
        gl.add_widget(Button(text="C", on_press=self.clear))

        bl.add_widget(gl)
        return bl


if __name__ == "__main__":
    BoxApp().run()
