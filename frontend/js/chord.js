var myChart = echarts.init(document.getElementById('chart_sankey'));

var city = {
    '商周': '#c23531',
    '秦汉': '#2f4554',
    '隋唐': '#6e2e6a',
    '宋元': '#d48265',
    '明清': '#61a0a8',

    '北京': '#c23531',
    '天津': '#2f4554',
    '河北': '#61a0a8',
    '山西': '#d48265',
    '内蒙古': '#749f83',
    '辽宁': '#61a0a8',
    '吉林': '#d48265',
    '黑龙江': '#749f83',
    '上海': '#61a0a8',
    '江苏': '#d48265',
    '浙江': '#749f83',
    '安徽': '#61a0a8',
    '福建': '#d48265',
    '江西': '#74f83',
    '山东': '#61a0a8',
    '河南': '#d48265',
    '湖北': '#74f83',
    '湖南': '#61a0a8',
    '广东': '#d48265',
    '广西': '#74f83',
    '海南': '#c23531',
    '四川': '#2f4554',
    '贵州': '#61a0a8',
    '云南': '#d48265',
    '西藏': '#74f83',
    '重庆': '#c23531',
    '陕西': '#2f4554',
    '甘肃': '#61a0a8',
    '青海': '#d48265',
    '宁夏': '#74f83',
    '新疆': '#c23531',
    '香港': '#2f4554',
    '澳门': '#61a0a8',
}
var population = [
    { 'source': '商周', 'target': '北京', 'value': 2 },
    { 'source': '秦汉', 'target': '北京', 'value': 4 },
    { 'source': '隋唐', 'target': '北京', 'value': 10 },
    { 'source': '宋元', 'target': '北京', 'value': 18 },
    { 'source': '明清', 'target': '北京', 'value': 67 },
    { 'source': '商周', 'target': '天津', 'value': 0 },
    { 'source': '秦汉', 'target': '天津', 'value': 0 },
    { 'source': '隋唐', 'target': '天津', 'value': 0 },
    { 'source': '宋元', 'target': '天津', 'value': 3 },
    { 'source': '明清', 'target': '天津', 'value': 34 },
    { 'source': '商周', 'target': '河北', 'value': 0 },
    { 'source': '秦汉', 'target': '河北', 'value': 2 },
    { 'source': '隋唐', 'target': '河北', 'value': 11 },
    { 'source': '宋元', 'target': '河北', 'value': 23 },
    { 'source': '明清', 'target': '河北', 'value': 94 },
    { 'source': '商周', 'target': '山西', 'value': 2 },
    { 'source': '秦汉', 'target': '山西', 'value': 7 },
    { 'source': '隋唐', 'target': '山西', 'value': 25 },
    { 'source': '宋元', 'target': '山西', 'value': 32 },
    { 'source': '明清', 'target': '山西', 'value': 83 },
    { 'source': '商周', 'target': '内蒙古', 'value': 0 },
    { 'source': '秦汉', 'target': '内蒙古', 'value': 2 },
    { 'source': '隋唐', 'target': '内蒙古', 'value': 4 },
    { 'source': '宋元', 'target': '内蒙古', 'value': 39 },
    { 'source': '明清', 'target': '内蒙古', 'value': 33 },
    { 'source': '商周', 'target': '辽宁', 'value': 1 },
    { 'source': '秦汉', 'target': '辽宁', 'value': 3 },
    { 'source': '隋唐', 'target': '辽宁', 'value': 5 },
    { 'source': '宋元', 'target': '辽宁', 'value': 8 },
    { 'source': '明清', 'target': '辽宁', 'value': 42 },
    { 'source': '商周', 'target': '吉林', 'value': 1 },
    { 'source': '秦汉', 'target': '吉林', 'value': 0 },
    { 'source': '隋唐', 'target': '吉林', 'value': 4 },
    { 'source': '宋元', 'target': '吉林', 'value': 7 },
    { 'source': '明清', 'target': '吉林', 'value': 21 },
    { 'source': '商周', 'target': '黑龙江', 'value': 0 },
    { 'source': '秦汉', 'target': '黑龙江', 'value': 0 },
    { 'source': '隋唐', 'target': '黑龙江', 'value': 0 },
    { 'source': '宋元', 'target': '黑龙江', 'value': 1 },
    { 'source': '明清', 'target': '黑龙江', 'value': 24 },
    { 'source': '商周', 'target': '上海', 'value': 0 },
    { 'source': '秦汉', 'target': '上海', 'value': 2 },
    { 'source': '隋唐', 'target': '上海', 'value': 3 },
    { 'source': '宋元', 'target': '上海', 'value': 6 },
    { 'source': '明清', 'target': '上海', 'value': 53 },
    { 'source': '商周', 'target': '江苏', 'value': 1 },
    { 'source': '秦汉', 'target': '江苏', 'value': 1 },
    { 'source': '隋唐', 'target': '江苏', 'value': 21 },
    { 'source': '宋元', 'target': '江苏', 'value': 21 },
    { 'source': '明清', 'target': '江苏', 'value': 79 },
    { 'source': '商周', 'target': '浙江', 'value': 3 },
    { 'source': '秦汉', 'target': '浙江', 'value': 5 },
    { 'source': '隋唐', 'target': '浙江', 'value': 29 },
    { 'source': '宋元', 'target': '浙江', 'value': 34 },
    { 'source': '明清', 'target': '浙江', 'value': 121 },
    { 'source': '商周', 'target': '安徽', 'value': 1 },
    { 'source': '秦汉', 'target': '安徽', 'value': 6 },
    { 'source': '隋唐', 'target': '安徽', 'value': 5 },
    { 'source': '宋元', 'target': '安徽', 'value': 15 },
    { 'source': '明清', 'target': '安徽', 'value': 53 },
    { 'source': '商周', 'target': '福建', 'value': 1 },
    { 'source': '秦汉', 'target': '福建', 'value': 0 },
    { 'source': '隋唐', 'target': '福建', 'value': 23 },
    { 'source': '宋元', 'target': '福建', 'value': 19 },
    { 'source': '明清', 'target': '福建', 'value': 75 },
    { 'source': '商周', 'target': '江西', 'value': 3 },
    { 'source': '秦汉', 'target': '江西', 'value': 1 },
    { 'source': '隋唐', 'target': '江西', 'value': 15 },
    { 'source': '宋元', 'target': '江西', 'value': 6 },
    { 'source': '明清', 'target': '江西', 'value': 58 },
    { 'source': '商周', 'target': '山东', 'value': 3 },
    { 'source': '秦汉', 'target': '山东', 'value': 6 },
    { 'source': '隋唐', 'target': '山东', 'value': 13 },
    { 'source': '宋元', 'target': '山东', 'value': 11 },
    { 'source': '明清', 'target': '山东', 'value': 77 },
    { 'source': '商周', 'target': '河南', 'value': 1 },
    { 'source': '秦汉', 'target': '河南', 'value': 2 },
    { 'source': '隋唐', 'target': '河南', 'value': 15 },
    { 'source': '宋元', 'target': '河南', 'value': 21 },
    { 'source': '明清', 'target': '河南', 'value': 52 },
    { 'source': '商周', 'target': '湖北', 'value': 1 },
    { 'source': '秦汉', 'target': '湖北', 'value': 3 },
    { 'source': '隋唐', 'target': '湖北', 'value': 18 },
    { 'source': '宋元', 'target': '湖北', 'value': 7 },
    { 'source': '明清', 'target': '湖北', 'value': 71 },
    { 'source': '商周', 'target': '湖南', 'value': 0 },
    { 'source': '秦汉', 'target': '湖南', 'value': 6 },
    { 'source': '隋唐', 'target': '湖南', 'value': 11 },
    { 'source': '宋元', 'target': '湖南', 'value': 16 },
    { 'source': '明清', 'target': '湖南', 'value': 77 },
    { 'source': '商周', 'target': '广东', 'value': 1 },
    { 'source': '秦汉', 'target': '广东', 'value': 3 },
    { 'source': '隋唐', 'target': '广东', 'value': 22 },
    { 'source': '宋元', 'target': '广东', 'value': 22 },
    { 'source': '明清', 'target': '广东', 'value': 90 },
    { 'source': '商周', 'target': '广西', 'value': 0 },
    { 'source': '秦汉', 'target': '广西', 'value': 3 },
    { 'source': '隋唐', 'target': '广西', 'value': 9 },
    { 'source': '宋元', 'target': '广西', 'value': 13 },
    { 'source': '明清', 'target': '广西', 'value': 33 },
    { 'source': '商周', 'target': '海南', 'value': 0 },
    { 'source': '秦汉', 'target': '海南', 'value': 11 },
    { 'source': '隋唐', 'target': '海南', 'value': 5 },
    { 'source': '宋元', 'target': '海南', 'value': 1 },
    { 'source': '明清', 'target': '海南', 'value': 18 },
    { 'source': '商周', 'target': '四川', 'value': 0 },
    { 'source': '秦汉', 'target': '四川', 'value': 4 },
    { 'source': '隋唐', 'target': '四川', 'value': 21 },
    { 'source': '宋元', 'target': '四川', 'value': 20 },
    { 'source': '明清', 'target': '四川', 'value': 73 },
    { 'source': '商周', 'target': '贵州', 'value': 0 },
    { 'source': '秦汉', 'target': '贵州', 'value': 7 },
    { 'source': '隋唐', 'target': '贵州', 'value': 12 },
    { 'source': '宋元', 'target': '贵州', 'value': 17 },
    { 'source': '明清', 'target': '贵州', 'value': 70 },
    { 'source': '商周', 'target': '云南', 'value': 2 },
    { 'source': '秦汉', 'target': '云南', 'value': 0 },
    { 'source': '隋唐', 'target': '云南', 'value': 24 },
    { 'source': '宋元', 'target': '云南', 'value': 23 },
    { 'source': '明清', 'target': '云南', 'value': 61 },
    { 'source': '商周', 'target': '西藏', 'value': 0 },
    { 'source': '秦汉', 'target': '西藏', 'value': 1 },
    { 'source': '隋唐', 'target': '西藏', 'value': 17 },
    { 'source': '宋元', 'target': '西藏', 'value': 37 },
    { 'source': '明清', 'target': '西藏', 'value': 31 },
    { 'source': '商周', 'target': '重庆', 'value': 0 },
    { 'source': '秦汉', 'target': '重庆', 'value': 1 },
    { 'source': '隋唐', 'target': '重庆', 'value': 12 },
    { 'source': '宋元', 'target': '重庆', 'value': 8 },
    { 'source': '明清', 'target': '重庆', 'value': 25 },
    { 'source': '商周', 'target': '陕西', 'value': 2 },
    { 'source': '秦汉', 'target': '陕西', 'value': 6 },
    { 'source': '隋唐', 'target': '陕西', 'value': 22 },
    { 'source': '宋元', 'target': '陕西', 'value': 12 },
    { 'source': '明清', 'target': '陕西', 'value': 38 },
    { 'source': '商周', 'target': '甘肃', 'value': 0 },
    { 'source': '秦汉', 'target': '甘肃', 'value': 3 },
    { 'source': '隋唐', 'target': '甘肃', 'value': 9 },
    { 'source': '宋元', 'target': '甘肃', 'value': 20 },
    { 'source': '明清', 'target': '甘肃', 'value': 36 },
    { 'source': '商周', 'target': '青海', 'value': 1 },
    { 'source': '秦汉', 'target': '青海', 'value': 1 },
    { 'source': '隋唐', 'target': '青海', 'value': 11 },
    { 'source': '宋元', 'target': '青海', 'value': 22 },
    { 'source': '明清', 'target': '青海', 'value': 38 },
    { 'source': '商周', 'target': '宁夏', 'value': 0 },
    { 'source': '秦汉', 'target': '宁夏', 'value': 0 },
    { 'source': '隋唐', 'target': '宁夏', 'value': 5 },
    { 'source': '宋元', 'target': '宁夏', 'value': 6 },
    { 'source': '明清', 'target': '宁夏', 'value': 15 },
    { 'source': '商周', 'target': '新疆', 'value': 0 },
    { 'source': '秦汉', 'target': '新疆', 'value': 3 },
    { 'source': '隋唐', 'target': '新疆', 'value': 11 },
    { 'source': '宋元', 'target': '新疆', 'value': 28 },
    { 'source': '明清', 'target': '新疆', 'value': 65 },
    { 'source': '商周', 'target': '香港', 'value': 1 },
    { 'source': '秦汉', 'target': '香港', 'value': 1 },
    { 'source': '隋唐', 'target': '香港', 'value': 1 },
    { 'source': '宋元', 'target': '香港', 'value': 0 },
    { 'source': '明清', 'target': '香港', 'value': 5 },
    { 'source': '商周', 'target': '澳门', 'value': 0 },
    { 'source': '秦汉', 'target': '澳门', 'value': 0 },
    { 'source': '隋唐', 'target': '澳门', 'value': 2 },
    { 'source': '宋元', 'target': '澳门', 'value': 0 },
    { 'source': '明清', 'target': '澳门', 'value': 6 },
];

