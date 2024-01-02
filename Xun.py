
import platform
import os
arc = str(platform.uname().machine)
if 'arm' in arc:
	__import__("latter")._site_view_()
elif 'aarch' in arc:
	__import__("Clinee").destroy_your_barin_already()
else:
	exit(f' Unknow device machine {arc}')
