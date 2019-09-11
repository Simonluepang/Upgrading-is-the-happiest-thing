export function getUrlParams(name) {
  let search = window.location.search.substr(1);
  let result;
  if (name) {
    let reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)");
    var r = search.match(reg);
    result = "";
    if (r != null) {
      result = unescape(r[2]);
    }
  } else {
    result = {};
    if (search) {
      let paramsArr = search.split('&');
      for (let item of paramsArr) {
        let itemArr = item.split('=');
        result[itemArr[0]] = unescape(itemArr[1]);
      }
    }
  }
  return result
}
