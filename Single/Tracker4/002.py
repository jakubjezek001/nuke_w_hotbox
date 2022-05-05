#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Toggle Scale
#
#----------------------------------------------------------------------------------------------------------

#6 = translate, 7 = rotate, 8 = scale
transformMode = 8

for i in nuke.selectedNodes():
    value = 1 - i.knob('tracks').value(transformMode)

    #count tracks
    tracks = 0
    while i.knob('tracks').isAnimated(31 * tracks + 2):
        tracks += 1

    for track in range(tracks):
        i.knob('tracks').setValue(value, 31 * track + transformMode)