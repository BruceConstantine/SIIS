/**
 * Created by lvhuiyang on 16-12-27.
 */
$(document).ready(function () {
    $("#create_chart").click(function () {
        var count_stu = $("#count_stu").text();
        var count_class = $("#count_class").text();
        var count_major = $("#count_major").text();
        // alert(count_stu + '\n' + count_class + '\n' + count_major);
        chart(count_stu, count_class, count_major);
    });
});


function chart(count_stu, count_class, count_major) {
    // 基于准备好的dom，初始化echarts实例
    var myChart = echarts.init(document.getElementById('chart_area'));

    // 指定图表的配置项和数据
    var option = {
        title: {
            text: '信息统计'
        },
        tooltip: {},
        legend: {
            data: ['数量']
        },
        xAxis: {
            data: ["专业数量", "班级数量", "学生数量"]
        },
        yAxis: {},
        series: [{
            name: '信息统计数量',
            type: 'bar',
            data: [count_major, count_class, 1000]
        }]
    };

    // 使用刚指定的配置项和数据显示图表。
    myChart.setOption(option);
}