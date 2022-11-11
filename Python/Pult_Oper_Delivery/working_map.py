from tkinter import *
import tkintermapview
address = "Франтишека Крала, 65, Харьков, Украина"


window = Tk()
window.title("Test_Map")
window.geometry("800x800+300+50")
map_widget = tkintermapview.TkinterMapView(window, width=800, height=800, corner_radius=0)
map_widget.place(x=0, y=0)
marker1 = map_widget.set_address(address, text=address, marker=True)
map_widget.set_zoom(16)
# map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=18)

# marker_1.set_text("Пушкинская, 7, Харьков, Украина")








window.mainloop()