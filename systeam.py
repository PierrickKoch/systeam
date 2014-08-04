#!/usr/bin/env python

# http://web.archive.org/web/*/store.steampowered.com/hwsurvey
# http://webcache.googleusercontent.com/search?q=cache:store.steampowered.com/hwsurvey
# for page prior to January 2014, use the previous version of this script:
# https://github.com/pierriko/systeam/blob/jan14/systeam.py
STEAM_SURVEY = "http://store.steampowered.com/hwsurvey"

import sys
from lxml.html import parse
from datetime import datetime

def main(url = STEAM_SURVEY):
    elt = parse(url).getroot()
    res = {os: float(elt.xpath('//*[@id="osversion_details"]/*[@id="cat%i_stats_row"]/div[3]'%cat)[0].text[:-1])
           for os,cat in {'windows':0, 'macos':1, 'linux':2}.items()}
    print({datetime.today().strftime("%Y-%m-%d"): res})
    print('[info] %.2f%% unknown'%(100.0-sum(res.values())))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()
