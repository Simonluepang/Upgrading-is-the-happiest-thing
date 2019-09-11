<template>
  <div class="date-item-wrap">
    <input readonly type="text" ref="dateRef" id="sssss">
  </div>
</template>

<script>
export default {
  name: 'DateItem',
  props:{
    type:{
      default:"date",
      type:String,
    },
    format:{
      default:"yyyy-MM-dd",
      type:String,
    },
    service:{
      type:Object,
      default(){
        return {}
      }
    },
    value:{
      type:String,
      default:''
    }
  },
  watch:{
    value:{
      handler(v) {
        this.laydate.render({
          elem:  this.$refs.dateRef,
          value:v
        })
      },
      // immediate:true
    }
  },
  data(){
    return {
      laydate:layui.laydate,
      dateobj:{}
    }
  },
  mounted(){
    this.$nextTick(() => {
      let format = this.format;
      this.dateobj =  this.laydate.render({
        elem:  this.$refs.dateRef,//指定元素
        type: this.type,
        format:this.format,
        value:this.value
      })
      // this.laydate.set({value:'2019-09-09 20:58'})
      // console.log('mounted',a);
      // this.laydate = layui.laydate;
    })
  },
}
</script>
<style lang="scss" scoped>
  .date-item-wrap{
    input{
      height: 20px;
      border: 0;
    }
  }
</style>
