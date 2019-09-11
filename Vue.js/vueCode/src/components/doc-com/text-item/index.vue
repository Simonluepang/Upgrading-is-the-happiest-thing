<template>
  <div class="text-item-wrap">
    <div v-if="type == 'text_num' || type == 'text_single'" class="d-flex">
      <div v-for="(item,index) in textUnitType()" :key="index">
        <div-input class="mr-5 ml-5" v-if="item == 'borderDiv'"  v-model="default_value" bottomBorder
        ></div-input>
        <div-input class="mr-5 ml-5" v-else-if="item == 'noborderDiv'"  v-model="default_value"
        ></div-input>
        <div v-else>{{item}}</div>
      </div>
    </div>
    <div v-else-if="type == 'text_view'" :class="{tgrey:!default_value}">{{default_value || `{ ${options.ctl_name} }`}}</div>
    <div v-else-if="type == 'text_datetime'" class="d-flex">
      <div>{{options.ctl_name}}：</div>
      <date-item type="datetime" :value="default_value" format="yyyy-MM-dd HH:mm"></date-item>
    </div>
    <div v-else>{{options.ctl_name}}</div>
  </div>
</template>

<script>
import {Request} from '@/utils/request'
import divInput from '../div-input'
import dateItem from '@/components/doc-com/date-item'
export default {
  name: 'TextItem',
  components:{
    divInput,
    dateItem
  },
  props:{
    options:{
      type:Object,
      default(){
        return {}
      }
    },
  },
  watch:{
    options:{
      handler(val){
        if(val.default_value) {
          this.default_value = val.default_value;
        }
        // if(val.default_value_script) {
        //   let service = val.default_value_script;
        //   let url;
        //   if(service.script_type == 'api') {
        //      url = service.script_content;
        //   } else {
        //     url = '/medicalrecord/getmedicalrecorddata'
        //   }
        //   let params = {
        //     "scriptid": service.scriptid,
        //   }
        //   // Request('get',url,params).then(res => {
        //   //   if(res.data) {
        //   //   this.default_value = res.data;

        //   //   }
        //   // })
        // }
      },
      // deep:true,
      immediate:true
    },
    
  },
  computed:{
    type(){
      return this.options.ctl_type
    }
  },
  data(){
    return {
      inputValue:'',
      inputValue1:'',
      default_value:''
    }
  },
  methods:{
    textUnitType(){
      let result = []
      let dataName = this.options.ctl_name;
      if(/.+(（|\(){1}.+(）|\))$/.test(dataName)){
        let arr = dataName.match(/(.+)((（|\(){1}.+(）|\))$)/);
        result = [arr[1],'borderDiv',arr[2]]
      } else {
        result = [dataName+'：','noborderDiv']
      }
      return result
    },

    inputFocus(e){
      console.log('sssssss',e)
    }
  }
}
</script>
<style lang="scss" scoped>
  .text-item-wrap{
    .editBox{
      min-width: 40px;
      height: 20px;
      border-bottom: 1px solid #aaa;
    }
    .tgrey{
      color: #bbb8b8;
    }
  }

</style>
