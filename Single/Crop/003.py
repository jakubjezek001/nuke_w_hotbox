#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: To BoundingBox (Expression)
#
#----------------------------------------------------------------------------------------------------------

for i in nuke.selectedNodes():
    inputNode = i.input(0)
    for index, axis in enumerate(['x','y','r','t']):
        i.knob('box').setExpression(f'input.bbox.{axis}', index)