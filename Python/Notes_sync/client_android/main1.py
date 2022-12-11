from kivy.app import App
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

import Variables

Config.set("graphics", "resizable", "0")
Config.set("graphics", "width", "350")
Config.set("graphics", "height", "500")

saveInput = ""


class ClientApp(App):

    # def start(self):

    # self.sam_primer.text = []

    # def calculate(self, symbol):
    #
    #     global saveInput
    #     if symbol.text is '<':
    #         saveInput = self.otvet_july.text = ""
    #
    #     elif symbol.text is not 'Answer':
    #         self.otvet_july.text += symbol.text
    #         saveInput += symbol.text
    #     else:
    #         try:
    #             if str(Variables.answer) == str(saveInput):
    #                 Variables.pravilno += 1
    #                 self.textField1.text = str(Variables.pravilno_str) + str(Variables.pravilno)
    #                 self.otvet_july.text = ""
    #                 self.sam_primer.text = ""
    #                 Variables.answer = ""
    #                 Variables.answer_July = ""
    #                 Variables.value_a = 0
    #                 Variables.value_b = 0
    #                 Variables.value_c = 0
    #                 Variables.znak1 = ""
    #                 Variables.znak2 = ""
    #                 saveInput = ""
    #                 self.start()
    #             else:
    #                 Variables.nepravilno += 1
    #                 self.textField2.text = str(Variables.nepravilno_str) + str(Variables.nepravilno)
    #                 print(Variables.nepravilno)
    #                 self.otvet_july.text = ""
    #                 self.sam_primer.text = ""
    #                 Variables.answer = ""
    #                 Variables.answer_July = ""
    #                 Variables.value_a = 0
    #                 Variables.value_b = 0
    #                 Variables.value_c = 0
    #                 Variables.znak1 = ""
    #                 Variables.znak2 = ""
    #                 saveInput = ""
    #                 self.start()
    # saveInput = self.otvet_july.text = str(eval(saveInput))
    # except:
    #     saveInput = self.otvet_july.text = ""

    def build(self):
        root = BoxLayout(orientation="vertical", padding=1)


        self.input_text = TextInput(
            text="", readonly=False, font_size=60,
            size_hint=[.15, .33], background_color=[1, 1, 1, .8], focus=True, halign="center")
        self.sent_button = Button(text='Sent', halign="center", size_hint_y=.11)
        self.output_text = TextInput(text='', size_hint=[.5, .5], readonly=True, font_size=30, halign="center")
        
        one_window = GridLayout(cols=1, size_hint=[1, .25], padding=[0, 0, 0, 0], size_hint_y=.11)
        one_window.add_widget(self.input_text)
        one_window.add_widget(self.sent_button)
        one_window.add_widget(self.output_text)

        root.add_widget(one_window)

        return root

    # def add_widget(self):
    #     self.start()
    #     pass


if __name__ == "__main__":
    ClientApp().run()
