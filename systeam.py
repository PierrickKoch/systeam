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

def str_last_month():
    from datetime import timedelta, datetime
    dt1 = datetime.today().replace(day=1) # first day of this month
    dt2 = dt1 - timedelta(days=1) # subtract one day = previous month
    return dt2.strftime("%Y-%m")

def main(url = STEAM_SURVEY):
    doc = load(url)
    elements = select(doc)
    result = {}
    result['linux'] = process(elements, ["Ubuntu", "Linux", "Gentoo", "Fedora", "openSUSE"])
    result['windows'] = process(elements, ["Windows"])
    result['macos'] = process(elements, ["MacOS"])
    print({str_last_month(): result})

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1 and sys.argv[1].startswith("http"):
        main(sys.argv[1])
    else:
        main()

