from selenium import webdriver
import time
import re


def search_product():
    driver.find_element_by_xpath('//*[@id="q"]').send_keys(kw)
    driver.find_element_by_xpath(
        '//*[@id="J_TSearchForm"]/div[1]/button').click()
    time.sleep(20)
    token = driver.find_element_by_xpath(
        '//*[@id="mainsrp-pager"]/div/div/div/div[1]').text
    token = int(re.compile('(\\d+)').search(token).group(1))
    return token


def drop_down():
    for x in range(1, 11):
        js = 'window.scrollBy(0,600)'
        driver.execute_script(js)
        time.sleep(0.5)

        # j = x/10
        # js = 'documentElement.scrollTop = document.documentElement.scrollHeight * %f' % j
        # driver.execute_script(js)


def get_product():
    divs = driver.find_elements_by_xpath(
        '//div[@class="items"]/div[@class="item J_MouserOnverReq  "]')
    for div in divs:
        image = div.find_element_by_xpath(
            './/div[@class="pic"]/a/img').get_attribute('src')
        deal = div.find_element_by_xpath('.//div[@class="deal-cnt"]').text
        product = {'订单量': deal, '图片': image}
        print(product)


def next_page():
    token = search_product()
    drop_down()
    get_product()
    num = 1
    while num != token:
        driver.get('https://s.taobao.com/search?q={}&s={}'.format(
            kw, 44 * num))
        driver.implicitly_wait(10)
        num += 1
        drop_down()
        get_product()


kw = input('请输入你想要查询的商品')
driver = webdriver.Chrome()
driver.get('https://www.taobao.com/')
driver.maximize_window()
next_page()
