<template>
  <div class="check-boxs-wrap d-flex a-center">
    <div class="check-label mr-15 f-14">{{options.ctl_name && options.ctl_name + '：'}}</div>
    <div class="check-group d-flex a-center flex-wrap">
      <check-item  
        v-for="(item,index) in boxsData || []" :key="index" 
        :label="item.val_str" v-model="item.isdefault"
        @checkedChenge="checkedChenge(item,$event)"
        @labelChange="labelChange(item,$event)" />
        <div-input v-if="options.link_type.indexOf('lastedit')>-1" bottomBorder isEdit/>
    </div>
  </div>
</template>

<script>
import checkItem from "./check-box-item";
import divInput from '../div-input'
export default {
  name: "CheckBoxs",
  components: {
    checkItem,
    divInput
  },
  props: {
    options: {
      type: Object,
      default:{}
    }
  },
  watch:{
    options:{
      handler(v){
        this.boxsData = v.data_value;
        let type = v.ctl_type_attr || '';
        this.isMult = !!(type.indexOf('mult') > -1);
        this.isEdit = !!(type.indexOf('text') > -1);
      },
      immediate:true
    }
  },
  computed:{
  },
  data() {
    return {
      isEdit: false,
      isMult: false,
      boxsData:[],
    };
  },
  mounted(){
  },
  methods: {
    labelChange(item,v) {
      item.val_str = v;
    },
    checkedChenge(item){
      // item.isdefault = v;
      if(!this.isMult) {
        this.boxsData.forEach(ele => {
          if(ele.isdefault &&  ele.val_code != item.val_code) {
            ele.isdefault = false;
          }
        });
      }
      this.$emit('valueChange',item);

    }
  }
};
</script>
<style lang="scss" scoped>
.check-boxs-wrap {
  .check-label{
    line-height: 26px;
    flex-shrink: 0;
    align-self: flex-start;
  }
}
</style>