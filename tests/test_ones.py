# -*- coding: utf-8 -*-

import pytest

from pages.ones import OneAI


class TestOneAI:
    @pytest.mark.parametrize('login_data, project_name, target_page', [({"password": "iTesting", "email": "pleaseFollowiTesting@outlook.com"}, {"project_name":"VIPTEST"}, {"target_page": "https://ones.ai/project/#/home/project"})])
    def test_merge_api_ui(self, login_data, project_name, target_page):
        one_page = OneAI(login_data, target_page)
        actual_project_name = one_page.get_project_name()
        assert actual_project_name == project_name["project_name"]