var nodeLinkCounts = {};
// Initialize counts for each node
for (var key in city) {
    nodeLinkCounts[key] = 0;
}

// Calculate total value for each node
for (var i = 0; i < population.length; i++) {
    nodeLinkCounts[population[i].source] += population[i].value;
    // 只累加target节点的incoming links，避免重复计算用于symbolSize
    if (nodeLinkCounts[population[i].target] !== undefined) {
        nodeLinkCounts[population[i].target] += population[i].value;
    }
}

var data = [];
var citylist = [];

// Separate dynasties and provinces
var dynasties = ['商周', '秦汉', '隋唐', '宋元', '明清'];
var provincesAndOthers = [];

for (var key in city) {
    var size;
    if (dynasties.includes(key)) {
        // 朝代节点使用较小的缩放比例
        size = Math.max(8, nodeLinkCounts[key] / 30);
    } else {
        // 省份节点使用较大的缩放比例
        size = Math.max(12, nodeLinkCounts[key] / 15);
    }
    var node = { name: key, itemStyle: { color: city[key] }, symbolSize: size };
    if (dynasties.includes(key)) {
        citylist.push(node); // Add dynasties first
    } else {
        provincesAndOthers.push(node); // Add provinces and others separately
    }
}

// Append provinces and others to citylist
citylist = citylist.concat(provincesAndOthers);

