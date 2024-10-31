import subprocess

def reboot():
	print('func reboot')
	cmdReboot = "sudo shutdown -r now"
	subprocess.run(cmdReboot, shell=True)
