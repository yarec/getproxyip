#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @author   xubigshu@gmail.com
# @site     http://www.51lu.me
# @date     2016-1-9
#

from etc.logger import logger
from crawler.daily import CZ88, KuaiDaiLi
from crawler.hourly import KuaiDaiLi2, XiCiDaiLi, IP66, \
    IP66API, IP002, CNProxy, CNProxyForeign

class Crawler:
    """ Crawl the public proxy ip from the Internet. """

    @classmethod
    def run(cls):
        proxyip = []
        for source in [CNProxy, CNProxyForeign, IP66, IP66API, IP002, \
                       XiCiDaiLi, CZ88, KuaiDaiLi, IP002, KuaiDaiLi2]:
            instance = source()
            proxyips = instance.crawl()
            proxyip.extend(proxyips)
            logger.info('%s crawl ip: %s', source, len(proxyips))

        return proxyip
