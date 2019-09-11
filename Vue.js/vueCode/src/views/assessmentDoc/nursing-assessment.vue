<template>
<div class="page-wrap">
  <div class="page-header b-box d-flex j-between a-center pl-20 pr-20" >
    <div>
     <drop-down :data="selectedData">
      <template v-slot="{item}">
        <div class="d-flex a-center j-between">
          <div>{{item.value}}</div>
          <div>{{item.displaylabel}}</div>
        </div>
      </template>
     </drop-down>
    </div>
    <div class="d-flex">
      <button type="button" class="layui-btn layui-btn-sm layui-btn-danger">新建</button>
      <button type="button" disabled class="layui-btn layui-btn-sm layui-btn-danger">保存</button>
      <button type="button" disabled class="layui-btn layui-btn-sm layui-btn-danger">导出</button>
      <button type="button" disabled class="layui-btn layui-btn-sm layui-btn-danger">打印</button>
      <button type="button" disabled class="layui-btn layui-btn-sm layui-btn-danger">删除</button>
    </div>
  </div>
  <div class="nursing-assessment-wrap b-box myscroll">
    <form-header :publicData="publicData" ></form-header>
    <form-box :formData="formData"></form-box>
  </div>
</div>
</template>

<script>
import { getFormData,getPublicitemData} from '@/api/nursing-assessment.api';
import  formBox from '@/components/form-box/form-box';
import formHeader from '@/components/form-box/header'
import dropDown from '@/components/doc-com/drop-down'
export default {
  name: 'NursingAssessment',
  components:{
    formBox,
    formHeader,
    dropDown
  },
  data(){
    return {
      assessData:{},
      formData:[],
      publicData:[],
      publicIds:[],
      dicparams:{},
      selectedData:[
        {
          value:'1',
          displaylabel:'测试',
          displaySelect:'测试显示',
        },
        {
          value:'2',
          displaylabel:'测试ssss',
          displaySelect:'测试显示',
        }
      ]
    }
  },
  created(){
    getFormData('2019070814305313801337a4af76831d').then(res => {
      if(res.data && res.data.ctl_extends) {
        this.dicparams = { 
          "zyh": "01951706", //"住院号",
          "rycs": "1",//"入院次数",
          "cwh": "01906",// "床位号",
          "bqdm": "116", // "病区代码",
          "inner_code":res.data.ds_innercode,//"数据元内码",
          "hospitalid":"9DA399D7EEF64131AE23C1063CF4EE82",//"医院ID",
          "templateid":res.data.id,//"模板ID",
          "forpeople":res.data.fitcode
          }
        this.formatData(res.data.ctl_extends);
      }
    })
  },
  methods:{
    formatData(originData){
      this.publicData = [];
      this.formData = [];
      if(originData&&originData.length) {
        originData.forEach(item => {
          if(item.default_value_script) {
            this.publicIds.push(item.default_value_script.scriptid);
          }
        })
        this.getPublicData(originData).then(origin => {
          let groupMap = {};
          for(let item of origin) {
            if(item.mobile_type) {
              if(!groupMap[item.mobile_type]) {
                groupMap[item.mobile_type+''] = [];
              }
             groupMap[item.mobile_type+''].push(item);
            } else if(item.ispublicctrl){
              this.publicData.push(item);
            }
          }
          for(let key in groupMap) {
            groupMap[key].sort((a,b) =>{
              return a.sort - b.sort
            })
            let data = groupMap[key].sort((a,b) =>{
              return a.sort_num - b.sort_num
            })
            let item = {
              label:key,
              data:data,
              sort:data[0].sort_num,
              showAttrextends:[]
            }
            this.formData.push(item)
          }

          this.formData.sort((a,b) => {
            return a.sort - b.sort
          }),

          this.publicData.sort((a,b) => {
            return a.sort_num - b.sort_num
          })

        })
      }
    },
    getPublicData(originData){
      let params = {
        scriptids : JSON.stringify(this.publicIds),
        dicparams:this.dicparams
      }
      return getPublicitemData(params).then(res => {
        if(res.code == 0 && res.data) {
          let valueArr = res.data
          originData.forEach(item => {
            if(item.default_value_script) {
              let apiItem = valueArr.find((val => {
                return val.key == item.default_value_script.scriptid
              }))
              if(apiItem.data){
                item.default_value = apiItem.data;
              }
            }
          })
        }
        return originData
      })
    }
  }
}
</script>
<style lang="scss" scoped>
  .page-wrap{
    height: 100%;
    .page-header{
      height: 60px;
      border-bottom:1px solid #f1f0f0
    }
    .nursing-assessment-wrap{
      padding: 40px 80px;
      height: calc(100% - 60px);
      // height: 100%;
      // background: pink;
      overflow: auto;
    }
  }
</style>
