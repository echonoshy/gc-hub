console.log("程序开始运行");

console.log("定义集合存储数据");
let name_set = new Set();
console.log("开始载入数据");

// 循环变量
var my_loop;
// 下滑延时 500毫秒 网速/加载速度较慢的朋友们最好放慢速度 提高准确性
var r_time = 500;

// 转发数
var forward_num = 1;
let forwardElement = document.getElementsByClassName("forward")[0];
if (forwardElement && forwardElement.innerText.indexOf("万") != -1) {
    forward_num = 10000 * (parseInt(forwardElement.innerText) + 1);
} else if (forwardElement) {
    forward_num = parseInt(forwardElement.innerText);
}

// 下滑
function r() {
    window.scroll(0, 1920 * forward_num);
    // 到底后自动停止下滑 并 抽奖
    if (document.querySelector(".reaction-list__nomore")) {
        // 停止下滑循环
        stop_r();
        // 抽奖函数
        draw();
    }
}

// 停止下滑循环
function stop_r() {
    console.log("停止下滑~");
    clearInterval(my_loop);
}

// 抽奖函数
function draw() {
    // 获取所有反应项
    let reactionItems = document.getElementsByClassName("reaction-item");
    if (!reactionItems || reactionItems.length === 0) {
        console.log("没有找到转发项，无法抽奖。");
        return;
    }

    // 遍历所有反应项
    var len = reactionItems.length;
    for (var i = 0; i < len; i++) {
        let reactionTextElement = reactionItems[i].getElementsByClassName("reaction-item__name")[0];
        if (reactionTextElement && reactionTextElement.innerText.includes("转发了")) {
            // 提取转发用户名并去除多余后缀
            var name = reactionTextElement.innerText.replace("转发了", "").trim();
            name_set.add(name);
        }
    }

    console.log("全部数据加载完毕");
    console.log("总共" + name_set.size + "名转发用户");

    console.log(name_set);
}

// 获取幸运儿
function go(num) {
    for (var i = 0; i < num; i++) {
        // 生成随机数，直接打印中奖者信息
        var lucky_num = parseInt(Math.random() * name_set.size, 10);
        console.log("中奖用户名为:" + Array.from(name_set)[lucky_num]);
        console.log(" ");
    }
}

// 开始自动下滑 r_time毫秒一次
my_loop = setInterval(r, r_time);

// 全部数据加载完毕后，使用 go(中奖数) 抽取中奖者
