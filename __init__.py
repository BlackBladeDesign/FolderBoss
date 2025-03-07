import bpy
import os
import shutil

bl_info = {
    "name": "Folder Boss",
    "blender": (4, 3, 0),
    "category": "Organization",
}


class FolderBossOperator(bpy.types.Operator):
    bl_idname = "object.folder_boss_operator"
    bl_label = "Folder Boss Operator"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        blend_file_path = bpy.data.filepath
        if not blend_file_path:
            self.report({'ERROR'}, "Please save the blend file first.")
            return {'CANCELLED'}

        blend_dir = os.path.dirname(blend_file_path)
        folders = ["Blend", "Textures", "References", "FBX"]

        blend_file_name = os.path.splitext(os.path.basename(blend_file_path))[0]
        parent_folder_path = os.path.join(blend_dir, blend_file_name)

        if not os.path.exists(parent_folder_path):
            os.makedirs(parent_folder_path)

        for folder in folders:
            folder_path = os.path.join(parent_folder_path, folder)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

        blend_file_name = os.path.basename(blend_file_path)
        new_blend_path = os.path.join(parent_folder_path, "Blend", blend_file_name)

        if blend_file_path != new_blend_path:
            shutil.move(blend_file_path, new_blend_path)
            bpy.ops.wm.open_mainfile(filepath=new_blend_path)

        return {'FINISHED'}

def menu_func(self, context):
    self.layout.operator(FolderBossOperator.bl_idname)

def register():
    bpy.utils.register_class(FolderBossOperator)
    bpy.types.TOPBAR_MT_file.append(menu_func)

def unregister():
    bpy.utils.unregister_class(FolderBossOperator)
    bpy.types.TOPBAR_MT_file.remove(menu_func)

if __name__ == "__main__":
    register()