import {mockRequest,Request} from '../utils/request'
import { mockData } from '../utils/mockData'

export const getFormData = (id) => {
    // return mockRequest(mockData)
    let data = {
        // id:"2019070814305313801337a4af76831c",
        id:id,
        update_timestamp:new Date().getTime()
    }
    return mockRequest(mockData)
    // return mockRequest(mockData) medicalrecord/getmedicalrecorddata
    // Request('get','medicalrecord/getmedicalrecorddata',data)
    // return Request('get','DocumentTemplate/GetMedicalRecordTemplate',data)
}

export const getPublicitemData = data => {
    return Request('get','/api/GetScriptData',data)
}