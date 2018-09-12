from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import base64


service_args = ['--proxy=zproxy.lum-superproxy.io:22225',
                    '--proxy-type=http']
authentication_token = 'Basic ' + base64.b64encode(b'lum-customer-hl_3ce1ccc6-zone-static-country-us:1ltxhtyklc0u')
capa = DesiredCapabilities.PHANTOMJS
capa['phantomjs.page.customHeaders.Proxy-Authorization'] = authentication_token
driver = webdriver.PhantomJS(executable_path='/Users/apple/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs',
                             desired_capabilities=capa, service_args=service_args)
driver.get('http://www.baidu.com')
print driver.page_source