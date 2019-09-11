import axios from "axios";
import qs from "qs";
import cookies from './js.cookie'
const baseApi = {
    thirdProd:'',
    thirdDev:'',
    prod:'',
    dev:'dev'
};
const NODE_ENV = process.env.NODE_ENV;
// import store from "vuex"
// import { router } from '@/core/app'
// axios 配置
// axios.defaults.baseURL = NODE_ENV === "production" ? baseApi.prod : baseApi.dev;
axios.defaults.timeout = 20000;
axios.defaults.withCredentials = true;
axios.defaults.headers.common["X-Requested-With"] = "XMLHttpRequest";
// POST传参序列化
axios.interceptors.request.use(
    config => {
        // 单个网站的admin用户
        config.headers.common["Gw-Admin-Access-Token"] = "";
        // 整个网点user
        config.headers.common["Gw-User-Access-Token"] = "";

      /*  let token=getToken();
        config.headers["Authorization"] = token;
        config.headers["platform"] = 1;*/
        return config;
    },
    err => {
        // Message.error("参数错误");
        return Promise.reject(err);
    }
);
// 返回状态判断
axios.interceptors.response.use(
    res => {
        const response = res.data;
        if (response.msg) {
            if (response.code === 0) {
                // Message.success(response.msg);
            } else if (response.code) {
                // Message.error(response.msg);
            } else {
            }
        }
        return response;
    },
    err => {
        if (err && err.response) {
            switch (err.response.status) {
                case 401:
                   /* // Message.error("未授权，请登录");
                    removeToken();
                    // window.location.href = "#/login/pwdlogin";
                    let nowpath=router.history.current.fullPath;
                    if(nowpath.indexOf("login")>-1||curpath.indexOf("common")> -1 ||curpath.indexOf("error") > -1){

                    }else {
                        router.replace("/login/pwdlogin");
                    }*/
                    break;
                case 404:
                    // router.push("/error")
                    break;
                case 504:
                    // router.push("/error")
                    break;
                case 500:
                    // router.push("/error")
                    break;
                default:
                // Message.error("Oops, 出错啦");
            }
        }
        return Promise.resolve(err);
        // return Promise.reject(err);
    }
);
export const Request = (method, url, data, isForm=false) => {
    // 处理请求的url和数据
    if (method === "get") {
        data = { params: data };
    } else {
        if (isForm) {
            data = qs.stringify(data);
        } else {
            data = data;
        }
    }
    axios.defaults.baseURL = NODE_ENV === "production" ? baseApi.prod : baseApi.dev;
    // 发送请求
    return new Promise((resolve, reject) => {
        let sty = {};
        if (isForm) {
            sty.headers = {
                "Content-Type": "application/x-www-form-urlencoded"
            };
        } else {
            sty.headers = {
                "Content-Type": "application/json;charset=utf-8"
            };
        }
        axios[method](url, data, sty)
            .then(
                response => {
                    resolve(response);
                },
            )
    })
};
export const Upload = (url, data) => {
    // 发送请求
    return new Promise((resolve, reject) => {

        let sty = {};
        sty.headers = {
            "Content-Type": "multipart/form-data"
        };
        axios.defaults.baseURL = NODE_ENV === "production" ? baseApi.prod : baseApi.dev;
        axios.post(url, data)
            .then(
                response => {
                    resolve(response);
                },
            )
    })
};

export const mockRequest = (data) => {
    return new Promise((res,rej) => {
        setTimeout(() => {
            res(data);
        },300)
    })
}
