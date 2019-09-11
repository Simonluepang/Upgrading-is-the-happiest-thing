import {Request,Upload} from '../utils/request'

//获取诊断接口
export const getZDLst = params =>
  Request(`post`, ``, params);
//获取措施接口
export const getCSLst = params =>
  Request(`post`, ``, params);

//获取相关因素接口
export const getYSLst = params =>
  Request(`post`, ``, params);
//获取症状特性接口
export const getZZLst = params =>
  Request(`post`, ``, params);
//获取目标接口
export const getMBLst = params =>
  Request(`post`, ``, params);
//获取频次接口
export const getPCLst = params =>
  Request(`post`, ``, params);
//上传图片
export const UploadFile = params =>
  Upload("", params);

