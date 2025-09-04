import subprocess
import os

# Do not apply to patients' data, using module-mode(internet connection)!
# written by Takeshi Ohkubo


os.chdir('/home/shimada-hospital-ubuntu-2000/dictation-kit-4.5')
subprocess.run(['chmod', 'u+x', 'bin/linux/julius'], shell=False)
cmd1=['sh', 'run-linux-dnn.sh']


p1=subprocess.Popen(cmd1, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
for line in iter(p1.stdout.readline,b''):
    txt2=line.rstrip().decode("utf-8", errors='ignore')
    if txt2=="sentence1:  終わり 。":
        break
    if txt2.startswith('sentence1:'):
        txt3=txt2[12:]
        txt3=txt3.replace(' ', '')
        print(txt3)

