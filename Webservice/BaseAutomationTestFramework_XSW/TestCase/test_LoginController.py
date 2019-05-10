#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import sys
sys.path.append("..")
from TestCase.TestCaseModel import *
from InterfaceManager.LoginController import *

class LoginController(object):
    def test_Integrated_interface(self):
        assert_pass(GetMenuMessage().get_menu_message(-1))
        assert_pass(GetUserHead().get_user_head())
        assert_pass(UnbindPassport().unbind_passport())
        assert_pass(UpdatePassword().update_password(
            UpdatePassword().req_params('96e79218965eb72c92a549dd5a330112', '96e79218965eb72c92a549dd5a330112')))
        assert_pass(GetHeadSettingMenu().get_head_setting_menu())
        assert_pass(SetUserHead().set_user_head('0000','0000'))



if __name__ == '__main__':
    # logging.warning(GetMenuMessage().get_menu_message(-1))

    # logging.warning(UnbindPassport().unbind_passport())
    # logging.warning(UpdatePassword().update_password(
    #     UpdatePassword().req_params('96e79218965eb72c92a549dd5a330112', '96e79218965eb72c92a549dd5a330112')))
    # logging.warning(GetHeadSettingMenu().get_head_setting_menu())
    # logging.warning(GetUserHead().get_user_head())
    # logging.warning(SetUserHead().set_user_head('0000',SetUserHead().req_params('0000')))
    logging.warning(BindPassport().bind_passport(BindPassport().req_params('111111', 'xushenwei', '111111')))
    logging.warning(CheckPassportIsBind().check_passport_is_bind('xushenwei'))

    pass