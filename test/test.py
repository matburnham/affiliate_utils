import unittest
from affiliate_utils import get_target, strip_www, url_to_domain

class testUrlToDomain(unittest.TestCase):
    """Test url_to_domain functionality."""

    def testEmpty(self):
        self.assertEqual(url_to_domain(''), None)

    def testHttp(self):
        self.assertEqual(url_to_domain('http://example.org'), 'example.org')

    def testHttp2(self):
        self.assertEqual(url_to_domain('http://example.org/foo'), 'example.org')

    def testHttp3(self):
        self.assertEqual(url_to_domain('http://example.org/foo/bar'), 'example.org')
        
    def testPort(self):
        self.assertEqual(url_to_domain('http://www.example.org:80'), 'www.example.org')

    def testNoHttp1(self):
        self.assertEqual(url_to_domain('example.org'), 'example.org')

    def testNoHttp2(self):
        self.assertEqual(url_to_domain('example.org/foo'), 'example.org')

    def testNoHttp3(self):
        self.assertEqual(url_to_domain('example.org/foo/bar'), 'example.org')

    def testSansWww(self):
        self.assertEqual(url_to_domain('asda.com'), 'asda.com')

    def testWww(self):
        self.assertEqual(url_to_domain('www.asda.com'), 'www.asda.com')

    def testDirect(self):
        self.assertEqual(url_to_domain('direct.asda.com'), 'direct.asda.com')


class testStripWww(unittest.TestCase):
    """Test strip_www functionality"""

    def testEmpty(self):
        self.assertEqual(strip_www(''), '')

    def testHttp(self):
        self.assertEqual(strip_www('http://example.org'), 'http://example.org')

    def testSansWww(self):
        self.assertEqual(strip_www('asda.com'), 'asda.com')

    def testWww(self):
        self.assertEqual(strip_www('www.asda.com'), 'asda.com')

    def testDirect(self):
        self.assertEqual(strip_www('direct.asda.com'), 'direct.asda.com')

class testAffiliateLinks(unittest.TestCase):
    """Test AffiliateWindow URLs."""

    def testGetTargetTCB(self):
        src = 'https://www.topcashback.co.uk/earncashback.aspx?mpurl=currys&continue=1'
        target = 'http://www.currys.co.uk/gbuk/index.html?srcid=369&xtor=AL-1&cmpid=aff~TopCashBack~'
        domain = 'currys.co.uk'
        url = get_target(src)
        self.assertEqual(url,target)
        self.assertEqual(strip_www(url_to_domain(url)), domain)

    def testGetTargetMediaplex(self):
        src = 'http://adfarm.mediaplex.com/ad/ck/15368-110724-36269-43?CJAID=801842&CJPID=1777643&ttp=100&rfr=123'
        target = 'https://promotions.betfair.com/value-uk-football-dual-aff-t?CID=&PLA=153681107243626943&ttp=100&rfr=123&mpch=ads'
        domain = 'promotions.betfair.com'
        url = get_target(src)
        self.assertEqual(url,target)
        self.assertEqual(strip_www(url_to_domain(url)), domain)

#    def testGetTargetAW(self):
#        src = 'https://www.topcashback.co.uk/earncashback.aspx?mpurl=currys&continue=1&x=**'
 #       target = 'http://www.currys.co.uk/gbuk/index.html?srcid=369&xtor=AL-1&cmpid=aff~TopCashBack~'
  #      self.assertEqual(get_target(src),target)

#def suite():
#    suite = unittest.TestSuite()
#    suite.addTest(unittest.makeSuite(testAffiliateWindow))
#    return suite

if __name__ == '__main__':
    unittest.main()

