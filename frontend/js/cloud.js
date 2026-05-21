const chart = echarts.init(document.getElementById('chart_cloud'));

  const cdata = originData_songyuan.map(val => ({
    ...val,
    textStyle: {
      normal: {
        color: randomColor()
      }
    }
  }));

  
  chart.setOption({
    series: [{
      type: 'wordCloud',
      shape: 'diamond',
      left: 'center',
      top: 'center',
      width: '70%',
      height: '80%',
      right: null,
      bottom: null,
      sizeRange: [12, 60],
      rotationRange: [-90, 90],
      rotationStep: 45,
      gridSize: 8,
      drawOutOfBound: false,
      textStyle: {
        normal: {
          fontFamily: 'sans-serif',
          fontWeight: 'normal'
        },
        emphasis: {
          shadowBlur: 10,
          shadowColor: '#333'
        }
      },
      cdata
    }]
  });

  function randomColor() {
    return 'rgb(' + [
      Math.round(Math.random() * 160),
      Math.round(Math.random() * 160),
      Math.round(Math.random() * 160)
    ].join(',') + ')';
  }