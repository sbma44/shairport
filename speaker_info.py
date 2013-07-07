from soco import SonosDiscovery, SoCo
import json
from settings import *

def refresh_speaker_info():
	sd = SonosDiscovery()
	possible_matches = sd.get_speaker_ips()
	speaker_info = {}
	for ip in possible_matches:
		s = SoCo(ip)
		try:			
			speaker_info[ip] = s.get_speaker_info()
		except Exception, e:
			speaker_info[ip] = {}

	f = open("%s%s" % (DIRECTORY, SPEAKER_INFO_FILE), 'w')
	json.dump(speaker_info, f)
	f.close()

def load_speaker_info():
	f = open("%s%s" % (DIRECTORY, SPEAKER_INFO_FILE), 'r')
	j = json.load(f)
	f.close()
	return j

def store_volume(ip, volume):
	f = open("%s%s_volume.json" % (DIRECTORY, ip), 'w')
	json.dump(volume, f)
	f.close()

def recall_volume(ip):
	f = open("%s%s_volume.json" % (DIRECTORY, ip), 'r')
	j = json.load(f)
	f.close()
	return j

if __name__ == '__main__':
	refresh_speaker_info()