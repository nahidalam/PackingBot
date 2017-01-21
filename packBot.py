__author__ = "Nahid Alam"
__copyright__ = "Copyright 2017"

import sys
import json
import urllib
import contextlib
from operator import attrgetter


class Solution(object):
	def __init__(self, volume, ids, value):
		self.volume = volume
		self.ids = ids
		self.value = value		


def printResult(solutions):
	maxValue = max(solutions, key=attrgetter("value")).value
	ids = max(solutions, key=attrgetter("value")).ids
	data = {}
	data['part_ids'] = ids
	data['value'] = maxValue
	json_data = json.dumps(data)
	print json_data


def compute(parts, suitVol):
	solutions = []
	solutions.append(Solution(0, [], 0))

	for part in parts:
	
		length = len(solutions)
		currIndex = length - 1

		while currIndex >= 0:

			volume = solutions[currIndex].volume + part['volume']
		
			if volume <= suitVol:

				value = solutions[currIndex].value + part['value']
				ids = solutions[currIndex].ids[:] 
				ids.append(part['id'])

				k = currIndex
				
				while k < len(solutions):
					if solutions[k].volume < volume :
						k = k + 1
					else: 
						break

				if k >= len(solutions):
					solutions.append(Solution(volume, ids, value))
				elif solutions[k].volume == volume:
					if solutions[k].value < value:
						solutions[k].value = value
				else: 
					solutions.insert(k, Solution(volume, ids, value))
			currIndex = currIndex - 1
	return solutions


def main():
	urlsuitcase = sys.argv[1]
	urlparts = sys.argv[2]

	with contextlib.closing(urllib.urlopen(urlsuitcase)) as suitResponse:
		suit = json.loads(suitResponse.read())
		suitVol = suit['volume']

	with contextlib.closing(urllib.urlopen(urlparts)) as partsResponse:
		parts = json.loads(partsResponse.read())

	
	printResult(compute(parts, suitVol))



if __name__ == "__main__":
	main()

