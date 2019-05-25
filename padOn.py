import os, re, subprocess

result = subprocess.check_output('xinput', shell=True)
result = str(result)
p = re.search('Touchpad\D*(\d+)', result)

id = p.group(1)

os.system('xinput set-int-prop %s "Device Enabled" 8 1' % (id))
