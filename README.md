# Project Folder Organizer

## Overview

This tool helps to automatically organize your Blender project files into a standardized folder structure. It simplifies the process of maintaining an organized workflow by creating dedicated subfolders for different types of assets.
![Screenshot 2025-03-08 002345](https://github.com/user-attachments/assets/b2de9ec2-0a1f-43b7-82db-2e8b2aaa88fd)

## Features

- **Folder Creation**: Automatically creates a new folder in the same directory where the Blend file is located.
- **Subfolder Organization**: The following subfolders are created within the new folder:
  - `Blend`: Contains the original `.blend` file.
  - `Textures`: Stores all texture files related to the project.
  - `FBX`: Holds any exported `.fbx` files.
- **File Relocation**: The script automatically moves your `.blend` file into the `Blend` folder, keeping your project clean and organized.

## Benefits

- **Consistency**: Maintains a consistent file structure for all your projects, making it easier to manage and share assets.
- **Efficiency**: Saves time by automatically organizing and moving files, so you don't have to do it manually.
- **Scalability**: This system will eventually be extended to organize all linked assets in the same way.

## How It Works

1. The tool will scan the directory where your `.blend` file is saved.
2. It will create a new folder using the name of the `.blend` file.
3. Inside this new folder, the tool will create the `Blend`, `Textures`, and `FBX` subfolders.
4. The `.blend` file will be automatically moved into the `Blend` folder.
   
By using this tool, you can ensure that your Blender projects are organized in a clear and predictable way from the start.

## Using The Addon

1. Open your Blender project.
2. Navigate to `File > Folder Boss Operator` from the Blender top menu.
3. The tool will automatically organize the project and move the files into the appropriate subfolders.

## Installation

1. Download as a .Zip from this repository.
2. Open Blender and go to `Edit > Preferences > Add-ons > Install`.
3. Navigate to the downloaded script file and select it.
4. After installation, enable the add-on by checking the box next to its name in the Add-ons menu.
5. The tool will now be accessible under `File > Folder Boss Operator`.

## Future Plans

- Extend the system to organize all linked assets (such as textures, references, and other project files) in the same folder structure.
- Improve the script with additional configuration options to cater to different workflows.
- Add functionality to handle other file types, such as animation files, renders, and more, for a more comprehensive organization solution.
