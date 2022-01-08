module.exports = {
    "id": "tqyb",
    "name": "天气预报极速版",
    "keys": ["tqyburl","tqyburl2","tqyburl3","tqyburl4","tqyburl5"],
    "author": "@tom",
    "settings": [{
      "id": "tqybSuffix",
      "name": "当前账号",
      "val": "1",
      "type": "number",
      "desc": "当前抓取ck记录的账号序号，如：1、2、3、4"
    }, {
      "id": "tqybCount",
      "name": "账号个数",
      "val": "1",
      "type": "number",
      "desc": "指定任务最多跑几个账号，根据抓取的账号数据个数来设值"
    }, {
      "id": "tqybXH",
      "name": "循环获取ck",
      "val": "0",
      "type": "number",
      "desc": "0关闭，1打开，默认关闭"
    }, {
      "id": "tqybTXTX",
      "name": "txtx",
      "val": "0",
      "type": "number",
      "desc": "0关闭，1打开，默认关闭"
    }, {
      "id": "tqybSC",
      "name": "sc",
      "val": "0",
      "type": "number",
      "desc": "0关闭，1打开，默认关闭"
    }, {
      "id": "tqybnotifyttt",
      "name": "推送控制",
      "val": "1",
      "type": "number",
      "desc": "0关闭，1推送,默认12点以及23点推送"
    }, {
      "id": "tqybnotifyInterval",
      "name": "通知控制",
      "val": "2",
      "type": "number",
      "desc": "0关闭，1为 所有通知，2为 12，23 点通知，3为 6，12，18，23 点通知"
    }, {
      "id": "tqybMinutes",
      "name": "推送-通知 分钟控制",
      "val": "10",
      "type": "number",
      "desc": "推送以及通知控制在什么分钟段，可设置0-59,默认0到10"
    }],
    "repo": "https://raw.githubusercontent.com/xl2101200/-/main/tqyb.js",
    "icons": ["https://raw.githubusercontent.com/xl2101200/-/main/tom/tom.jpg", "https://raw.githubusercontent.com/xl2101200/-/main/tom/tom.jpg"],
    "script": "https://raw.githubusercontent.com/xl2101200/-/main/tqyb.js",
    "icon": "https://raw.githubusercontent.com/xl2101200/-/main/tom/tom.jpg",
    "favIcon": "mdi-star-outline",
    "favIconColor": "grey",
    "datas": [{
      "key": "tqyburl",
      "val": "http://coin.makingmoney.cn:8088/task/coin?guid=UUID-3282B11C-AAB1-4157-8321-0D1965A4B41B&ver=1.3.0&systemver=14.2&bid=com.swx.weather.app&mt=1&sw=414&sh=736&device=iPhone&idiom=0&chl=AppStore&language=zh-Hans-CN&locale=CN&zone=Asia%2FShanghai&timestamp=1641615230&idfv=0338DDAA-AFDE-4380-8147-28E19CA9E0E3&sign=2a45b38d46b962d37b6c8b6fef9cd97a"
    }, {
      "key": "tqyburl2",
      "val": ""
    }],
    "sessions": [],
    "isLoaded": true
  }
