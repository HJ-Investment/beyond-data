<style lang="less" scoped>
    @import '../../../styles/common.less';
</style>

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
                    我的文章列表
                </h4>
                <Row>
                    <Col span="24">
                        <Table :columns="articlestableColumns" height="550px" :data=articletableData ref="tableExcel"></Table>
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
import {articlestableColumns} from './data/articles.js'
import Cookies from 'js-cookie';

export default {
    data () {
        return {
            date_value: new Date(),
            articlestableColumns: articlestableColumns,
            articletableData: [],
        };
    },
    created () {
        var time = util.formatDate(new Date(), 'yyyy-MM-dd')
        console.log(time)
        var username = Cookies.get('user') 
        this.$http.get('http://45.76.77.76:9900/articles?owner=' + username).then(function (data) {
            console.log(1)
            data = data.body;
            console.log(data)
            this.articletableData = data
        }, function (response) {
            console.log(2)
            console.log(response.status)
        });
    },
    methods: {
        changeDateTime (value) {
            this.date_value = value

            var username = Cookies.get('user') 
            var token = Cookies.get('token')
            this.$http.get('http://45.76.77.76:9900/articles?owner=' + username, ).then(function (data) {
                console.log(1)
                data = data.body;
                console.log(data)
                this.articletableData = data
            }, function (response) {
                console.log(2)
                console.log(response.status)
            });
        }
    }
};
</script>