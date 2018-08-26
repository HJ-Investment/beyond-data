<!-- <style lang="less" scoped>
    @import '../../styles/common.less';
</style> -->

<template>
    <div>
        <!-- <Row>
            <Col span="12">
                <DatePicker @on-change="changeDateTime" :value=date_value type="date" placeholder="Select date" style="width: 200px"></DatePicker>
            </Col>
        </Row> -->
        <Row class="margin-top-10">
            <Card>
                <h4 slot="title">
                    <!-- <Icon type="ios-analytics-outline"></Icon> -->
                    <Collapse v-model="analysisaccordionvalue" >
                        <Panel name="1">
                            【行业板块】上涨TOP10在最近8周的表现
                            <div slot="content" id='eastmoney-hybk-up-charts' :style="{height: '900px'}"></div>
                        </Panel>
                        <Panel name="2">
                            【行业板块】下跌TOP10在最近8周的表现
                            <div slot="content" id='eastmoney-hybk-down-charts' :style="{height: '900px'}"></div>
                        </Panel>
                        <Panel name="3">
                            【概念板块】上涨TOP10在最近8周的表现
                            <div slot="content" id='eastmoney-gnbk-up-charts' :style="{height: '900px'}"></div>
                        </Panel>
                        <Panel name="4">
                            【概念板块】下跌TOP10在最近8周的表现
                            <div slot="content" id='eastmoney-gnbk-down-charts' :style="{height: '900px'}"></div>
                        </Panel>
                    </Collapse>
                </h4>
                <<!-- Row>
                    <Col>
                        <div id='eastmoney-charts' :style="{height: '900px'}"></div>
                    </Col>
                </Row> -->
            </Card>
        </Row>
    </div>
</template>

