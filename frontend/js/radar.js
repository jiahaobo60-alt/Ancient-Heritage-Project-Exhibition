function getDynastyNum(pname,plist,dataProvince) {
    //获取地点
    // console.log(dataProvince);
    $.ajax({
        url: BASE_URL+'/api/getDynastyNum/',
        type: 'POST',
        dataType: 'json',
        data: {
            province: pname,
        },
        async:false,
        success: function (data) {
            dataProvince.shift();
            dataProvince.push([data.results]);
            plist.shift();
            plist.push(pname);
        },
        error: function (jqXHR, textStatus, errorThrown) {
            console.log(textStatus, errorThrown);
        }
    });    
}

