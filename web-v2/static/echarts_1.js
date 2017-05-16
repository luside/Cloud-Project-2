//create an 'echarts'
var myChart = echarts.init(document.getElementById('echarts1')); 

//options of the 'echarts'
option = {
    //the title of the chart
    title : {
        text: 'Australia Tweets Emotion Analysis',
        textStyle: {
            color: '#fff'
        },
        x:'center'
    },
    //show tips when move mouse on a data
    tooltip: {
        trigger: 'item',
        formatter: "{b}:<br/>{c} ({d}%)" 
        //{a}: group name (eg.inner-pie), {b}: data name (eg.Positive), {c}: data value (number of tweets), {d}: proportion
    },
    //legend of the chart, clicking the legend will hide/show corresponding data
    legend: {
        orient: 'horizontal',
        y: 'bottom',
        textStyle: {
            color: '#fff'
        },
        data:['Positive','Neutral','Negative'
                //'Morning-Pos','Afternoon-Pos','Night-Pos',
                //'Morning-Neu','Afternoon-Neu','Night-Neu',
                //'Morning-Neg','Afternoon-Neg','Night-Neg'
        ]
    },
    //data group
    series: [
        {
            name:'inner_pie',
            type:'pie',
            selectedMode: 'single',
            radius: [0, '30%'],

            label: {
                normal: {
                    position: 'inner'
                }
            },
            labelLine: {
                normal: {
                    show: false
                }
            },
            color:['rgb(169,74,66)','rgb(202,160,56)','rgb(125,188,153)'],
            data:[
                {value:973620, name:'Positive'},    //value is the number of cooresponding tweets
                {value:1408982, name:'Neutral'},
                {value:354870, name:'Negative'}
            ]
        },
        {
            name:'outter_pie',
            type:'pie',
            radius: ['40%', '55%'],
            color:['rgba(169,74,66,0.5)','rgba(169,74,66,0.7)','rgba(169,74,66,0.9)',
                    'rgba(202,160,56,0.5)','rgba(202,160,56,0.7)','rgba(202,160,56,0.9)',
                    'rgba(125,188,153,0.5)','rgba(125,188,153,0.7)','rgba(125,188,153,0.9)'
                    ],
            data:[
                {value:169541, name:'Morning-Pos'},
                {value:345655, name:'Afternoon-Pos'},
                {value:458424, name:'Night-Pos'},
                {value:278115, name:'Morning-Neu'},
                {value:470946, name:'Afternoon-Neu'},
                {value:659921, name:'Night-Neu'},
                {value:71122, name:'Morning-Neg'},
                {value:117558, name:'Afternoon-Neg'},
                {value:166240, name:'Night-Neg'}
            ]
        }
    ]
};

//set options for the 'echarts'
myChart.setOption(option); 