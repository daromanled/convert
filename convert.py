import glob
import os.path
import subprocess

convert = "D:\\convert.exe"

files = glob.glob(os.path.join('Source', "*.jpg"))
os.mkdir('Result')
for file in files:
    name_of_file = file.replace('Source', 'Result')
    process = subprocess.run([convert, file, '-resize', '200', name_of_file])
