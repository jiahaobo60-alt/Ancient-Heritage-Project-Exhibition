function getMap(pname) {
    //获取地点
    pointList=[];
    $.ajax({
        url: BASE_URL+'/api/map/',
        type: 'POST',
        dataType: 'json',
        data: {
            province: pname,
        },
        async:false,
        success: function (data) {
            pointList = data.results;
            // console.log(pointList);
            var scList = new Array();
            var scGeo = {};
            for (var i=0;i<pointList.length;i++) {
                // console.log(pointList[i].name);
                scGeo[pointList[i].name] = [pointList[i].longitude,pointList[i].latitude];
                // console.log(scGeo);
                var sc = {};
                sc["name"] = pointList[i].name;
                sc["value"] = Math.floor(Math.random()*200);
                sc["introduction"] = pointList[i].introduction;
                scList.push(sc);
            }
            // console.log(scList);
            scatterVal = scList;
            scatterGeo = scGeo;
        },
        error: function (jqXHR, textStatus, errorThrown) {
            console.log(textStatus, errorThrown);
        }
    });    
}

function getHeatMap(heatmapData) {
    //获取地点
    pointList=[];
    $.ajax({
        url: BASE_URL+'/api/heatMap/',
        type: 'POST',
        dataType: 'json',
        data: {
            token :"token"
        },
        async:false,
        success: function (data) {
            pointList = data.results;
            for (var i=0;i<pointList.length;i++) {
                heatmapData.push({value : [pointList[i].longitude,pointList[i].latitude,10]});
            }
            // console.log(heatmapData);
        },
        error: function (jqXHR, textStatus, errorThrown) {
            console.log(textStatus, errorThrown);
        }
    });    
}

