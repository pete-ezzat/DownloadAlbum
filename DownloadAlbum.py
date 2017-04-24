#!/usr/bin/python2

import re
import os
import urllib
import argparse
from BeautifulSoup import *

def download_song(link):
   wget_link = "wget -{} {}{}{}".format("c", '"', link, '"')
   os.system(wget_link)

def get_link(song):
   source_code = urllib.urlopen(song)
   for line in source_code:
      if line.startswith('<div align="center" class="orange" dir="rtl"><img src="http://www.melody4arab.com/images/download'):
         link = line[130:]
         el = re.search('http.*?(mp3)', link)
         link = link[el.start():el.end()]
         download_song(link)

parser = argparse.ArgumentParser(description="Downloading full albums from melody4arab.com")
parser.add_argument('-l', type=str, help="Set album download link.", required=False)
the_args = parser.parse_args()

url = ''

if the_args.l is not None:
   url = the_args.l
else:
   url = raw_input("Album Link: ")

source_code = urllib.urlopen(url).read()
soup = BeautifulSoup(source_code)

tags = soup('a')
for tag in tags:
   link = tag.get('href', None)
   if link.startswith('http://www.melody4arab.com/download/ar_download'):
      print link
      get_link(link)
