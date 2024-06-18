import pytui
drawer = pytui.init()
drawer.addElemement(pytui.label(content="hello world"))
while True:
    drawer.draw()