#!/usr/bin/env python

def load(url):
    from lxml.html import parse
    return parse(url).getroot()

results={}
urls='''
http://web.archive.org/web/20140228170316/http://store.steampowered.com/hwsurvey
http://web.archive.org/web/20140326133356/http://store.steampowered.com/hwsurvey
http://web.archive.org/web/20140530012800/http://store.steampowered.com/hwsurvey
http://web.archive.org/web/20140622203216/http://store.steampowered.com/hwsurvey
http://web.archive.org/web/20140625131340/http://store.steampowered.com/hwsurvey
http://web.archive.org/web/20140626023713/http://store.steampowered.com/hwsurvey
http://web.archive.org/web/20140718223214/http://store.steampowered.com/hwsurvey
'''.split()
for url in urls:
    d = url[27:35]
    elt = load(url)
    results['%s-%s-%s'%( d[:4], d[4:6], d[6:] )] = \
        {os: float(elt.xpath('//*[@id="osversion_details"]/*[@id="cat%i_stats_row"]/div[3]'%cat)[0].text[:-1])
           for os,cat in {'windows':0, 'macos':1, 'linux':2}.items()}

print(results)
