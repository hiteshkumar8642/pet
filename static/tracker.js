$(function() {

  var gaugeOptions = {

    chart: {
      type: 'solidgauge'
    },

    title: null,

    pane: {
      center: ['50%', '85%'],
      size: '140%',
      startAngle: -90,
      endAngle: 90,
      background: {
        backgroundColor: (Highcharts.theme && Highcharts.theme.background2) || '#EEE',
        innerRadius: '60%',
        outerRadius: '100%',
        shape: 'arc'
      }
    },

    tooltip: {
      enabled: false
    },

    // the value axis
    yAxis: {
      stops: [
        [0.1, '#55BF3B'], // green
        [0.5, '#DDDF0D'], // yellow
        [0.9, '#DF5353'] // red
      ],
      lineWidth: 0,
      minorTickInterval: null,
      tickPixelInterval: 400,
      tickWidth: 0,
      title: {
        y: -70
      },
      labels: {
        y: 16
      }
    },

    plotOptions: {
      solidgauge: {
        dataLabels: {
          y: 5,
          borderWidth: 0,
          useHTML: true
        }
      }
    }
  };

  // The speed gauge
  $('#container-speed').highcharts(Highcharts.merge(gaugeOptions, {
    yAxis: {
      min: 0,
      max: 200,
      title: {
        text: 'Weight'
      }
    },

    credits: {
      enabled: false
    },

    series: [{
      name: 'Speed',
      data: [80],
      dataLabels: {
        format: '<div style="text-align:center"><span style="font-size:25px;color:' +
          ((Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black') + '">{y}</span><br/>' +
          '<span style="font-size:12px;color:silver">lbs</span></div>'
      },
      tooltip: {
        valueSuffix: ' lbs'
      }
    }]

  }));

  // The RPM gauge
  $('#container-rpm').highcharts(Highcharts.merge(gaugeOptions, {
    yAxis: {
      min: 0,
      max: 100,
      title: {
        text: 'Pet Age'
      }
    },

    series: [{
      name: 'RPM',
      data: [15],
      dataLabels: {
        format: '<div style="text-align:center"><span style="font-size:25px;color:' +
          ((Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black') + '">{y:.1f}</span><br/>' +
          '<span style="font-size:12px;color:silver">Human Years</span></div>'
      },
      tooltip: {
        valueSuffix: ' Human Age'
      }
    }]

  }));
  // The Excercise Gauge
  $('#container-excercise').highcharts(Highcharts.merge(gaugeOptions, {
    yAxis: {
      min: 0,
      max: 25,
      title: {
        text: 'Pet Age'
      }
    },

    series: [{
      name: 'RPM',
      data: [1],
      dataLabels: {
        format: '<div style="text-align:center"><span style="font-size:25px;color:' +
          ((Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black') + '">{y:.1f}</span><br/>' +
          '<span style="font-size:12px;color:silver">* 1000 / min</span></div>'
      },
      tooltip: {
        valueSuffix: ' Dog age'
      }
    }]

  }));


  $('#petfood').highcharts({
    chart: {
      plotBackgroundColor: null,
      plotBorderWidth: null,
      plotShadow: false,
      type: 'pie'
    },
    title: {
      text: 'Pet Food Composition'
    },
    tooltip: {
      pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
    },
    plotOptions: {
      pie: {
        allowPointSelect: true,
        cursor: 'pointer',
        dataLabels: {
          enabled: true,
          format: '<b>{point.name}</b>: {point.percentage:.1f} %',
          style: {
            color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
          }
        }
      }
    },
    series: [{
      name: "Brands",
      colorByPoint: true,
      data: [{
        name: "Carbs",
        y: 49
      }, {
        name: "Fats",
        y: 19,
        sliced: true,
        selected: true
      }, {
        name: "Proteins",
        y: 30
      }, ]
    }]
  });
  // Pet Weight Chart
  $('#petweight').highcharts({
    title: {
      text: '<span style="font-size: 1.3em;">Pet Weight History</span>',
      x: -300 //center
    },
    subtitle: {
      text: 'Consult your vetranarian for your specific ideals',
      x: -20
    },
    xAxis: {
      categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
        'Jul', 'Aug',
      ]
    },
    yAxis: {
      title: {
        text: 'Weight (lbs)'
      },
      plotLines: [{
        value: 0,
        min: 0,
        max: 80,
        width: 1,
        color: '#808080'
      }]
    },
    tooltip: {
      valueSuffix: 'lbs'
    },
    legend: {
      layout: 'vertical',
      align: 'right',
      verticalAlign: 'middle',
      borderWidth: 0
    },
    series: [{
      name: 'Pet Weight',
      data: [58, 56, 55, 54, 56, 55, 57, 55]
    }]

  });
});
