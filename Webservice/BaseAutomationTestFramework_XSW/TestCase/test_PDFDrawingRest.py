#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import sys
sys.path.append("..")
from TestCase.TestCaseModel import *
from InterfaceManager.PDFDrawingRest import *

class PDFDrawingRest(object):
    def test_Integrated_interface(self):
        assert_pass(GetDrawingClassifyInfos().get_drawing_classify_infos())
        assert_pass(GetProjHasPdfDraw().get_proj_has_PDF_draw())
        PDFinfo_resp = GetDrawingDetailInfos().get_drawing_detail_infos(GetDrawingDetailInfos().certain_params())
        assert_pass(PDFinfo_resp)
        PDFinfo = PDFinfo_resp.get('result').get('content')
        if PDFinfo != []:
            classifyId = PDFinfo[0].get('classifyId')
            drawingId = PDFinfo[0].get('drawingId')
            drawingName = PDFinfo[0].get('drawingName')
            ppid = PDFinfo[0].get('ppid')
        else:
            raise Exception('Not find a PDF project!')
        assert_pass(UpdateDrawingInfo().update_drawing_info(
            UpdateDrawingInfo().req_params(classifyId, drawingId, drawingName, 'memotest', ppid)))
        # assert_pass(DelDrawingInfos().delete_drawing_infos(DelDrawingInfos().req_params(0,0)))  # 删除了无法恢复，在集成里面暂时没有想好怎么做



if __name__ == '__main__':
    pytest.main(['test_PDFDrawingRest.py'])
    # logging.warning(GetDrawingDetailInfos().get_drawing_detail_infos(GetDrawingDetailInfos().certain_params()))
    # logging.warning(GetDrawingClassifyInfos().get_drawing_classify_infos())
    # logging.warning(UpdateDrawingInfo().update_drawing_info(UpdateDrawingInfo().req_params(12,14,'神奇宝贝无限奔跑流之神秘图层1100.pdf','memotest',131866)))
    # logging.warning(GetProjHasPdfDraw().get_proj_has_PDF_draw())
    # logging.warning(DelDrawingInfos().delete_drawing_infos(DelDrawingInfos().req_params(0,0)))
    pass