document.addEventListener('DOMContentLoaded', function() {
// 初始化echarts实例
var timelineChart = echarts.init(document.getElementById('timeline-chart'));

// 定义时间轴数据
var years = ['2018', '2019', '2020', '2021', '2022', '2023'];

// 定义分类数据
var categories = ['民间文学', '传统音乐', '传统舞蹈', '传统戏剧', '传统技艺', '传统美术', '传统医药', '民俗'];

// 默认数据 (已修改以显示不同的趋势)
var defaultData = [
    [120, 132, 101, 134, 90, 230], // 民间文学 (保持不变)
    [220, 182, 191, 234, 290, 330], // 传统音乐 (保持不变)
    [150, 232, 201, 154, 190, 330], // 传统舞蹈 (保持不变)
    [320, 332, 301, 334, 390, 330], // 传统戏剧 (保持不变)
    [180, 250, 210, 280, 310, 380], // 传统技艺 (修改为新的趋势数据)
    [100, 150, 130, 180, 220, 280], // 传统美术 (修改为新的趋势数据)
    [250, 280, 260, 300, 340, 400], // 传统医药 (修改为新的趋势数据)
    [80, 110, 90, 120, 150, 200]   // 民俗 (修改为新的趋势数据)
];

// 获取真实数据
function getTimelineData() {
    $.ajax({
        url: 'getLineChart',
        type: 'GET',
        data: {
            pname: typeof pname !== 'undefined' ? pname : '中国'
        },
        success: function(data) {
            console.log('lineData:', data);
            if (data && data.length > 0) {
                updateTimelineChart(data);
            } else {
                console.log('使用默认数据');
                updateTimelineChart(defaultData);
            }
        },
        error: function(err) {
            console.log('折线图数据请求失败，使用默认数据');
            updateTimelineChart(defaultData);
        }
    });
}

// 更新图表
function updateTimelineChart(data) {
    var option = {
        animation: true,
        animationDuration: 3000,  // 动画持续时间，单位毫秒
        animationEasing: 'cubicInOut',  // 动画缓动效果
        animationThreshold: 2000,  // 动画阈值，当单个系列显示的图形数量大于这个阈值时会关闭动画
        title: {
            text: '非遗项目年度增长趋势',
            textStyle: {
                color: '#ffffff',
                fontFamily: 'FZQKBYSJW',
                fontSize: 16,
                textBorderColor: '#000',
                textBorderWidth: 2
            },
            left: 'center'
        },
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'cross',
                label: {
                    backgroundColor: '#6a7985'
                }
            },
            textStyle: {
                fontFamily: 'FZQKBYSJW',
                textBorderColor: '#000',
                textBorderWidth: 1
            }
        },
        legend: {
            data: categories,
            textStyle: {
                color: '#ffffff',
                fontFamily: 'FZQKBYSJW',
                textBorderColor: '#000',
                textBorderWidth: 2
            },
            top: 30
        },
        grid: {
            left: '3%',
            right: '4%',
            top:'30%',
            bottom: '0%',  
            containLabel: true
        },
        xAxis: {
            type: 'category',
            boundaryGap: false,
            data: years,
            axisLine: {
                lineStyle: {
                    color: '#ffffff'
                }
            },
            axisLabel: {
                color: '#ffffff',
                fontFamily: 'FZQKBYSJW',
                textBorderColor: '#000',
                textBorderWidth: 2
            }
        },
        yAxis: {
            type: 'value',
            axisLine: {
                lineStyle: {
                    color: '#ffffff'
                }
            },
            axisLabel: {
                color: '#ffffff',
                fontFamily: 'FZQKBYSJW',
                textBorderColor: '#000',
                textBorderWidth: 2
            },
            splitLine: {
                lineStyle: {
                    color: 'rgba(255,255,255,0.1)'
                }
            },
            min: 0,
            max: 400,
            interval: 100
        },
        series: categories.map((category, index) => ({
            name: category,
            type: 'line',
            smooth: true,
            lineStyle: {
                width: 2
            },
            showSymbol: true,
            symbolSize: 6,
            emphasis: {
                focus: 'series'
            },
            data: data[index] || []
        }))
    };
    
    timelineChart.setOption(option);
}

// 初始化时获取数据
getTimelineData();

// 响应式调整
window.addEventListener('resize', function() {
    timelineChart.resize();
});
}); 