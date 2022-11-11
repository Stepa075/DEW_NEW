# Чтобы запустить одно окно root из другого окна, нужно импортировать файл с GUI локально в функции
# с вызовом второго root! Тогда целевое окно не будет запускаться при старте первого GUI.
def run_anyway():
    import Han_PCN_copy.main_New_GUI
    Han_PCN_copy.main_New_GUI.root.mainloop()