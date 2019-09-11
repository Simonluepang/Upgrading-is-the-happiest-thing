<template>
  <div  @click="changeChecked" class="check-box-item-wrap d-flex a-center re">
    <label class="wxzlabelbg" :class="{xzlabelbg:isChecked}"></label>
    <div-input :isEdit="isEdit" class="label-name pl-2 mr-10"  v-model="editLabel"></div-input>
  </div>
</template>

<script>
import divInput from '../div-input'
export default {
  name: 'CheckBoxItem',
  components:{
    divInput
  },
  props:{
    options:{
      type:Object,
      default(){
        return {
          isEdit:false,
        }
      }  
    },
    isEdit:{
      type:Boolean,
      default:false,
    },
    value:{
      type:Boolean,
      default:false
    },
    label:{
      type:String,
      default:''
    }
  },
  watch:{
    value:{
      handler(v){
       this.isChecked = v;
       if(v) {
        this.$emit('checkedChenge',v);
       }
      },
      immediate:true
    }
  },
  computed:{
    editLabel:{
      get(){
        return this._editLabel || this.label
      },
      set(v){
        this._editLabel = v;
        this.$emit('labelChange',v)
      }
    }
  },
  data(){
    return {
      timmer:null,
      _editLabel:'',
      isChecked:false,
    }
  },
  mounted(){
  },
  methods:{
    changeChecked(){
      this.$emit('input',!this.isChecked);
      this.$emit('checkedChenge',!this.isChecked);
    },
  }
}
</script>
<style lang="scss" scoped>
  .pl-2{
    padding-left: 2px;
  }
  .check-box-item-wrap{
    font-size: 14px;
    line-height: 14px;
    padding-top: 3px;
    padding-bottom: 3px;
    >label{
      position: relative;
      // border: 1px solid #333;
      width: 12px;
      height: 12px;
      // text-align: center;
      // line-height: 16px;
      // font-size: 13px;
      font-weight: 600;
      background-size:100% 100%; 
      &.wxzlabelbg{
        background-image: url('../../../assets/img/operate/weixuanzhong.png')
      }
      &.xzlabelbg{
        background-image: url('../../../assets/img/operate/xuanzhong.png')
      }
    }
  }
</style>
