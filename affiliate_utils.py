"""Affiliate Utils

Utility module to process affiliate URLs.

Supports the following URLs:
* TopCashback
* Mediaplex

"""

import lxml.html
import urlparse
import urllib2

__all__ = ['url_to_domain', 'strip_www', 'get_target']

def url_to_domain(url):
    """
    Returns the domain portion of a URL.
    
    >>> url_to_domain('http://infinitemonkeycorps.net/docs/pph/#unittest')
    'infinitemonkeycorps.net'
    
    :param url: URL
    :type url: string
    :return: Domain portion of URL
    :rtype: string
    
    """
    # handle URLs without a scheme nicely
    if urlparse.urlparse(url).scheme not in ['http', 'https']:
        url = 'http://' + url
    return urlparse.urlparse(url).hostname

def strip_www(domain):
    """
    Strips any www. prefix from a domain name.

    >>> strip_www('www.google.com')
    'google.com'

    :param domain: domain name
    :type domain: string
    :return: Domain name with any 'www.' prefix removed
    :rtype: string
    
    """
    if domain.startswith('www.'):
        return domain[4:]
    else:
        return domain

def get_target(url):
    """
    Returns the target URL of an affiliate link.
    
    >>> get_target('https://www.topcashback.co.uk/earncashback.aspx?mpurl=currys&continue=1')
    'http://www.currys.co.uk/gbuk/index.html?srcid=369&xtor=AL-1&cmpid=aff~TopCashBack~'
    
    :param url: URL
    :type url: string
    :return: Target URL that supplied URL resolves to
    :rtype: string
    """
    domain = strip_www(url_to_domain(url))
    if domain in ['topcashback.com', 'topcashback.co.uk']:
        return _get_tcb_target(url)
    elif domain in ['adfarm.mediaplex.com']:
        return _get_tcb_target(url)
    else:
        return url

def _follow_first_link(url):
    """Returns the target URL by following the first <A HREF='...'>link</A>
    found.
    
    """
    response = urllib2.urlopen(url)
    # TODO: error checking
    html = response.read()
    
    # TopCashback brings up a banner page with Javascript redirect
    # - find the manual redirect
    root = lxml.html.fromstring(html)
    links = root.xpath("//a")
    url = links[0].attrib['href']
    target_url = urllib2.urlopen(url).url
    return target_url

def _get_tcb_target(url):
    """Returns the target URL of a TopCashback splash screen forwarding page."""
    return _follow_first_link(url)

def _get_mediaplex_target(url):
    """Returns the target URL of a Mediaplex forwarding page.
    
    Source: http://adfarm.mediaplex.com/ad/ck/15368-110724-36269-43?
        CJAID=801842&CJPID=1777643&ttp=100&rfr=123

    Content:
    --------
    <html><head><title></title>
    <script language="JavaScript1.1">
    <!--
    window.location.replace("https://promotions.betfair.com/value-uk-
        football-dual-aff-t?CID=&PLA=153681107243626943&ttp=100&rfr=123&
        mpch=ads");
    //-->
    </script>
    <noscript>
    <meta http-equiv="refresh"
        content="0;URL=https://promotions.betfair.com/value-uk-football-
        dual-aff-t?CID=&PLA=153681107243626943&ttp=100&rfr=123&mpch=ads">
    </noscript>
    </head><body><a href="https://promotions.betfair.com/value-uk-football
        -dual-aff-t?CID=&PLA=153681107243626943&ttp=100&rfr=123&mpch=ads">
        Click Here</a></body></html>

    Target: https://promotions.betfair.com/value-uk-football-dual-aff-t?
        CID=&PLA=153681107243626943&ttp=100&rfr=123&mpch=ads"""
    return _follow_first_link(url)

