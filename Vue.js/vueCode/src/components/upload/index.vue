<template>
  <div class="add-pic-wrap">
    <template v-if="imgurl.length>0">
      <div class="added-pics" v-for="(item,index) in imgurl" :key="index">
        <img :src="item.imgUrl" alt>
      </div>
    </template>
    <div class="flex-center add-pic" v-if="imgurl.length<4">
      <div>
        <span style="font-size: 30px">+</span>
        <!--<div style="margin-top: 0.08rem;">添加照片</div>-->
        <input type="file" class="upload-input" accept="image/*" @change="upLoad($event)">
      </div>
    </div>
  </div>
</template>
<script>
  import { UploadFile } from "../../api/nurseplan";

  export default {
    props: {
      imgurl: {
        type: Array
      }
    },
    data() {
      return {
        baseUrl: ""
      };
    },
    created(){},
    methods: {
      upLoad(event) {
        var file = event.target.files[0];
        var imageType = /^image\//;
        //是否是图片
        if (!imageType.test(file.type)) {
          alert("请选择图片！");
          return;
        }
        let params = new FormData();
        params.append("sFile", file);
        UploadFile(params).then(res => {
          if(res.code!==undefined&&parseInt(res.code)===0) {
            let newimgurl = [...this.imgurl, { imgUrl: res.data }];
            this.$emit("changePics", newimgurl);
          }else{
            alert("上传文件失败，请重试");
          }
        });

      },
     /* getBaseUrlFn() {
        getbaseurl().then(res => {
          if (res.code!==undefined&&parseInt(res.code) === 0) {
            this.baseUrl = res.data;
          }
        });
      },*/
      deleImg(index) {
        this.imgurl.splice(index, 1);
      }
    }
  };
</script>
<style lang="scss" scoped>
  .flex-center {
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .add-pic-wrap {
    display: flex;
    margin:4px 2px;

    .added-pics {
      position: relative;
    }

    img {
      width: 70px;
      height: 70px;
      margin-right: 7px;
      border-radius: 3px;
      border:1px solid #CCCCDB;
    }

    .add-pic {
      background: #ffffff;
      width: 70px;
      height: 70px;
      text-align: center;
      color: rgba(150, 150, 159, 1);
      border-radius: 3px;
      border:1px solid #CCCCDB;
      font-size: 33px;
      position: relative;

      .upload-input {
        width: 70px;
        height: 70px;
        position: absolute;
        top: 50%;
        transform: translateY(-50%);
        left: 0;
        opacity: 0;
      }
    }
  }
</style>

