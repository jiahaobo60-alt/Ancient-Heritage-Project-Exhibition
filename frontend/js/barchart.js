function getBarChart(pname) {
    $.ajax({
        url: BASE_URL+'/api/getBarChart/',
        type: 'POST',
        dataType: 'json',
        data: {
            province: pname,
        },
        async:false,
        success: function (data) {
            window.barChartData = data.results;
        },
        error: function (jqXHR, textStatus, errorThrown) {
            console.log(textStatus, errorThrown);
        }
    });    
}

function findMaxValue(arr) {
    let max = arr[0][0];  // 假设第一个元素为最大值
  
    for (let i = 0; i < arr.length; i++) {
      for (let j = 0; j < arr[i].length; j++) {
        if (arr[i][j] > max) {
          max = arr[i][j];  // 更新最大值
        }
      }
    }
  
    return max;
  }
