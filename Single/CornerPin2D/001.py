#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Anim point to Matrix 4x4
#
#----------------------------------------------------------------------------------------------------------

#animated_cornerpin_to_matrix" is a helper script to convert animation data from a cornerpin to a 4x4 transform matrix.
#This Python Script creates a CornerPin node in Nuke using the
#transform_matrix knob to store animation data from another CornerPin node in Nuke. 
#This will help to distribute animated CornerPin data for example
#from Mocha in Nuke to all sorts of nodes like 'Gridwarp', 'SplineWarp',
#'Paint and Roto' nodes.
#
#Egbert Reichel 2015

import nuke
import nukescripts

def animatedCP2MTX():
    
    try:
        input = nuke.selectedNode()
    
        #----------------------------------------------------------------------------------------------------------
 
        if  input.Class() == 'CornerPin2D':
          
            node_in = input.input(0)
            
            cp = nuke.nodes.CornerPin2D( name = 'CornerPin_to_Matrix')
            
            xpos = input['xpos'].value()
            ypos = input['ypos'].value()
            
            cp_width = cp.screenWidth()
            cp_height = cp.screenHeight()
            
            cp.setXYpos(int(xpos) + int(cp_width) + 25 , int(ypos))
            cp.knob('extra matrix').setValue(True)
            cp.setInput(0, node_in)
            nuke.show(cp)
            cp_em = cp.knob('transform_matrix')
            
            
             #---------------------------------------------------------------------------------------
            
            # conversion cp_to_mtx
            
            def getAnimatedCPasMTX(cornerpin, iterator):
                
                i = iterator
                cp =  cornerpin
                
                pmTo = nuke.math.Matrix4()
                pmFrom = nuke.math.Matrix4()
                    
                imageWidth = float(cp.width())
                imageHeight = float(cp.height())
                    
                to1x = cp['to1'].getValueAt(i)[0]
                to1y = cp['to1'].getValueAt(i)[1]
                to2x = cp['to2'].getValueAt(i)[0]
                to2y = cp['to2'].getValueAt(i)[1]
                to3x = cp['to3'].getValueAt(i)[0]
                to3y = cp['to3'].getValueAt(i)[1]
                to4x = cp['to4'].getValueAt(i)[0]
                to4y = cp['to4'].getValueAt(i)[1]
                    
                from1x = cp['from1'].getValueAt(i)[0]
                from1y = cp['from1'].getValueAt(i)[1]
                from2x = cp['from2'].getValueAt(i)[0]
                from2y = cp['from2'].getValueAt(i)[1]
                from3x = cp['from3'].getValueAt(i)[0]
                from3y = cp['from3'].getValueAt(i)[1]
                from4x = cp['from4'].getValueAt(i)[0]
                from4y = cp['from4'].getValueAt(i)[1]
                    
                    
                pmTo.mapUnitSquareToQuad(to1x,to1y,to2x,to2y,to3x,to3y,to4x,to4y)
                pmFrom.mapUnitSquareToQuad(from1x,from1y,from2x,from2y,from3x,from3y,from4x,from4y)
                    
                mtx = pmTo*pmFrom.inverse()    
                mtx.transpose()
                    
                return mtx
                
            #---------------------------------------------------------------------------------------
            
 
 
            #--------------------------------''' Define Frame Range'''---------------------------------    
    
            frames = nuke.getFramesAndViews('get FrameRange', '%s-%s' % (nuke.root().firstFrame(), nuke.root().lastFrame()))
            frame_range = nuke.FrameRange( frames[0] ) 
              
            #---------------------------------------------------------------------------------------  
                    
            for i in frame_range:
 

                mtx = getAnimatedCPasMTX(input, i)
                              
                #------------------------------------------------------------------------------
                #apply values
                
                cp_em.setAnimated()
                for j in range(16):
                    cp_em.setValueAt(mtx[j], i, j )
                                                       
                                   
                #-----------------------------------------------------------------------------------------------    
            
 
        
        else:
    
            nuke.message('please select a CornerPin node')
     
    except:
 
         nuke.message('please select a CornerPin node')
     


for _ in nuke.selectedNodes():
    animatedCP2MTX()