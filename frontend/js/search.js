var dataList = document.getElementById('search_list');
var textArea = document.getElementById("search-input");

function findScatterPointByName(scatterName) {
    for (var i = 0; i < scatterdata.length; i++) {
        if (scatterdata[i].name === scatterName) {
            highlightScatterPoint(i);
            console.log(scatterdata[i].name);
            return scatterdata[i].name;
        }
    }
    return null;
}

// 手动高亮指定的散点图点
function highlightScatterPoint(index) {
    scatterMap.dispatchAction({
        type: 'highlight',
        seriesIndex: 0,  // 散点图所在的系列索引
        dataIndex: index  // 要高亮的散点图点的索引
    });
}

// 手动取消高亮指定的散点图点
function downplayScatterPoint(index) {
    scatterMap.dispatchAction({
        type: 'downplay',
        seriesIndex: 0,  // 散点图所在的系列索引
        dataIndex: index  // 要取消高亮的散点图点的索引
    });
}

function search() {
    if (textArea.value) {
        $.ajax({
            url: BASE_URL + '/api/search/',
            type: 'POST',
            dataType: 'json',
            data: {
                input: textArea.value,
            },
            success: function (data) {
                sceneryList = data.results;
                pname = sceneryList[0]["pname"];
                changeMap(pname);
                findScatterPointByName(textArea.value);
                //清空输入框
                textArea.value = "";
            },
            error: function (jqXHR, textStatus, errorThrown) {
                console.log(textStatus, errorThrown);
            }
        });

    } else {
        alert("你尚未输入信息,请重新输入")
    }
}

function updateList(event) {
    var input = event.target;
    var inputValue = input.value.trim();
    $.ajax({
        url: BASE_URL + '/api/updateList/',
        type: 'POST',
        dataType: 'json',
        data: {
            input: inputValue,
        },
        success: function (data) {
            sceneryList = data.results;
            sceneryList.forEach(function (element) {
                // 创建一个新的选项
                var option = document.createElement('option');
                option.value = element.sname;
                // 将选项添加到datalist中
                dataList.appendChild(option);
            })
        },
        error: function (jqXHR, textStatus, errorThrown) {
            console.log(textStatus, errorThrown);
        }
    });
}

function click(sid) {
    $.ajax({
        url: BASE_URL + '/api/click/',
        type: 'POST',
        dataType: 'json',
        data: {
            input: sid,
        },
        success: function (data) {
            scenery = data.results;
            pname = scenery["pname"];
        },
        error: function (jqXHR, textStatus, errorThrown) {
            console.log(textStatus, errorThrown);
        }
    });
    //清空输入框
    textArea.value = "";
    dataList.innerHTML = '';
}