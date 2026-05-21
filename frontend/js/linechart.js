function getLineChart(pname) {
    $.ajax({
        url: BASE_URL+'/api/getLineChart/',
        type: 'POST',
        dataType: 'json',
        data: {
            province: pname,
        },
        async:false,
        success: function (data) {
            window.lineData = data.results;
        },
        error: function (jqXHR, textStatus, errorThrown) {
            console.log(textStatus, errorThrown);
        }
    });    
}