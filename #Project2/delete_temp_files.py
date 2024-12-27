import os
import shutil
import tempfile

def delete_temp_files():
    """
    Deletes files and folders in the system's temporary directory.
    """
    # Get the path to the temporary directory
    temp_dir = tempfile.gettempdir()
    print(f"Temporary directory: {temp_dir}")
    
    # Counter for tracking deletion
    deleted_files = 0
    deleted_folders = 0

    try:
        for item in os.listdir(temp_dir):
            item_path = os.path.join(temp_dir, item)
            
            # Check if it's a file
            if os.path.isfile(item_path) or os.path.islink(item_path):
                try:
                    os.unlink(item_path)  # Remove file or symbolic link
                    deleted_files += 1
                except Exception as e:
                    print(f"Failed to delete file: {item_path}. Reason: {e}")
            
            # Check if it's a folder
            elif os.path.isdir(item_path):
                try:
                    shutil.rmtree(item_path)  # Remove directory and contents
                    deleted_folders += 1
                except Exception as e:
                    print(f"Failed to delete folder: {item_path}. Reason: {e}")

    except Exception as e:
        print(f"Error while accessing temporary directory. Reason: {e}")

    print(f"Deleted {deleted_files} files and {deleted_folders} folders from {temp_dir}.")

# Run the function
if __name__ == "__main__":
    delete_temp_files()