import os

def get_files_info(working_directory: str, directory: str=".") -> str:
    try:
        working_dir_abs=os.path.abspath(working_directory)
        target_dir=os.path.normpath(os.path.join(working_dir_abs,directory))
        valid_target_dir=os.path.commonpath([working_dir_abs,target_dir])==working_dir_abs
        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        print(target_dir)
        valid_directory=os.path.isdir(target_dir)
        
        if not valid_directory:
            return f'Error: "{directory}" is not a directory'

        files=os.listdir(target_dir)
        print(files)
        file_size_list=[]
        is_file_dir=[]
        for file in files:
            file_path=(os.path.join(target_dir,file))
            file_size_list.append(os.path.getsize(file_path))
            is_file_dir.append(os.path.isdir(file_path))


        print(file_size_list)
        print(is_file_dir)

        


            
    except Exception as e:
        return f"Error: {e}"
        

