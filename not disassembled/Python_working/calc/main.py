from kivy.app import App
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

import Variables
from logic import change_primer

Config.set("graphics", "resizable", "0")
Config.set("graphics", "width", "350")
Config.set("graphics", "height", "500")

saveInput = ""


class CalculatorApp(App):

    def start(self):
        value_a, value_b, value_c, ri1, ri2, ri3 = change_primer()
        Variables.value_a = value_a
        Variables.value_b = value_b
        Variables.value_c = value_c
        Variables.znak1 = ri2
        Variables.znak2 = ri3
        Variables.answer = ri1
        self.sam_primer.text = str(value_a) + str(ri2) + str(value_b) + str(ri3) + str(value_c)

    def calculate(self, symbol):

        global saveInput
        if symbol.text is '<':
            saveInput = self.otvet_july.text = ""

        elif symbol.text is not 'Answer':
            self.otvet_july.text += symbol.text
            saveInput += symbol.text
        else:
            try:
                if str(Variables.answer) == str(saveInput):
                    Variables.pravilno += 1
                    self.textField1.text = str(Variables.pravilno_str) + str(Variables.pravilno)
                    self.otvet_july.text = ""
                    self.sam_primer.text = ""
                    Variables.answer = ""
                    Variables.answer_July = ""
                    Variables.value_a = 0
                    Variables.value_b = 0
                    Variables.value_c = 0
                    Variables.znak1 = ""
                    Variables.znak2 = ""
                    saveInput = ""
                    self.start()
                else:
                    Variables.nepravilno += 1
                    self.textField2.text = str(Variables.nepravilno_str) + str(Variables.nepravilno)
                    print(Variables.nepravilno)
                    self.otvet_july.text = ""
                    self.sam_primer.text = ""
                    Variables.answer = ""
                    Variables.answer_July = ""
                    Variables.value_a = 0
                    Variables.value_b = 0
                    Variables.value_c = 0
                    Variables.znak1 = ""
                    Variables.znak2 = ""
                    saveInput = ""
                    self.start()
                # saveInput = self.otvet_july.text = str(eval(saveInput))
            except:
                saveInput = self.otvet_july.text = ""

    def build(self):
        root = BoxLayout(orientation="vertical", padding=1)

        self.sam_primer = TextInput(
            text="one field", readonly=True, font_size=60,
            size_hint=[.70, .33], background_color=[1, 1, 1, .8], halign="center")

        self.ravno = TextInput(
            text="=", readonly=True, font_size=60,
            size_hint=[.05, .33], background_color=[1, 1, 1, .8], halign="center")

        self.otvet_july = TextInput(
            text="", readonly=True, font_size=60,
            size_hint=[.15, .33], background_color=[1, 1, 1, .8], focus=True, halign="center")

        one_window = GridLayout(cols=3, size_hint=[1, .25], padding=[0, 0, 0, 0], size_hint_y=.11)

        one_window.add_widget(self.sam_primer)
        one_window.add_widget(self.ravno)
        one_window.add_widget(self.otvet_july)

        root.add_widget(one_window)

        self.textField1 = TextInput(text=Variables.pravilno_str + str(Variables.pravilno), size_hint=[.5, .5],
                                    readonly=True, font_size=30,
                                    halign="center")
        self.textField2 = TextInput(text=Variables.nepravilno_str + str(Variables.nepravilno), size_hint=[.5, .5],
                                    readonly=True,
                                    font_size=30, halign="center")

        allTextFields = GridLayout(cols=2, padding=[0, 0, 0, 0], size_hint_y=.13)

        allTextFields.add_widget(self.textField1)
        allTextFields.add_widget(self.textField2)

        root.add_widget(allTextFields)

        allButtons = GridLayout(cols=3, size_hint=[1, .40])

        allButtons.add_widget(Button(text='7', font_size=30, on_press=self.calculate))
        allButtons.add_widget(Button(text='8', font_size=30, on_press=self.calculate))
        allButtons.add_widget(Button(text='9', font_size=30, on_press=self.calculate))

        allButtons.add_widget(Button(text='4', font_size=30, on_press=self.calculate))
        allButtons.add_widget(Button(text='5', font_size=30, on_press=self.calculate))
        allButtons.add_widget(Button(text='6', font_size=30, on_press=self.calculate))

        allButtons.add_widget(Button(text='1', font_size=30, on_press=self.calculate))
        allButtons.add_widget(Button(text='2', font_size=30, on_press=self.calculate))
        allButtons.add_widget(Button(text='3', font_size=30, on_press=self.calculate))

        allButtons.add_widget(Button(text='0', font_size=30, on_press=self.calculate))
        allButtons.add_widget(Button(text="<", font_size=30, on_press=self.calculate))
        allButtons.add_widget(Button(text="Answer", font_size=30, on_press=self.calculate))

        root.add_widget(allButtons)
        self.start()
        return root

    # def add_widget(self):
    #     self.start()
    #     pass


if __name__ == "__main__":
    CalculatorApp().run()
