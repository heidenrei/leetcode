# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        s = set()
        start = startUrl[7:].split('/')[0]
        def go(startUrl, htmlParser, starter):
            s.add(startUrl)
            for x in htmlParser.getUrls(startUrl):
                tmp_starter = x[7:].split('/')[0]
                if tmp_starter != starter:
                    continue
                if x not in s:
                    go(x, htmlParser, starter)
        go(startUrl, htmlParser, start)
        return list(s)