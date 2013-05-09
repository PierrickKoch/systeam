#!/usr/bin/env python

# http://web.archive.org/web/*/store.steampowered.com/hwsurvey
# http://webcache.googleusercontent.com/search?q=cache:store.steampowered.com/hwsurvey
STEAM_SURVEY = "http://store.steampowered.com/hwsurvey"

def load(url):
    from lxml.html import parse
    return parse(url).getroot()

def select(doc):
    return doc.cssselect('div.stats_col_mid.data_row')

def filterc(elements, subs):
    return [elt for elt in elements if subs in elt.text_content()]

def process(elements, substrs):
    total = 0.0
    for subs in substrs:
        for elt in filterc(elements, subs):
            # get the text of the next element, the percentage value
            percent = elt.itersiblings().next()
            # remove the '%' and parse as float
            total += float(percent.text_content()[:-1])
    # result
    return total

def date():
    from datetime import datetime
    return  datetime.today().strftime("%Y-%m-%d")

def main(url = STEAM_SURVEY):
    elements = select( load(url) )
    result = {}
    result['linux'] = process(elements, ["Ubuntu", "Linux", "Gentoo", "Fedora", "openSUSE"])
    result['windows'] = process(elements, ["Windows"])
    result['macos'] = process(elements, ["MacOS"])
    print({date(): result})

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()

