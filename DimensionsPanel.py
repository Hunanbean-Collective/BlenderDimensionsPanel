bl_info = {
    "name": "Dimensions Panel",
    "author": "Hunanbean, with ChatGPT4",
    "version": (1, 0),
    "blender": (3, 3, 0),
    "description": "Add a Dimensions panel to the Object Properties. Due to Blender design, i cannot seem to add it directly to the existing Transform Panel. It must be its own",
    "category": "Object",
    "location": "Properties > Object > Dimensions",
}

import bpy

class OBJECT_PT_CustomDimensions(bpy.types.Panel):
    bl_label = "Transform"
    bl_idname = "OBJECT_PT_custom_dimensions"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"
    
    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True

        obj = context.object

        col = layout.column()
        row = col.row(align=True)
        row.prop(obj, "dimensions")

def register():
    bpy.utils.register_class(OBJECT_PT_CustomDimensions)

def unregister():
    bpy.utils.unregister_class(OBJECT_PT_CustomDimensions)

if __name__ == "__main__":
    register()
