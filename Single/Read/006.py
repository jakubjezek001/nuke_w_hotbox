#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Overscan
#
#----------------------------------------------------------------------------------------------------------

def start():

    import nuke
    import nukescripts

    class SetFirstFramePanel(nukescripts.PythonPanel):
        def __init__(self):
            nukescripts.PythonPanel.__init__(self, 'Merge Transforms')

            # CREATE KNOBS
            self.first = nuke.Int_Knob('first', 'First Frame')
            self.first.setValue(int(nuke.root()['first_frame'].value()))

            # ADD KNOBS
            self.addKnob(self.first)

    # open panel and get value for first frame
    p = SetFirstFramePanel()
    if p.showModalDialog():
        first = p.first.value()

    # set first frame into nodes
    nodes = nuke.selectedNodes()
    for i in nodes:
        if i.Class() == "Read":
            i.knob('frame_mode').setValue("start at")
            i.knob('frame').setValue(str(first))
        else:
            nuke.message("It has to be Read node")
            return 0


for _ in nuke.selectedNodes():
    start()
    break
