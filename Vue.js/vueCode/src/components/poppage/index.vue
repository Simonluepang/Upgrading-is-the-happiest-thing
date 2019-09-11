
<template>
  <div class="d-flex page-main popmain"
       v-if="showCustomPopup" @click.self="maskClick('self')">
    <!-- 弹出层 -->
    <div class="compop" :class="{'borderradius':radius}" :style="{'width':wth,'height':higt,'max-width': maxwth,'max-height': maxhigt}">
      <div class="pop-title" v-if="title!==''" :class="{'radiustop':radius}" :style="{'background':'url('+titleimg+') no-repeat','background-size':'100% 100%'}">{{title}}</div>
      <div  class="flex-grow myscroll">
        <slot></slot>
      </div>
      <div class="pop-btmbtn" :class="{'radiusbtm':radius}">
        <div class="cancelbtn" v-if="cancelbtn!==''" :class="{'radiusbtm':radius}" @click="cancelFn">{{cancelbtn}}</div>
        <div class="surebtn" v-if="surebtn!==''" :class="cancelbtn!==''&&surebtn!==''?'borderleft':''" @click="sureFn">{{surebtn}}</div>
      </div>
    </div>
  </div>
</template>

<script>
  var poptitleimg=require('../../assets/img/poptitle.png');
  export default {
    props:{
      autoclose:{
        type:Boolean,
        default:false
      },
      radius:{
        type:Boolean,
        default:true
      },
      backtop:{
        type:Boolean,
        default:true
      },
      wth:{
        type:String,
        default:'100%'
      },
      higt:{
        type:String,
        default:'100%'
      },
      maxwth:{
        type:String,
        default:'100%'
      },
      maxhigt:{
        type:String,
        default:'100%'
      },
      title:{
        type:String,
        default:''
      },
      titleimg:{
        type:String,
        default:poptitleimg
      },
      cancelbtn:{
        type:String,
        default:'取消'
      },
      surebtn:{
        type:String,
        default:'确定'
      },
      allshow:{
        type:Boolean,
        default:false
      }
    },
    data() {
      return {
        showCustomPopup: false,
      };
    },
    mounted(){
      if(this.allshow){
        this.showCustom();
      }
    },
    methods: {
      showCustom() {
        this.showCustomPopup = true;
      },
      maskClick(flg) {
        if(this.allshow===false) {
          if (flg === 'self') {
            if (this.autoclose === true) {
              this.showCustomPopup = false;
            }
          } else {
            this.showCustomPopup = false;
          }
        }
      },
      cancelFn(){
          this.maskClick();
          this.$emit('cancelFn');
      },
      sureFn(){
        this.maskClick();
        this.$emit('sureFn');
      },
    }
  }
</script>

<style scoped>
  .popmain{
    position: fixed;
    z-index: 10000;
    top: 0;
    right: 0;
    left: 0;
    bottom: 0;
    background: rgba(0,0,0,0.5);
    justify-content: center;
    align-items: center;
  }
  .compop{
    min-height: 100px;
    min-width: 300px;
    background: #fff;
    display: flex;
    flex-direction: column;
  }
  .pop-title{
    width: 100%;
    height: 60px;
    /*background: url('../../assets/img/poptitle.png') no-repeat;
    background-size: 100% 100%;*/
    color: #fff;
    font-size: 20px;
    line-height: 60px;
    padding-left: 20px;
    font-weight: bold;
    box-sizing: border-box;
    flex-shrink: 0;
  }
  .pop-btmbtn{
    height: 50px;
    box-sizing: border-box;
    width: 100%;
    display: flex;
    flex-direction: row;
    border-top: 1px solid #e4e6f3;
    line-height: 50px;
    flex-shrink: 0;
  }
  .cancelbtn{
    cursor: pointer;
    text-align: center;
    font-size: 16px;
    color: #7d7d85;
    flex-grow: 1;
    border-bottom-left-radius: 10px;
  }
  .surebtn{
    text-align: center;
    font-size: 16px;
    color: #07a2b6;
    /*width: 50%;*/
    cursor: pointer;
    flex-grow: 1;
    border-bottom-right-radius: 13px;
  }
  .borderleft{

    border-left: 1px solid #e4e6f3;
  }
  .borderradius{
    border-radius: 13px;
  }
  .radiustop{
    border-top-left-radius: 13px;
    border-top-right-radius: 13px;
  }
  .radiusbtm{
    border-bottom-left-radius: 13px;
    border-bottom-right-radius: 13px;
  }
</style>
