<template>
  <div class="form-box-wrap mt-10">
    <div class="d-flex" v-for="(dataItem,index) in formData" :key="index">

      <div class="form-label d-flex a-center j-center">
        {{dataItem.label !== 'null' ? dataItem.label : ''}}
      </div>
      <div class="flex-auto">
        <div class="form-item p-10 d-flex a-center f-14" v-for="(item,index) in ctlLinkfilter(dataItem.data)" :key="index">
          <div class="form-index">{{index+1+'、'}}</div>
            <text-item class="flex-auto" v-if="getItemType(item.ctl_type) == 'text'" :options="item"></text-item>
            <check-boxs class="flex-auto" v-else-if="getItemType(item.ctl_type) == 'drop'" 
            :options="item"
            @valueChange="valueChange(dataItem,item,$event)"
            
            ></check-boxs>
        </div>
        <template v-if="dataItem.showAttrextends.length">
          <div class="form-item p-10 d-flex a-center f-14" v-for="(item,index) in dataItem.showAttrextends" :key="item.ctl_id">
            <div class="form-index">{{`(${index+1})`}}</div>
            <text-item class="flex-auto" v-if="getItemType(item.ctl_type) == 'text'" :options="item"></text-item>
            <check-boxs class="flex-auto" v-else-if="getItemType(item.ctl_type) == 'drop'" 
            :options="item"
            ></check-boxs>
          </div>
        </template>
      </div>
    </div>
  </div>
</template>

<script>
import checkBoxs from '@/components/doc-com/check-boxs';
import textItem from '@/components/doc-com/text-item';
export default {
  name: 'FormBox',
  components:{
    checkBoxs,
    textItem
  },
  props:{
    formData:{
      type:Array,
      default(){
        return []
      },
    }
  },
  filters:{
  },
  data(){
    return {
      linkdata:{},
      dataReady:false
    }
  },
  computed:{
  },

  mounted(){
  },
  methods:{
    getItemType(str){
      if (str.indexOf('drop')>-1) {
        return 'drop'
      } else if (str.indexOf('text')>-1 && str.indexOf('drop') < 0 ){
        return 'text'
      }
    },
    ctlLinkfilter(arr) {
      let res = [];
      for(let item of arr) {
        if(!item.link_ctl || !item.link_ctl.length) {
          res.push(item)
        } else if(item.link_ctl && item.link_ctl.length && !this.dataReady){
          let key = item.attrextends.showbylinkctrl;
          if(!this.linkdata[key]){
            this.linkdata[key] = {linkid:[],data:[]}
          }
          this.linkdata[key].linkid = [...this.linkdata[key].linkid,...item.link_ctl];
          this.linkdata[key].data.push(item)
        }
      }
      return res
    },
    valueChange(g,i,e) {
      console.log(e.isdefault)
      this.ctlLinkDataInit(g,i)
    },
    ctlLinkDataInit(g,i){
      this.dataReady = true
      g.showAttrextends = [];
      i.data_value.forEach(item => {
        if(this.linkdata[item.val_str] && item.isdefault) {
          let addBefore = this.linkdata[item.val_str]
          if(addBefore.linkid.indexOf(i.ctl_id)>-1) {
            g.showAttrextends = [...g.showAttrextends,...addBefore.data];
          }
        }
      })
    }
  },

}
</script>
<style lang="scss" scoped>
  .form-index{
    line-height: 26px;
    align-self: flex-start
  }
  .form-box-wrap{
    min-height: 400px;
    border: 1px solid #333;
    flex-shrink: 0;
    align-self: flex-start;
    .form-label{
      padding: 10px;
      width: 110px;
      flex-shrink: 0;
      border-right: 1px solid #333;
      border-bottom: 1px solid #333;
      &:last-child{
        border-bottom:none;
      }
    }
    .form-item{
      padding: 10px;
      min-height: 20px;
      border-bottom: 1px solid #333;
      &:nth-last-child(){
        border-bottom:none;
      }
    }
  }

</style>
