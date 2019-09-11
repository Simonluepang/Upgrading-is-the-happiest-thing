<template>
  <div class="header-wrap">
    <div class="f-25 text-center ">
      <text-item :options="publicData[0]" ></text-item>
    </div>
    <div class="f-25 text-center mt-5">
       <text-item :options="publicData[1]" ></text-item>
    </div>
    <div style="height:20px" class="mt-20 d-flex j-between flex-wrap">
      <div class="d-flex a-center" v-for="(item ,index) in publicData.slice(2,)" :key="index">
        <div>{{item.appctlname}}：</div>
        <text-item :options="item" ></text-item>
      </div>
    </div>
  </div>
</template>

<script>
import divInput from '@/components/doc-com/div-input';
import textItem from '@/components/doc-com/text-item';
// import {getPublicitemData} from '@/api/nursing-assessment.api';
export default {
  name: 'Header',
  components:{
    divInput,
    textItem
  },
  props:{
    publicData:{
      default(){
        return[]
      },
      type:Array,
    }
  },
  watch:{
   publicData:{
     handler(v){

     },
     immediate:true
   } 
  },
  methods:{
    getDefaultValue(data){
      let scriptids = [];

    }
  }
}
</script>
<style lang="scss" scoped>

</style>
