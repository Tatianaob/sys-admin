# import os
import subprocess

# os.system("ls")
# subprocess.run(["ls", "-l", "README.md"])

command="uname"
commandArgument="-a"
print(f'Gathering system information with commad: {command} {commandArgument}')
subprocess.run([command, commandArgument])


command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])