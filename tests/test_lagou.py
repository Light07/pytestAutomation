# coding=utf-8

import json
import requests
import pytest
from selenium import webdriver

flag = 1


def cookie_to_selenium_format(self, cookie):
    cookie_selenium_mapping = {'path': '', 'secure': '', 'name': '', 'value': '', 'expires': ''}
    cookie_dict = {}
    if getattr(cookie, 'domain_initial_dot'):
        cookie_dict['domain'] = '.' + getattr(cookie, 'domain')
    else:
        cookie_dict['domain'] = getattr(cookie, 'domain')
    for k in list(cookie_selenium_mapping.keys()):
        key = k
        value = getattr(cookie, k)
        cookie_dict[key] = value
    return cookie_dict

@pytest.mark.lagou
class TestLaGou:
    # 在pytest里，针对一个类方法的setup为setup_method,
    # setup_method作用同unittest里的setUp()
    def setup_method(self, method):
        self.s = requests.Session()
        self.url = 'https://www.lagou.com'

    def test_visit_lagou(self):
        result = self.s.get(self.url)
        assert result.status_code == 200
        assert '拉勾' in result.text

    @pytest.mark.notToRun
    def test_get_new_message(self):
        # 此处需要一个方法登录获取登录的cookie
        message_url = 'https://gate.lagou.com/v1/entry/message/newMessageList'
        cookie = {
            'cookie': '_gid=GA1.2.438589688.1601450871; gate_login_token=475844a837230240e1e73e4ecfa34102e65fa8e5384801cca67bbe983a142abb;'}
        headers = {'x-l-req-header': '{deviceType: 9}'}

        # 直接带登录态发送请求
        result = self.s.get(message_url, cookies=cookie, headers=headers)
        print(result.text)
        assert result.status_code == 200
        assert json.loads(result.content)['message'] == '成功'

    # 在pytest里，针对一个类方法的teardown为teardown_method,
    # teardown_method作用同unittest里的dearDown()
    def teardown_method(self, method):
        self.s.close()
