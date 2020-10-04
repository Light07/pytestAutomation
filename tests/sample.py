import json

import pytest
@pytest.mark.smoke
class Sample(object):
    def test_equal(self):
        assert 1 == 0

    def not_equal(self):
        assert 1 != 0



if __name__ == "__main__":
    x = [({"password": "P@ssw0rd", "email": "testertalk@outlook.com"}), ({"project_name":"VIPTEST"})]
    for i in x:
        print(type(i))