import os
import pickle

import requests
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

    def load_settings(self):
        with open("settings.txt", "r", encoding="UTF8") as setings:
            f = setings.read()
            lines = f.split(';')
            print(lines[0])
            Variables.ip = lines[0]

    def on_start(self):
        if os.path.exists('data.pickle'):
            with open('data.pickle', 'rb') as f:  # Выгружаем данные из файла пикли
                try:
                    data_new = pickle.load(f)
                except:
                    data_new = []
                    pass
            Variables.list_of_saved_data = data_new
            entry.delete(1.0, END)
            for element in Variables.list_of_saved_data:
                entry.insert(1.0, element + '\n')
            print(Variables.list_of_saved_data)
        else:
            with open('data.pickle', "w"):
                pass


    def general_title_state(self):
        if Variables.code_of_response_server == 200:
            # Variables.root_title = "My notes sync LAN (connected)"
            # root.title(Variables.root_title)
            val = list((entry1.get(1.0, END)).split())
            # val.reverse()
            print("value = " + str(val))
            if Variables.list_of_get_data != val:
                write_server_data_to_entry()

        else:
            Variables.root_title = "My notes sync LAN (no connect)"
            # root.title(Variables.root_title)
            pass
        pass
        # root.after(2000, general_title_state)

    def write_server_data_to_entry(self):
        b = Variables.list_of_get_data
        self.output_text.text.delete()
        for element in b:
            self.output_text.text.insert(1.0, element + '\n')

    def write_local_data(self):
        val = list((entry.get(1.0, END)).split())
        val.reverse()
        Variables.list_of_saved_data = val
        with open('data.pickle', "wb") as f:
            pickle.dump(Variables.list_of_saved_data, f)
        root.after(2000, write_local_data)

    def set_data(self):
        try:
            dict = {}
            lis = list((entry.get(1.0, END)).split('\n'))
            if lis[-1] == '\n' or lis[-1] == '':
                del lis[-1]
            for index, val in enumerate(lis):
                dict[index] = val
            print(dict)
            r = requests.get("http://127.0.0.1:5000/data_json_set", json=dict)
            if r.status_code == 200:
                print("set_data " + str(lis))
        except:
            print("EXcept of set data!!!")
            pass

    # def get_clipboard_text(event):
    #     from tkinter import Tk
    #     root = Tk()
    #     root.withdraw()
    #     s = root.clipboard_get()
    #     entry.insert(1.0, s)

    # def view_my_notes(event):
    #     t = Toplevel()
    #     t.wm_title("My notes")
    #     l = Text(t, font=("Arial Bold", 12))
    #     l.pack(side="top", fill="both", expand=True, padx=5, pady=5)
    #     aaa = entry2.get(1.0, END)
    #     l.insert(1.0, aaa)

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
        # Clock.schedule_interval(lambda dt: self.pr(), 1)
        return root

    # def add_widget(self):
    #     self.start()
    #     pass


if __name__ == "__main__":
    ClientApp().run()
