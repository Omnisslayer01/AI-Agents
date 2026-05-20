import os

def get_files_info(working_directory: str, directory: str=".") -> str:
    try:
        working_dir_abs=os.path.abspath(working_directory)
        target_dir=os.path.normpath(os.path.join(working_dir_abs,directory))
        valid_target_dir=os.path.commonpath([working_dir_abs,target_dir])==working_dir_abs

        
        if directory==".":
            directory="current"
        final_str=f"Result for {directory} directory: \n"

        if not valid_target_dir:
            return f'{final_str} \t Error: Cannot list "{directory}" as it is outside the permitted working directory'
        valid_directory=os.path.isdir(target_dir)
        
        if not valid_directory:
            return f'{final_str} \t Error: "{directory}" is not a directory'

        files=os.listdir(target_dir)
        
        
        for file in files:
            file_path=(os.path.join(target_dir,file))
            final_str+=f"\t - {file}: file_size={os.path.getsize(file_path)} bytes, is_dir={os.path.isdir(file_path)}\n"
        
        return final_str
            
            
    except Exception as e:
        return f"Error: {e}"
        

