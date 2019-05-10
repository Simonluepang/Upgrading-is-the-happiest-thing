#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import sys
sys.path.append("..")
from TestCase.TestCaseModel import *
from InterfaceManager.CommonController import *

class CommonController(object):
    def test_Integrated_interface(self):
        '''CommonController集成接口'''
        assert_pass(GetUserRealName().get_user_realname(GetUserRealName().req_params(LoginConfig['epid'],'xushenwei')))
        assert_pass(GetApplyUploadUrl().get_apply_upload_url(GetApplyUploadUrl().req_params('string',0)))
        assert_pass(UploadHead().upload_head(UploadHead().req_params('a12','a12')))
        assert_pass(UploadAttachFile().upload_attach_file('TestUploadLib.xlsx'))
        assert_pass(GetFeedBackType().get_feed_bacd_type(888))
        assert_pass(AddFeedBack().add_feed_back(AddFeedBack().certain_params()))
        assert RemizGetAccessCode().get_access_code(
            RemizGetAccessCode().req_params(LoginConfig['epid'], '96e79218965eb72c92a549dd5a330112', 'xushenwei')).get(
            'type') == 'success'
        assert RemizCenterVerification().center_verification(
            RemizCenterVerification().req_params('96e79218965eb72c92a549dd5a330112', 'xushenwei',
                                                 LoginConfig['epid'])).get('type') == 'success'





if __name__ == '__main__':
    # logging.warning(GetUserRealName().get_user_realname(GetUserRealName().req_params(LoginConfig['epid'],'xushenwei')))
    # logging.warning(GetApplyUploadUrl().get_apply_upload_url(GetApplyUploadUrl().req_params('string',0)))
    # logging.warning(UploadHead().upload_head(UploadHead().req_params('a12','a12')))
    # logging.warning(UploadAttachFile().upload_attach_file('TestUploadLib.xlsx'))
    # logging.warning(GetFeedBackType().get_feed_bacd_type(888))
    # logging.warning(AddFeedBack().add_feed_back(AddFeedBack().certain_params()))
    #
    # logging.warning(RemizGetAccessCode().get_access_code(
    #     RemizGetAccessCode().req_params(LoginConfig['epid'], '96e79218965eb72c92a549dd5a330112', 'xushenwei')))
    # logging.warning(RemizCenterVerification().center_verification(
    #     RemizCenterVerification().req_params('96e79218965eb72c92a549dd5a330112', 'xushenwei', LoginConfig['epid'])))

    pytest.main(['test_CommonController.py'])
    pass