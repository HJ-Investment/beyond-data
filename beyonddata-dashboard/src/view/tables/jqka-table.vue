<!-- <style lang="less" scoped>
    @import '../../styles/common.less';
    @import './components/table.less';
</style> -->

<template>
    <div>
        <Row>
            <Col span="12">
                <DatePicker @on-change="changeDateTime" :value=date_value type="date" placeholder="Select date" style="width: 200px"></DatePicker>
            </Col>
        </Row>
        <Row class="margin-top-10">
            <Card>
                <h4 slot="title">
                    <Icon type="android-archive"></Icon>
                    同花顺行业板块涨跌Top10
                </h4>
                <Row>
                    <Col span="18">
                        <Table :columns="jqkaBKtableColumns" height="550px" :data=jqkatableData ref="tableExcel"></Table>
                    </Col>
                </Row>
            </Card>
        </Row>
    </div>
</template>

<script>
// import {table2csvData, csvColumns} from './data/table2csv.js';
// import {table2excelData, excelColumns} from './data/table2excel.js';
import util from '@/libs/util.js';
// import table2excel from '@/libs/table2excel.js';

import {eastmoneyBKtableColumns} from './data/eastmoneytop10.js'
import {jqkaBKtableColumns} from './data/jqkatop10.js'
export default {
    data () {
        return {
            date_value: new Date(),
            jqkatableData: [],
            jqkaBKtableColumns: jqkaBKtableColumns,
        };
    },
    created () {
        var time = util.formatDate(new Date(), 'yyyy-MM-dd')
        console.log(time)
        
        this.$http.get('http://45.76.77.76:9900/jqka?collection_time=' + time).then(function (data) {
            console.log(1)
            data = data.body;
            console.log(data)
            this.jqkatableData = data
        }, function (response) {
            console.log(2)
            console.log(response.status)
        });
    },
    methods: {
        changeDateTime (value) {
            this.date_value = value

            this.$http.get('http://45.76.77.76:9900/jqka?collection_time=' + value).then(function (data) {
                console.log(1)
                data = data.body;
                console.log(data)
                this.jqkatableData = data
            }, function (response) {
                console.log(2)
                console.log(response.status)
            });
        }
    }
};
</script>