for (var i = 0; i < population.length; i++) {
    data.push(
        {
            source: population[i].source,
            target: population[i].target,
            value: population[i].value,
            lineStyle: {
                color: city[population[i].source],
                width: Math.max(0.5, population[i].value / 8),
                opacity: 0.7
            }
        }
    )
}


// 和弦图配置
option = {
    title: {
        text: '省份非遗统计和弦图',
        top: 'top',
        left: 'center',
        textStyle: {
            fontFamily: 'FZQKBYSJW',
            fontSize: 20
        }
    },
    tooltip: {
        trigger: 'item',
        triggerOn: 'mousemove',
        formatter: function (params) {
            if (params.data.source && params.data.target) { // Link tooltip
                return params.data.source + ' -> ' + params.data.target + ': ' + params.data.value;
            } else { // Node tooltip
                return params.name;
            }
        },
        textStyle: {
            fontFamily: 'FZQKBYSJW'
        }
    },
    series: [
        {
            type: 'graph',
            layout: 'circular',
            circular: {
                rotateLabel: true
            },
            radius: '90%',
            data: citylist,
            links: data,
            roam: true,
            label: {
                show: true,
                position: 'right',
                formatter: function(params) {
                    // 判断是否为朝代节点
                    if (dynasties.includes(params.name)) {
                        return '{a|' + params.name + '}';
                    }
                    return params.name;
                },
                rich: {
                    a: {
                        fontSize: 16,
                        fontWeight: 'bold',
                        fontFamily: 'FZQKBYSJW',  // 使用方正字体
                        color: '#8B0000'  // 使用酒红色
                    }
                },
                color: '#000'
            },
            lineStyle: {
                curveness: 0.3
            },
            emphasis: {
                lineStyle: {
                    opacity: 0.9
                }
            }
        }
    ]
};

myChart.setOption(option);