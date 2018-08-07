#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Convert Copy to Read
#
#----------------------------------------------------------------------------------------------------------

rootFirst = nuke.root().firstFrame()
rootLast = nuke.root().lastFrame()

# get selected nodes
nodes = nuke.selectedNodes()

# check if it is writes only
writes = [n for n in nodes if n.Class() == "Write"]


#iterate trough use definition to create read nodes
for w in writes:
    read = nuke.nodes.Read(file=w['file'].value(), name=w['name'].value()+"_Read1")

    read['first'].setValue(int(rootFirst if w['use_limit'].value() is False else w['first'].value()))
    read['last'].setValue(int(rootLast if w['use_limit'].value() is False else w['last'].value()))
    read['colorspace'].setValue(w['colorspace'].value())
    read['xpos'].setValue(w.xpos()-100)
    read['ypos'].setValue(w.ypos())


    