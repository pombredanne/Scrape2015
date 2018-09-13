from selenium import webdriver
import string
import zipfile
import os
# 代理服务器
proxyHost = "http-dyn.abuyun.com"
proxyPort = "9020"

# 代理隧道验证信息
proxyUser = "HVC6298Y0L8Z251D"
proxyPass = "53F57448DC830845"


def create_proxy_auth_extension(proxy_host, proxy_port,
                                proxy_username, proxy_password,
                                scheme='http', plugin_path=None):
    if plugin_path is None:
        plugin_path = os.getcwd()+r'/{}_{}@http-dyn.abuyun.com_9020.zip'.format(proxy_username, proxy_password)

    manifest_json = """
       {
           "version": "1.0.0",
           "manifest_version": 2,
           "name": "Abuyun Proxy",
           "permissions": [
               "proxy",
               "tabs",
               "unlimitedStorage",
               "storage",
               "<all_urls>",
               "webRequest",
               "webRequestBlocking"
           ],
           "background": {
               "scripts": ["background.js"]
           },
           "minimum_chrome_version":"22.0.0"
       }
       """
    print("sadadaasda")

    background_js = string.Template(
        """
        var config = {
            mode: "fixed_servers",
            rules: {
                singleProxy: {
                    scheme: "${scheme}",
                    host: "${host}",
                    port: parseInt(${port})
                },
                bypassList: ["foobar.com"]
            }
          };

        chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

        function callbackFn(details) {
            return {
                authCredentials: {
                    username: "${username}",
                    password: "${password}"
                }
            };
        }

        chrome.webRequest.onAuthRequired.addListener(
            callbackFn,
            {urls: ["<all_urls>"]},
            ['blocking']
        );
        """
    ).substitute(
        host=proxy_host,
        port=proxy_port,
        username=proxy_username,
        password=proxy_password,
        scheme=scheme,
    )

    with zipfile.ZipFile(plugin_path, 'w') as zp:
        zp.writestr("manifest.json", manifest_json)
        zp.writestr("background.js", background_js)
    print("bbbbbb")

    return plugin_path


proxy_auth_plugin_path = create_proxy_auth_extension(
    proxy_host=proxyHost,
    proxy_port=proxyPort,
    proxy_username=proxyUser,
    proxy_password=proxyPass)
print("cccccccc")

option = webdriver.ChromeOptions()
option.add_argument("--start-maximized")
option.add_extension(proxy_auth_plugin_path)
print("ddddddd")
driver = webdriver.Chrome(options=option)
driver.get("https://www.baidu.com/") 
print (driver.page_source)
print("eeeeeee")
