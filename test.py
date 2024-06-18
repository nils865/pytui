import pytui

drawer = pytui.init()
drawer.addElemement(pytui.label(content="hello world"))
drawer.addElemement(pytui.slider())

while True:
    drawer.draw()
