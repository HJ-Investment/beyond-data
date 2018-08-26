// new Vue({
//     el: '#app',
//     data: {
//         eastmoneyBKtableDatas: [],
//         eastmoneyBKtableData: {
//             collection_time: '',
//             sequence: 0,
//             bk_name: '',
//             last_price: 0,
//             raise_down: 0,
//             raise_down_perc: 0,
//             total_value: 0,
//             changes: 0,
//             raise_num: 0,
//             down_num: 0,
//             top_raise_down: '',
//             top_raise_down_perc: 0
//         },
//     },
//     // created: function() {
//     //     this.$http.get('45.76.77.76:9900/eastmoney_hybkup').then((data) => {
//     //         data = $.parseJSON(data.body);  //console.log(data.body)
//     //         this.books=data.data;
//     //     })
//     // },
//     methods:{
//         get_bybkup:function(){
//             this.$http.jsonp('http://45.76.77.76:9900/eastmoney_hybkup').then((data) => {
//                 data = $.parseJSON(data.body);
//                 console.log(data)
//                 this.eastmoneyBKtableData = data.data
//                 // this.book.id=parseInt(data.data);
//                 // this.books.push(this.book);
//                 // this.book='';
//             });
//         },
//         // delBook:function(book){
//         //     this.$http.post('http://localhost:8080/vuejs/api/del.php', {bookId:book.id}).then((data) => {
//         //         this.books.$remove(book);
//         //     });
//         // },
//     }
// });



// export const eastmoneyBKtableData = [{
//                     "sequence": 1,
//                     "bk_name": "000000",
//                     "last_price": 7302,
//                     "raise_down": 5627,
//                     "raise_down_perc": 1563,
//                     "total_value": 4254,
//                     "changes": 1438,
//                     "raise_num": 274,
//                     "down_num": 285,
//                     "top_raise_down": "1727",
//                     "top_raise_down_perc": 558
//                     }]

export const eastmoneyBKtableColumns = [
    {
        'title': '时间',
        'key': 'collection_time',
        // 'fixed': 'left',
        'width': 150
    },
    {
        'title': '排名',
        'key': 'sequence',
        // 'fixed': 'left',
        'width': 150
    },
    {
        'title': '板块名称',
        'key': 'bk_name',
        'fixed': 'left',
        'width': 200,
        // 'sortable': true,
        // filters: [
        //     {
        //         label: '大于4000',
        //         value: 1
        //     },
        //     {
        //         label: '小于4000',
        //         value: 2
        //     }
        // ],
        // filterMultiple: false,
        // filterMethod (value, row) {
        //     if (value === 1) {
        //         return row.show > 4000;
        //     } else if (value === 2) {
        //         return row.show < 4000;
        //     }
        // }
    },
    {
        'title': '最新价',
        'key': 'last_price',
        'width': 150,
        // 'sortable': true
    },
    {
        'title': '涨跌额',
        'key': 'raise_down',
        'width': 150,
        // 'sortable': true
    },
    {
        'title': '涨跌幅',
        'key': 'raise_down_perc',
        'width': 150,
        // 'sortable': true
    },
    {
        'title': '总市值(亿)',
        'key': 'total_value',
        'width': 150,
        // 'sortable': true
    },
    {
        'title': '换手率',
        'key': 'changes',
        'width': 150,
        // 'sortable': true
    },
    {
        'title': '上涨家数',
        'key': 'raise_num',
        'width': 150,
        // 'sortable': true
    },
    {
        'title': '下跌家数',
        'key': 'down_num',
        'width': 150,
        // 'sortable': true
    },
    {
        'title': '领涨股票',
        'key': 'top_raise_down',
        'width': 150,
        // 'sortable': true
    },
    {
        'title': '涨跌幅',
        'key': 'top_raise_down_perc',
        'width': 150,
        // 'sortable': true
    }
];