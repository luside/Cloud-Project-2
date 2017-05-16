//create an 'echarts'
var myChart = echarts.init(document.getElementById('echarts2'));  
//data of Australia [weekday, average emotion score, number of tweets, population]
var dataAU = [
    ['Mon',0.20264196519239885,189655,23130900],
    ['Tue',0.2091233444273198,190207,23130900],
    ['Wed',0.2166330989667821,193514,23130900],
    ['Thu',0.21628758856093092,190508,23130900],
    ['Fri',0.21919666729301682,183640,23130900],
    ['Sat',0.2235872945901822,191546,23130900],
    ['Sun',0.219374576093033,189470,23130900]
];
//data of Melbourne
var dataMel = [
    ['Mon',0.16126598567415493,23035,4181021],
    ['Tue',0.16976980005283762,24901,4181021],
    ['Wed',0.16742338643764124,26011,4181021],
    ['Thu',0.17868889307450744,24772,4181021],
    ['Fri',0.17406912076248418,23328,4181021],
    ['Sat',0.18877095676507824,24233,4181021],
    ['Sun',0.18277773084239685,23686,4181021]
];
var dataSyd = [
    ['Mon',0.2069946930088568,121084,4373433],
    ['Tue',0.21607307271614748,119285,4373433],
    ['Wed',0.2244760351873809,121274,4373433],
    ['Thu',0.22299764159566685,119268,4373433],
    ['Fri',0.22435211881095246,113943,4373433],
    ['Sat',0.23130352190030856,118527,4373433],
    ['Sun',0.22485662917142063,117865,4373433]
];
var dataPer = [
    ['Mon',0.19926327410056266,21725,1901582],
    ['Tue',0.2018393586246498,21345,1901582],
    ['Wed',0.21077261808120204,22478,1901582],
    ['Thu',0.19942769499919133,22032,1901582],
    ['Fri',0.2134954663203098,21764,1901582],
    ['Sat',0.20424820659473414,24285,1901582],
    ['Sun',0.21881799277124359,24101,1901582]
];
var dataBri = [
    ['Mon',0.2691757600403022,3651,2143121],
    ['Tue',0.27081599697534875,3728,2143121],
    ['Wed',0.27102107463400804,3957,2143121],
    ['Thu',0.2662163939124113,3677,2143121],
    ['Fri',0.2724982734866124,3861,2143121],
    ['Sat',0.2806925275109998,4081,2143121],
    ['Sun',0.27121914276317316,4033,2143121]
];
var dataAde = [
    ['Mon',0.19710102069671798,7835,1263888],
    ['Tue',0.20156137356728782,8351,1263888],
    ['Wed',0.22322813906323408,7890,1263888],
    ['Thu',0.21190149996776295,7812,1263888],
    ['Fri',0.22088844553567138,8068,1263888],
    ['Sat',0.21048229798268847,7556,1263888],
    ['Sun',0.20339934471361046,7854,1263888]
];
var dataCan = [
    ['Mon',0.17799032160908476,1170,418856],
    ['Tue',0.20530834532473946,1018,418856],
    ['Wed',0.20379505508698154,1121,418856],
    ['Thu',0.1929661973556363,1105,418856],
    ['Fri',0.21495840748740752,954,418856],
    ['Sat',0.22409903052010044,945,418856],
    ['Sun',0.21365174103938164,1042,418856]
];

//style of each point on the 'echarts'
var itemStyle = {
    normal: {
        opacity: 0.8,
        shadowBlur: 10,
        shadowOffsetX: 0,
        shadowOffsetY: 0,
        shadowColor: 'rgba(0, 0, 0, 0.5)'
    }
};

//option of the 'echarts'
option = {
    //legend of the chart, clicking the legend will hide/show corresponding data
    legend: {
        y: 'top',
        data: ['AU', 'Mel', 'Syd','Per','Bri','Ade','Can'],
        textStyle: {
            color: '#fff',
            fontSize: 16
        }
    },
    //show tips when move mouse on a data
    tooltip: {
        formatter: function (obj) {
            var value = obj.value;
            return obj.seriesName +' '+ value[0] + '<br/>' + 'Score: '+ value[1] 
            + '<br/>' + 'Tweets: ' + value[2] + '<br/>' + 'Population: '+ value[3]
            + '<br/>' + 'Tweet desire: '+ Math.round(value[2]/value[3]*10000)/100+' %';
         }
    },
    //x xxis of the chart
    xAxis: {
        name: 'Time',
        data:['Mon','Tue','Wed','Thu','Fri','Sat','Sun'],
        nameTextStyle: {
            color: '#fff',
            fontSize: 14
        },
        axisLine: {
            lineStyle: {
                color: '#eee'
            }
        }
    },
    //y axis of the chart
    yAxis: {
        type: 'value',
        name: 'Score',
        nameLocation: 'end',
        min:0.15,
        nameTextStyle: {
            color: '#fff',
            fontSize: 16
        },
        axisLine: {
            lineStyle: {
                color: '#eee'
            }
        },
        splitLine: {
            show: false
        }
    },
    //date group
    series: [
        {
            name: 'Syd',
            type: 'scatter',
            itemStyle: itemStyle,
            symbolSize: function (data) {
                return Math.sqrt(data[2]/data[3])*200;
            },
            data: dataSyd
        },
        {
            name: 'AU',
            type: 'scatter',
            itemStyle: itemStyle,
            symbolSize: function (data) {  //size of points in this group
                return Math.sqrt(data[2]/data[3])*200;  //scale up for better visual effects.
            },
            data: dataAU
        },
        {
            name: 'Mel',
            type: 'scatter',
            itemStyle: itemStyle,
            symbolSize: function (data) {
                return Math.sqrt(data[2]/data[3])*200;
            },
            data: dataMel
        },
        {
            name: 'Per',
            type: 'scatter',
            itemStyle: itemStyle,
            symbolSize: function (data) {
                return Math.sqrt(data[2]/data[3])*200;
            },
            data: dataPer
        },
        {
            name: 'Bri',
            type: 'scatter',
            itemStyle: itemStyle,
            symbolSize: function (data) {
                return Math.sqrt(data[2]/data[3])*200;
            },
            data: dataBri
        },
        {
            name: 'Ade',
            type: 'scatter',
            itemStyle: itemStyle,
            symbolSize: function (data) {
                return Math.sqrt(data[2]/data[3])*200;
            },
            data: dataAde
        },
        {
            name: 'Can',
            type: 'scatter',
            itemStyle: itemStyle,
            symbolSize: function (data) {
                return Math.sqrt(data[2]/data[3])*200;
            },
            data: dataCan
        }
    ]
};
//set options for the 'echarts'
myChart.setOption(option); 