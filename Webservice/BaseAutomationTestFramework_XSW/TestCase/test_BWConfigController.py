#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import sys
sys.path.append("..")
from TestCase.TestCaseModel import *
from InterfaceManager.BWConfigController import *
from InterfaceManager.BimRest import GetProject


class BWConfigController(object):
    # 原BW的Center接口都走不通
    def test_Integrated_interface(self):
        '''原BW集成接口'''
        # 获取第一个工程的projectId
        projectId = GetProject().get_project(GetProject().find_all_params()).get('result').get('content')[0].get(
            'projId')
        assert_pass(UpdatePermissions().update_permission(projectId,'xushenwei'))
        assert_pass(CheckProjectsFile().check_projects_file(projectId))
        assert_pass(CheckRecyclesFile().check_recycles_file(projectId))
        assert_pass(ListProjectLib().list_project_lib())
        assert_pass(ListProjectMajor().list_project_major(projectId))
        assert_pass(ListRecycles().list_recycles())
        assert_pass(ListCompletesMajors().list_complete_majors(projectId))
        assert_pass(ListComplete().list_complete())
        assert_pass(ListRecyclesMajors().list_recycles_majors(projectId))
        assert_pass(CheckCompletesFile().check_completes_file(projectId))
        assert_pass(CheckPermissions().check_permissions(projectId))


if __name__ == "__main__":
    projectId = GetProject().get_project(GetProject().find_all_params()).get('result').get('content')[0].get(
        'projId')
    logging.warning(UpdatePermissions().update_permission(projectId, 'xushenwei'))
    logging.warning(CheckProjectsFile().check_projects_file(projectId))
    logging.warning(CheckRecyclesFile().check_recycles_file(projectId))
    logging.warning(ListProjectLib().list_project_lib())
    logging.warning(ListProjectMajor().list_project_major(projectId))
    logging.warning(ListRecycles().list_recycles())
    logging.warning(ListCompletesMajors().list_complete_majors(projectId))
    logging.warning(ListComplete().list_complete())
    logging.warning(ListRecyclesMajors().list_recycles_majors(projectId))
    logging.warning(CheckCompletesFile().check_completes_file(projectId))
    logging.warning(CheckPermissions().check_permissions(projectId))

    pytest.main(['test_BWConfigController.py'])
    pass