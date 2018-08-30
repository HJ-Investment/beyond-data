<template>
    <div>
        <Row>
            <Col span="24">
                <Card>
                    <Form :label-width="80">
                        <FormItem label="文章标题" :error="articleError">
                            <Input v-model="articleTitle" @on-blur="handleArticletitleBlur" icon="android-list"/>
                        </FormItem>
                    </Form>
                    <div>
                        <editor v-model="content" @on-change="handleChange"/>
                    </div>
                    <br>
                    <span class="publish-button"><Button @click="publish" :loading="publishLoading" icon="md-cloud-upload" style="width:90px;" type="primary">发布</Button></span>
                </Card>
            </Col>
        </Row>
    </div>
</template>

<script>
import Editor from '_c/editor'
import { mapActions } from 'vuex'
export default {
  name: 'editor_page',
  components: {
    Editor
  },
  data () {
    return {
      content: '',
      articleTitle: '',
      articleError: '',
      publishLoading: false,
      owner: this.$store.state.user.userId
    }
  },
  methods: {
    ...mapActions([
      'handlePublish'
    ]),
    handleArticletitleBlur () {
        if (this.articleTitle.length !== 0) {
            // this.articleError = '';
            localStorage.articleTitle = this.articleTitle; // 本地存储文章标题
            if (!this.articlePathHasEdited) {
                let date = new Date();
                let year = date.getFullYear();
                let month = date.getMonth() + 1;
                let day = date.getDate();
                this.fixedLink = window.location.host + '/' + year + '/' + month + '/' + day + '/';
                this.articlePath = this.articleTitle;
                this.articlePathHasEdited = true;
                this.showLink = true;
            }
        } else {
            // this.articleError = '文章标题不可为空哦';
            this.$Message.error('文章标题不可为空哦');
        }
    },
    // editArticlePath () {
    //     this.editLink = !this.editLink;
    //     this.editPathButtonType = this.editPathButtonType === 'ghost' ? 'success' : 'ghost';
    //     this.editPathButtonText = this.editPathButtonText === '编辑' ? '完成' : '编辑';
    // },
    // setPublishTime (datetime) {
    //     this.publishTime = datetime;
    // },
    canPublish () {
        if (this.articleTitle.length === 0) {
            this.$Message.error('请输入文章标题');
            return false;
        } else {
            return true;
        }
    },
    publish () {
        var title = this.articleTitle
        var articelBody = this.content
        var ownerId = this.owner
        console.log(title, articelBody, ownerId)
        if (this.canPublish()) {
            this.publishLoading = true;
            console.log('1')
            // console.log(this.content)

            
            this.handlePublish({title, articelBody, ownerId}).then(res => {
                this.publishLoading = false;
                this.$router.push({
                    name: 'home'
                })
            })


            // setTimeout(() => {
            //     this.$http.post('http://45.76.77.76:9900/articles/', this.articelBody).then(function (data) {
            //         console.log(1)
            //         data = data.body;
            //         console.log(data)
            //         this.publishLoading = false;
            //         this.$Notice.success({
            //             title: '保存成功',
            //             desc: '文章《' + this.articleTitle + '》保存成功',
            //             onClose: this.$router.push({
            //                         name: 'articals'
            //                     })
            //         });
            //     }, function (response) {
            //         console.log(2)
            //         console.log(response.status)
            //     });
            // }, 1000);
        }
    },
    // handleSelectTag () {
    //     localStorage.tagsList = JSON.stringify(this.articleTagSelected);  // 本地存储文章标签列表
    // },
    handleChange (html, text) {
      // console.log(html, text)
      this.content = html
      console.log('handleChange: ' + this.content)
    }
  }
}
</script>