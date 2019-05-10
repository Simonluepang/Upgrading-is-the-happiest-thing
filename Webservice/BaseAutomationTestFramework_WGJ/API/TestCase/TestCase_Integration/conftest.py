#coding=utf-8
import pytest

from API.Public.AssertFunction import *


@pytest.fixture(scope="module")
def teardown_module():
    yield
    createInterfacePerformance()
    checkAPICoverageRate()


if __name__ == '__main__':
    teardown_module()