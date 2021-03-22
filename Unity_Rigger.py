bl_info = {
    "name": "Unity Armature",
    "author": "Sc1pt3r",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "Scene Properties > Unity Rigger",
    "description": "Adds a Unity compatiable bone rig",
    "warning": "",
    "doc_url": "",
    "category": "scene",
}

import bpy

def main(context):
    #create the armature object 
    bpy.ops.object.armature_add(enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1)) #create the armature object
    bpy.ops.object.mode_set(mode='EDIT', toggle=False)
    obArm = bpy.context.active_object #get the armature object
    
    #Rename the first bone to root
    obArm.data.bones["Bone"].name = "root"
    
    ebs = obArm.data.edit_bones
    ebs["root"].use_deform = False
    
    #Create The Hips
    eb = ebs.new("hips")
    eb.head = (0, .4, 8.5) # if the head and tail are the same, the bone is deleted
    eb.tail = (0, .4, 10)    # upon returning to object mode
    obArm.data.edit_bones['hips'].parent = obArm.data.edit_bones['root']
    
    #Create The Spine
    eb = ebs.new("spine")
    eb.head = (0, .4, 10) # if the head and tail are the same, the bone is deleted
    eb.tail = (0, .4, 11)    # upon returning to object mode
    obArm.data.edit_bones['spine'].parent = obArm.data.edit_bones['hips']
    
    #Upper Right Leg 
    eb = ebs.new("upper_leg.R")
    eb.head = (-1.2, .4, 8.5) # if the head and tail are the same, the bone is deleted
    eb.tail = (-1.2, .3, 4)    # upon returning to object mode
    obArm.data.edit_bones['upper_leg.R'].parent = obArm.data.edit_bones['hips']
    
    #Upper Left Leg
    eb = ebs.new("upper_leg.L")
    eb.head = (1.2, .4, 8.5) # if the head and tail are the same, the bone is deleted
    eb.tail = (1.2, .3, 4)    # upon returning to object mode
    obArm.data.edit_bones['upper_leg.L'].parent = obArm.data.edit_bones['hips']
    
    #Lower Right Leg
    eb = ebs.new("lower_leg.R")
    eb.head = (-1.2, .3, 4) # if the head and tail are the same, the bone is deleted
    eb.tail = (-1.2, .5, .5)    # upon returning to object mode
    obArm.data.edit_bones['lower_leg.R'].parent = obArm.data.edit_bones['upper_leg.R']
    
    #Lower Left Leg
    eb = ebs.new("lower_leg.L")
    eb.head = (1.2, .3, 4) # if the head and tail are the same, the bone is deleted
    eb.tail = (1.2, .5, .5)    # upon returning to object mode
    obArm.data.edit_bones['lower_leg.L'].parent = obArm.data.edit_bones['upper_leg.L']
    
    #Lower Right Foot
    eb = ebs.new("foot.R")
    eb.head = (-1.2, .5, .5) # if the head and tail are the same, the bone is deleted
    eb.tail = (-1.2, -1, .1)    # upon returning to object mode
    obArm.data.edit_bones['foot.R'].parent = obArm.data.edit_bones['lower_leg.R']
    
    #Lower Left Foot
    eb = ebs.new("foot.L")
    eb.head = (1.2, .5, .5) # if the head and tail are the same, the bone is deleted
    eb.tail = (1.2, -1, .1)    # upon returning to object mode
    obArm.data.edit_bones['foot.L'].parent = obArm.data.edit_bones['lower_leg.L']
    
    #Create The Chest
    eb = ebs.new("chest")
    eb.head = (0, .4, 11) # if the head and tail are the same, the bone is deleted
    eb.tail = (0, .4, 12)    # upon returning to object mode
    obArm.data.edit_bones['chest'].parent = obArm.data.edit_bones['spine']
    
    #Create The Upper Chest
    eb = ebs.new("upper_chest")
    eb.head = (0, .4, 12) # if the head and tail are the same, the bone is deleted
    eb.tail = (0, .4, 14.5)    # upon returning to object mode
    obArm.data.edit_bones['upper_chest'].parent = obArm.data.edit_bones['chest']
    
    #Create The Neck
    eb = ebs.new("neck")
    eb.head = (0, .4, 14.5) # if the head and tail are the same, the bone is deleted
    eb.tail = (0, .2, 15.3)    # upon returning to object mode
    obArm.data.edit_bones['neck'].parent = obArm.data.edit_bones['upper_chest']
    
    #Create The head
    eb = ebs.new("head")
    eb.head = (0, .2, 15.3) # if the head and tail are the same, the bone is deleted
    eb.tail = (0, .2, 16.3)    # upon returning to object mode
    obArm.data.edit_bones['head'].parent = obArm.data.edit_bones['neck']
    
    #Create The Right Eye
    eb = ebs.new("eye.R")
    eb.head = (-.35, .2, 15.92) # if the head and tail are the same, the bone is deleted
    eb.tail = (-.35, -.5, 15.92)    # upon returning to object mode
    obArm.data.edit_bones['eye.R'].parent = obArm.data.edit_bones['head']
    
    #Create The Left Eye
    eb = ebs.new("eye.L")
    eb.head = (.35, .2, 15.92) # if the head and tail are the same, the bone is deleted
    eb.tail = (.35, -.5, 15.92)    # upon returning to object mode
    obArm.data.edit_bones['eye.L'].parent = obArm.data.edit_bones['head']
    
    #Create The Jaw
    eb = ebs.new("jaw")
    eb.head = (0, .2, 15.5) # if the head and tail are the same, the bone is deleted
    eb.tail = (0, -.5, 15)    # upon returning to object mode
    obArm.data.edit_bones['jaw'].parent = obArm.data.edit_bones['head']
    
    #Create The Right Shoulder
    eb = ebs.new("shoulder.R")
    eb.head = (-.2, -.1, 13.5) # if the head and tail are the same, the bone is deleted
    eb.tail = (-1.7, .6, 13.8)    # upon returning to object mode
    obArm.data.edit_bones['shoulder.R'].parent = obArm.data.edit_bones['upper_chest']
    
    #Create The Left Shoulder
    eb = ebs.new("shoulder.L")
    eb.head = (.2, -.1, 13.5) # if the head and tail are the same, the bone is deleted
    eb.tail = (1.7, .6, 13.8)    # upon returning to object mode
    obArm.data.edit_bones['shoulder.L'].parent = obArm.data.edit_bones['upper_chest']
    
    #Create The Right Upper Arm
    eb = ebs.new("upper_arm.R")
    eb.head = (-2, .6, 13.8) # if the head and tail are the same, the bone is deleted
    eb.tail = (-4, .5, 13.7)    # upon returning to object mode
    obArm.data.edit_bones['upper_arm.R'].parent = obArm.data.edit_bones['shoulder.R']
    
    #Create The Left Upper Arm
    eb = ebs.new("upper_arm.L")
    eb.head = (2, .6, 13.8) # if the head and tail are the same, the bone is deleted
    eb.tail = (4, .5, 13.7)    # upon returning to object mode
    obArm.data.edit_bones['upper_arm.L'].parent = obArm.data.edit_bones['shoulder.L']
    
    #Create The Right Lower Arm
    eb = ebs.new("lower_arm.R")
    eb.head = (-4, .5, 13.7) # if the head and tail are the same, the bone is deleted
    eb.tail = (-6.4, .5, 13.7)    # upon returning to object mode
    obArm.data.edit_bones['lower_arm.R'].parent = obArm.data.edit_bones['upper_arm.R']
    
    #Create The Left Lower Arm
    eb = ebs.new("lower_arm.L")
    eb.head = (4, .5, 13.7) # if the head and tail are the same, the bone is deleted
    eb.tail = (6.4, .5, 13.7)    # upon returning to object mode
    obArm.data.edit_bones['lower_arm.L'].parent = obArm.data.edit_bones['upper_arm.L']
    
    #Create The Right Hand
    eb = ebs.new("hand.R")
    eb.head = (-6.4, .5, 13.7) # if the head and tail are the same, the bone is deleted
    eb.tail = (-7, .5, 13.7)    # upon returning to object mode
    obArm.data.edit_bones['hand.R'].parent = obArm.data.edit_bones['lower_arm.R']
    
    #Create The Upper Thumb 
    eb = ebs.new("thumb_proximal.R")
    eb.head = (-6.6, .2, 13.6) # if the head and tail are the same, the bone is deleted
    eb.tail = (-6.8, .15, 13.5)    # upon returning to object mode
    obArm.data.edit_bones['thumb_proximal.R'].parent = obArm.data.edit_bones['hand.R']
    
    #Create The Middle Thumb 
    eb = ebs.new("thumb_intermediate.R")
    eb.head = (-6.8, .15, 13.5) # if the head and tail are the same, the bone is deleted
    eb.tail = (-7.15, .15, 13.44)    # upon returning to object mode
    obArm.data.edit_bones['thumb_intermediate.R'].parent = obArm.data.edit_bones['thumb_proximal.R']
    
    #Create The Lower Thumb 
    eb = ebs.new("thumb_distal.R")
    eb.head = (-7.15, .15, 13.44) # if the head and tail are the same, the bone is deleted
    eb.tail = (-7.35, .15, 13.41)    # upon returning to object mode
    obArm.data.edit_bones['thumb_distal.R'].parent = obArm.data.edit_bones['thumb_intermediate.R']
    
    #Create The Upper Index
    eb = ebs.new("index_proximal.R")
    eb.head = (-7.25, .25, 13.7) # if the head and tail are the same, the bone is deleted
    eb.tail = (-7.5, .25, 13.65)    # upon returning to object mode
    obArm.data.edit_bones['index_proximal.R'].parent = obArm.data.edit_bones['hand.R']
    
    #Create The Middle Index
    eb = ebs.new("index_intermediate.R")
    eb.head = (-7.5, .25, 13.65) # if the head and tail are the same, the bone is deleted
    eb.tail = (-7.8, .25, 13.63)    # upon returning to object mode
    obArm.data.edit_bones['index_intermediate.R'].parent = obArm.data.edit_bones['index_proximal.R']
    
    #Create The Lower Index
    eb = ebs.new("index_distal.R")
    eb.head = (-7.8, .25, 13.63) # if the head and tail are the same, the bone is deleted
    eb.tail = (-7.95, .25, 13.6)    # upon returning to object mode
    obArm.data.edit_bones['index_distal.R'].parent = obArm.data.edit_bones['index_intermediate.R']
    
    #Create The Upper Middle
    eb = ebs.new("middle_proximal.R")
    eb.head = (-7.25, .45, 13.7) # if the head and tail are the same, the bone is deleted
    eb.tail = (-7.6, .45, 13.65)    # upon returning to object mode
    obArm.data.edit_bones['middle_proximal.R'].parent = obArm.data.edit_bones['hand.R']
    
    #Create The Middle Middle
    eb = ebs.new("middle_intermediate.R")
    eb.head = (-7.6, .45, 13.65) # if the head and tail are the same, the bone is deleted
    eb.tail = (-7.85, .45, 13.63)    # upon returning to object mode
    obArm.data.edit_bones['middle_intermediate.R'].parent = obArm.data.edit_bones['middle_proximal.R']
    
    #Create The Lower Middle
    eb = ebs.new("middle_distal.R")
    eb.head = (-7.85, .45, 13.63) # if the head and tail are the same, the bone is deleted
    eb.tail = (-8.05, .45, 13.6)    # upon returning to object mode
    obArm.data.edit_bones['middle_distal.R'].parent = obArm.data.edit_bones['middle_intermediate.R']
    
    #Create The Upper Ring
    eb = ebs.new("ring_proximal.R")
    eb.head = (-7.25, .63, 13.66) # if the head and tail are the same, the bone is deleted
    eb.tail = (-7.5, .63, 13.66)    # upon returning to object mode
    obArm.data.edit_bones['ring_proximal.R'].parent = obArm.data.edit_bones['hand.R']
    
    #Create The Middle Ring
    eb = ebs.new("ring_intermediate.R")
    eb.head = (-7.5, .63, 13.66) # if the head and tail are the same, the bone is deleted
    eb.tail = (-7.75, .63, 13.64)    # upon returning to object mode
    obArm.data.edit_bones['ring_intermediate.R'].parent = obArm.data.edit_bones['ring_proximal.R']
    
    #Create The Lower Ring
    eb = ebs.new("ring_distal.R")
    eb.head = (-7.75, .63, 13.64) # if the head and tail are the same, the bone is deleted
    eb.tail = (-7.95, .63, 13.62)    # upon returning to object mode
    obArm.data.edit_bones['ring_distal.R'].parent = obArm.data.edit_bones['ring_intermediate.R']
    
    #Create The Upper Pinky
    eb = ebs.new("pinky_proximal.R")
    eb.head = (-7.2, .8, 13.65) # if the head and tail are the same, the bone is deleted
    eb.tail = (-7.38, .8, 13.65)    # upon returning to object mode
    obArm.data.edit_bones['pinky_proximal.R'].parent = obArm.data.edit_bones['hand.R']
    
    #Create The Middle Pinky
    eb = ebs.new("pinky_intermediate.R")
    eb.head = (-7.38, .8, 13.65) # if the head and tail are the same, the bone is deleted
    eb.tail = (-7.55, .8, 13.65)    # upon returning to object mode
    obArm.data.edit_bones['pinky_intermediate.R'].parent = obArm.data.edit_bones['pinky_proximal.R']
    
    #Create The Lower Pinky
    eb = ebs.new("pinky_distal.R")
    eb.head = (-7.55, .8, 13.65) # if the head and tail are the same, the bone is deleted
    eb.tail = (-7.7, .8, 13.65)    # upon returning to object mode
    obArm.data.edit_bones['pinky_distal.R'].parent = obArm.data.edit_bones['pinky_intermediate.R']
    
    
    #Create The Left Hand
    eb = ebs.new("hand.L")
    eb.head = (6.4, .5, 13.7) # if the head and tail are the same, the bone is deleted
    eb.tail = (7, .5, 13.7)    # upon returning to object mode
    obArm.data.edit_bones['hand.L'].parent = obArm.data.edit_bones['lower_arm.L']
    
    #Create The Upper Thumb 
    eb = ebs.new("thumb_proximal.L")
    eb.head = (6.6, .2, 13.6) # if the head and tail are the same, the bone is deleted
    eb.tail = (6.8, .15, 13.5)    # upon returning to object mode
    obArm.data.edit_bones['thumb_proximal.L'].parent = obArm.data.edit_bones['hand.L']
    
    #Create The Middle Thumb 
    eb = ebs.new("thumb_intermediate.L")
    eb.head = (6.8, .15, 13.5) # if the head and tail are the same, the bone is deleted
    eb.tail = (7.15, .15, 13.44)    # upon returning to object mode
    obArm.data.edit_bones['thumb_intermediate.L'].parent = obArm.data.edit_bones['thumb_proximal.L']
    
    #Create The Lower Thumb 
    eb = ebs.new("thumb_distal.L")
    eb.head = (7.15, .15, 13.44) # if the head and tail are the same, the bone is deleted
    eb.tail = (7.35, .15, 13.41)    # upon returning to object mode
    obArm.data.edit_bones['thumb_distal.L'].parent = obArm.data.edit_bones['thumb_intermediate.L']
    
    #Create The Upper Index
    eb = ebs.new("index_proximal.L")
    eb.head = (7.25, .25, 13.7) # if the head and tail are the same, the bone is deleted
    eb.tail = (7.5, .25, 13.65)    # upon returning to object mode
    obArm.data.edit_bones['index_proximal.L'].parent = obArm.data.edit_bones['hand.L']
    
    #Create The Middle Index
    eb = ebs.new("index_intermediate.L")
    eb.head = (7.5, .25, 13.65) # if the head and tail are the same, the bone is deleted
    eb.tail = (7.8, .25, 13.63)    # upon returning to object mode
    obArm.data.edit_bones['index_intermediate.L'].parent = obArm.data.edit_bones['index_proximal.L']
    
    #Create The Lower Index
    eb = ebs.new("index_distal.L")
    eb.head = (7.8, .25, 13.63) # if the head and tail are the same, the bone is deleted
    eb.tail = (7.95, .25, 13.6)    # upon returning to object mode
    obArm.data.edit_bones['index_distal.L'].parent = obArm.data.edit_bones['index_intermediate.L']
    
    #Create The Upper Middle
    eb = ebs.new("middle_proximal.L")
    eb.head = (7.25, .45, 13.7) # if the head and tail are the same, the bone is deleted
    eb.tail = (7.6, .45, 13.65)    # upon returning to object mode
    obArm.data.edit_bones['middle_proximal.L'].parent = obArm.data.edit_bones['hand.L']
    
    #Create The Middle Middle
    eb = ebs.new("middle_intermediate.L")
    eb.head = (7.6, .45, 13.65) # if the head and tail are the same, the bone is deleted
    eb.tail = (7.85, .45, 13.63)    # upon returning to object mode
    obArm.data.edit_bones['middle_intermediate.L'].parent = obArm.data.edit_bones['middle_proximal.L']
    
    #Create The Lower Middle
    eb = ebs.new("middle_distal.L")
    eb.head = (7.85, .45, 13.63) # if the head and tail are the same, the bone is deleted
    eb.tail = (8.05, .45, 13.6)    # upon returning to object mode
    obArm.data.edit_bones['middle_distal.L'].parent = obArm.data.edit_bones['middle_intermediate.L']
    
    #Create The Upper Ring
    eb = ebs.new("ring_proximal.L")
    eb.head = (7.25, .63, 13.66) # if the head and tail are the same, the bone is deleted
    eb.tail = (7.5, .63, 13.66)    # upon returning to object mode
    obArm.data.edit_bones['ring_proximal.L'].parent = obArm.data.edit_bones['hand.L']
    
    #Create The Middle Ring
    eb = ebs.new("ring_intermediate.L")
    eb.head = (7.5, .63, 13.66) # if the head and tail are the same, the bone is deleted
    eb.tail = (7.75, .63, 13.64)    # upon returning to object mode
    obArm.data.edit_bones['ring_intermediate.L'].parent = obArm.data.edit_bones['ring_proximal.L']
    
    #Create The Lower Ring
    eb = ebs.new("ring_distal.L")
    eb.head = (7.75, .63, 13.64) # if the head and tail are the same, the bone is deleted
    eb.tail = (7.95, .63, 13.62)    # upon returning to object mode
    obArm.data.edit_bones['ring_distal.L'].parent = obArm.data.edit_bones['ring_intermediate.L']
    
    #Create The Upper Pinky
    eb = ebs.new("pinky_proximal.L")
    eb.head = (7.2, .8, 13.65) # if the head and tail are the same, the bone is deleted
    eb.tail = (7.38, .8, 13.65)    # upon returning to object mode
    obArm.data.edit_bones['pinky_proximal.L'].parent = obArm.data.edit_bones['hand.L']
    
    #Create The Middle Pinky
    eb = ebs.new("pinky_intermediate.L")
    eb.head = (7.38, .8, 13.65) # if the head and tail are the same, the bone is deleted
    eb.tail = (7.55, .8, 13.65)    # upon returning to object mode
    obArm.data.edit_bones['pinky_intermediate.L'].parent = obArm.data.edit_bones['pinky_proximal.L']
    
    #Create The Lower Pinky
    eb = ebs.new("pinky_distal.L")
    eb.head = (7.55, .8, 13.65) # if the head and tail are the same, the bone is deleted
    eb.tail = (7.7, .8, 13.65)    # upon returning to object mode
    obArm.data.edit_bones['pinky_distal.L'].parent = obArm.data.edit_bones['pinky_intermediate.L']
    
    
class SimpleOperator(bpy.types.Operator):
    #tool tip
    bl_idname = "object.simple_operator"
    bl_label = "Generate Unity Rig"

    def execute(self, context):
        main(context)
        return {'FINISHED'}

class UnityRigPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Unity Rigger"
    bl_idname = "OBJECT_PT_layout"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "scene"

    def draw(self, context):
        layout = self.layout
        
        scene = context.scene
        
        layout.label(text="Unity Humanoid Rigger")
        row = layout.row()
        row.scale_y = 2.0
        row.operator("object.simple_operator") 


def register():
    bpy.utils.register_class(UnityRigPanel)
    bpy.utils.register_class(SimpleOperator)

def unregister():
    bpy.utils.unregister_class(UnityRigPanel)
    bpy.utils.unregister_class(SimpleOperator)

if __name__ == "__main__":
    register()

#Test call
#bpy.ops.object.simple_operator()