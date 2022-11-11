import folium
import webbrowser



map = folium.Map(location=[49.934869269, 36.3792021920], zoom_start=20)#, tiles="Stamen Terrain")

folium.Marker(location=[49.93486926903723, 36.379202192066515], popup="Me", icon=folium.Icon(color='gray')).add_to(map)

map.save("map1.html")
webbrowser.open ('map1.html', new=2)
