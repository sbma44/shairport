import re
from settings import *
from soco import SonosDiscovery, SoCo
import speaker_info

def main():
	si = {}
	try:
		si = speaker_info.load_speaker_info()
	except Exception, e:
		speaker_info.refresh_speaker_info()
		si = speaker_info.load_speaker_info()	
	
	for (ip, speaker) in si.items():
		if re.search(PRIMARY_ZONE, speaker.get('zone_name', ''), re.I) is not None:
			s = SoCo(ip)
			s.volume(speaker_info.recall_volume(ip))
			s.stop()

if __name__ == '__main__':
	main()
