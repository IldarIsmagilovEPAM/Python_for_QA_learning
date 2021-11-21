import os
import sys
import subprocess

print(os.path.basename(sys.argv[0]))


subprocess.run(f'python {sys.argv[1]}.py')

