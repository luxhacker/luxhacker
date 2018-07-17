import requests
from selenium import webdriver
from time import sleep


def main():
    cus_profile_dir = r"C:\Users\ASUS\AppData\Roaming\Mozilla\Firefox\Profiles\js42l6nq.default"  # 你自定义profile的路径
    fp = webdriver.FirefoxProfile(cus_profile_dir)
    fp.set_preference("browser.download.folderList", 2)
    fp.set_preference("browser.download.manager.showWhenStarting", False)
    fp.set_preference("browser.download.dir", "/PythonDemo/test")
    fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")  # binary/octet-stream

    fp.update_preferences()
    br = webdriver.Firefox(firefox_profile=fp)     # 打开浏览器
    selenium_cookies = br.get_cookies()
    if not len(selenium_cookies):
        br.get("http://www.97yxt.com/")     # 打开想要爬取的知乎页面
        br.find_element_by_xpath("//input[@id='txtUserName2']").send_keys("yunxuetang")
        br.find_element_by_xpath("//input[@id='txtPassword2']").send_keys("jiuqi@123")
        br.find_element_by_xpath("//input[@id='btnLogin2']").click()
        selenium_cookies = br.get_cookies()
    # br.quit()
    # 接下来由request接受selenium的cookie，并访问网站
    s = requests.Session()
    cookie_dict = {}
    for i in selenium_cookies:
        s.cookies.set(i['name'], i['value'])
        cookie_dict.__setitem__(i['name'], i['value'])
        # requests.utils.add_dict_to_cookiejar(s.cookies, {i['name']: i['value']})
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:57.0) Gecko/20100101 Firefox/57.0',
        "Referer": "http://www.97yxt.com/login.htm",
        'Host': 'beacon.tingyun.com'
    }

    with requests.get('http://www.97yxt.com/', headers=headers) as response:
        print(response.status_code)
        # 模拟用户操作

        br.find_element_by_xpath("//i[@class='icon-book']").click()
        currentWindow = br.current_window_handle
        for handles in br.window_handles:
            if handles == currentWindow:
                continue
            else:
                br.switch_to.window(handles)
        # br.switch_to.window(br.window_handles[-1])
        sleep(1)
        names = br.find_elements_by_xpath("//span[@class='Knowledge_CoursePackage']")
        for name in names:
            name.click()
            # br.switch_to.window(br.window_handles[-1])
            thiswin = br.current_window_handle
            for bianli in br.window_handles:
                if bianli != thiswin:
                    br.switch_to.window(bianli)
            sleep(1)
            videos = br.find_elements_by_xpath("//a[@class='text-color6']")
            for video in videos:
                sleep(1)
                video.click()
                br.switch_to.window(br.window_handles[-1])
                currwin = br.current_window_handle
                for lala in br.window_handles:
                    if lala != currwin:
                        br.switch_to.window(lala)
                sleep(2)
                br.find_element_by_xpath("//span[@class='el-icon-download']").click()
                br.close()
                br.switch_to.window(currwin)

            br.close()
            br.switch_to.window(thiswin)
        br.close()
if __name__ == '__main__':
    main()





