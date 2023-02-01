
import os

path_to_file = r"lok2_Trim_Trim3_Trim444.mp4"
file_id = os.stat(path_to_file, follow_symlinks=False).st_ino
print(hex(file_id))