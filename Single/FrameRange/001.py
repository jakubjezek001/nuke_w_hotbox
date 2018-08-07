#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Get frame range from viewer
#
#----------------------------------------------------------------------------------------------------------

for i in nuke.selectedNode().dependent():
	if i.Class() == 'Viewer':
		frame_range =  i.knob('frame_range').value().split("-")
		nuke.selectedNode().knob('first_frame').setValue(float(frame_range[0]))
		nuke.selectedNode().knob('last_frame').setValue(float(frame_range[1]))
