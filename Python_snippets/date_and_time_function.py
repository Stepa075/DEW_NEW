def update_time():
    # change text on Label
    lbl_time['text'] = time.strftime('Current date: %Y-%m-%d Current time: %H:%M:%S')

    # run `update_time` again after 1000ms (1s)
    root.after(1000, update_time)  # function name without ()