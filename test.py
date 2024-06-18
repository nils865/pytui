import pytui

drawer = pytui.init()
drawer.addElemement(pytui.label(content="hello world"))
drawer.addElemement(pytui.slider(value=12,max=60))

while True:
    drawer.draw()
