import subprocess

subprocess.run(['ls', '-l'])
subprocess.run(['mkdir', '-p', 'first-folder'])
subprocess.run(['ls', '-l'])
subprocess.run(['mv', 'first-folder', 'second-folder'])
subprocess.run(['ls', '-l'])
subprocess.run(['rm', '-r', 'second-folder'])
subprocess.run(['ls', '-l'])