<script>
import Cookies from 'js-cookie';
export default {
    data () {
        return {
            eastmoney_hybk_up_charts_name: [],
            eastmoney_hybk_up_charts_time: [],
            eastmoney_hybk_up_charts_combine: [],
            eastmoney_hybk_up_charts_set: 0,

            eastmoney_hybk_down_charts_name: [],
            eastmoney_hybk_down_charts_time: [],
            eastmoney_hybk_down_charts_combine: [],
            eastmoney_hybk_down_charts_set: 0,

            eastmoney_gnbk_up_charts_name: [],
            eastmoney_gnbk_up_charts_time: [],
            eastmoney_gnbk_up_charts_combine: [],
            eastmoney_gnbk_up_charts_set: 0,

            eastmoney_gnbk_down_charts_name: [],
            eastmoney_gnbk_down_charts_time: [],
            eastmoney_gnbk_down_charts_combine: [],
            eastmoney_gnbk_down_charts_set: 0,

            analysisaccordionvalue: ['1','2','3','4']
        };
    },
    created () {
        var token = 'token ' + Cookies.get('token') 
        console.log(token)

        this.$http.get('http://45.76.77.76:9900/eastmoneyhybkupanalysis', {headers: {Authorization: token}}).then(function (data) {
            data = data.body;
            this.eastmoney_hybk_up_charts_name = data.name
            this.eastmoney_hybk_up_charts_time = data.time
            this.eastmoney_hybk_up_charts_combineine = data.combine

            this.drawLine('eastmoney-hybk-up-charts', data.name, data.time, data.combine);
        }, function (response) {
            console.log(response.status)
        });

        this.$http.get('http://45.76.77.76:9900/eastmoneyhybkdownanalysis', {headers: {Authorization: token}}).then(function (data) {
            data = data.body;
            this.eastmoney_hybk_down_charts_name = data.name
            this.eastmoney_hybk_down_charts_time = data.time
            this.eastmoney_hybk_down_charts_combine = data.combine

            this.drawLine('eastmoney-hybk-down-charts', this.eastmoney_hybk_down_charts_name, this.eastmoney_hybk_down_charts_time, this.eastmoney_hybk_down_charts_combine);
        }, function (response) {
            console.log(response.status)
        });

        this.$http.get('http://45.76.77.76:9900/eastmoneygnbkupanalysis', {headers: {Authorization: token}}).then(function (data) {
            data = data.body;
            this.eastmoney_gnbk_up_charts_name = data.name
            this.eastmoney_gnbk_up_charts_time = data.time
            this.eastmoney_gnbk_up_charts_combine = data.combine

            this.drawLine('eastmoney-gnbk-up-charts', this.eastmoney_gnbk_up_charts_name, this.eastmoney_gnbk_up_charts_time, this.eastmoney_gnbk_up_charts_combine);
        }, function (response) {
            console.log(response.status)
        });

        this.$http.get('http://45.76.77.76:9900/eastmoneygnbkdownanalysis', {headers: {Authorization: token}}).then(function (data) {
            data = data.body;
            this.eastmoney_gnbk_down_charts_name = data.name
            this.eastmoney_gnbk_down_charts_time = data.time
            this.eastmoney_gnbk_down_charts_combine = data.combine

            this.drawLine('eastmoney-gnbk-down-charts', this.eastmoney_gnbk_down_charts_name, this.eastmoney_gnbk_down_charts_time, this.eastmoney_gnbk_down_charts_combine);
        }, function (response) {
            console.log(response.status)
        });
    },
    mounted () {
        // console.log('mounted')
        // this.drawLine();
    },
    methods: {
        drawLine (type, name, time, combine) {
            // 基于准备好的dom，初始化echarts实例
            // let eastmoney_hybk_up_charts = this.$echarts.init(document.getElementById('eastmoney-hybk-up-charts'))
            // let eastmoney_hybk_down_charts = this.$echarts.init(document.getElementById('eastmoney-hybk-down-charts'))
            // let eastmoney_gnbk_up_charts = this.$echarts.init(document.getElementById('eastmoney-gnbk-up-charts'))
            // let eastmoney_gnbk_down_charts = this.$echarts.init(document.getElementById('eastmoney-gnbk-down-charts'))

            var option = {
                        tooltip: {
                            position: 'top'
                        },
                        title: [],
                        singleAxis: [],
                        series: []
                    }
            // var my_names = this.names

            this.$echarts.util.each(time, function (day, idx) {
                option.title.push({
                    textBaseline: 'middle',
                    top: (idx + 0.5) * 100 / 8 + '%',
                    text: day
                })
                option.singleAxis.push({
                    left: 50,
                    type: 'category',
                    boundaryGap: false,
                    data: name,
                    top: (idx * 100 / 8 + 5) + '%',
                    height: (100 / 8 - 10) + '%',
                    axisLabel: {
                        interval: 2
                    }
                })
                option.series.push({
                    singleAxisIndex: idx,
                    coordinateSystem: 'singleAxis',
                    type: 'scatter',
                    data: [],
                    symbolSize: function (dataItem) {
                        return dataItem[1] * 6
                    }
                })
            })

            this.$echarts.util.each(combine, function (dataItem) {
                option.series[dataItem[0]].data.push([dataItem[1], dataItem[2]]);
            })

            if (type == 'eastmoney-hybk-up-charts') {
                if (this.eastmoney_hybk_up_charts_set == 0) {
                    let eastmoney_hybk_up_charts = this.$echarts.init(document.getElementById('eastmoney-hybk-up-charts'))
                    eastmoney_hybk_up_charts.setOption(option)
                    this.eastmoney_hybk_up_charts_set = 1
                }
            }else if (type == 'eastmoney-hybk-down-charts') {
                if (this.eastmoney_hybk_down_charts_set == 0) {
                    let eastmoney_hybk_down_charts = this.$echarts.init(document.getElementById('eastmoney-hybk-down-charts'))
                    eastmoney_hybk_down_charts.setOption(option)
                    this.eastmoney_hybk_down_charts_set = 1
                }
            } else if (type == 'eastmoney-gnbk-up-charts') {
                if (this.eastmoney_gnbk_up_charts_set == 0) {
                    let eastmoney_gnbk_up_charts = this.$echarts.init(document.getElementById('eastmoney-gnbk-up-charts'))
                    eastmoney_gnbk_up_charts.setOption(option)
                    this.eastmoney_gnbk_up_charts_set = 1
                }
            } else {
                if (this.eastmoney_gnbk_down_charts_set == 0) {
                    let eastmoney_gnbk_down_charts = this.$echarts.init(document.getElementById('eastmoney-gnbk-down-charts'))
                    eastmoney_gnbk_down_charts.setOption(option)
                    this.eastmoney_gnbk_down_charts_set = 1
                }
            }
            
        },
        changeAccordion (value) {
            console.log(value[0])
            if (value[0] == 2) {
                this.drawLine('eastmoney-hybk-down-charts', this.eastmoney_hybk_down_charts_name, this.eastmoney_hybk_down_charts_time, this.eastmoney_hybk_down_charts_combine);
            } else if (value[0] == 3) {
                this.drawLine('eastmoney-gnbk-up-charts', this.eastmoney_gnbk_up_charts_name, this.eastmoney_gnbk_up_charts_time, this.eastmoney_gnbk_up_charts_combine);
            } else if (value[0] == 4) {
                this.drawLine('eastmoney-gnbk-down-charts', this.eastmoney_gnbk_down_charts_name, this.eastmoney_gnbk_down_charts_time, this.eastmoney_gnbk_down_charts_combine);
            }
        }
    }
};
</script>