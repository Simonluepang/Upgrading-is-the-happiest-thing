<template>
  <div class="tc-div">

    <pop-page ref="addplan"
              :allshow="true"
              maxwth="792px"
              maxhigt="80%"
              title="新增执行计划"
              @sureFn="sureFn" @cancel="cancel">
      <div class="add-div">
        <table class="subtable">
          <tr>
            <td class="td-title">护理诊断</td>
            <td>
              <search-drop searchplace="护理诊断关键字" place="请选择..." @reloadData="initZDFn"></search-drop>
            </td>
          </tr>
          <tr>
            <td class="td-title">相关因素</td>
            <td>
              <drop-ctrl ctrltype="multi" place="请选择..."></drop-ctrl>
            </td>
          </tr>
          <tr>
            <td class="td-title">症状/特征</td>
            <td>
              <search-drop searchplace="症状/特征关键字" place="请选择..." @reloadData="initZZFn"></search-drop>
            </td>
          </tr>
          <tr>
            <td class="td-title">目标</td>
            <td>
              <drop-ctrl ctrltype="multi" place="请选择..."></drop-ctrl>
            </td>
          </tr>
        </table>
        <div class="sublst">
          <div class="thead">
            <div class="r-xh itmchilddiv thcenter">
              <div class="checkbox"></div>
            </div>
            <div class="r-xh itmchilddiv thcenter">序号</div>
            <div class="r-hlcs itmchilddiv">护理措施</div>
            <div class="r-cz itmchilddiv thcenter">频次</div>
          </div>
          <div class="body-item">
            <div class="r-xh itmchilddiv thcenter cursorp" @click="checkFn('cs')">
              <div class="checkbox" :class="check.csIdLst.indexOf('1')>-1?'check-ok':''"></div>
            </div>
            <div class="r-xh itmchilddiv">1</div>
            <div class="r-hlcs itmchilddiv">护理措施测试1111</div>
            <div class="r-cz itmchilddiv thcenter">
              <drop-ctrl ctrltype="signle"></drop-ctrl>
            </div>
          </div>
        </div>
      </div>
    </pop-page>
  </div>
</template>

<script>
  import popPage from '@/components/poppage';
  import searchDrop from '@/components/doc-com/drop-ctrl/searchdrop';
  import dropCtrl from '@/components/doc-com/drop-ctrl';
  import { getZDLst, getCSLst, getYSLst, getZZLst, getMBLst } from '@/api/nurseplan';

  export default {
    name: 'newExePlan',
    components: {
      popPage,
      searchDrop,
      dropCtrl
    },
    data() {
      return {
        ZDLst: [],//初始化诊断lst
        YSLst: [],//相关因素lst
        ZZLst: [],//症状lst
        MBLst: [],//目标lst
        CSLst: [],//措施lst
        PCLst: [],//频次lst
        check: {
          zdIdLst: [],
          zdNameLst: [],
          ysIdLst: [],
          ysNameLst: [],
          zzIdLst: [],
          zzNameLst: [],
          mbIdLst: [],
          mbNameLst: [],
          csIdLst: [],
          csMapLst: []
        }
      };
    },
    created() {
      this.initData();
    },
    mounted() {
    },
    methods: {
      sureFn() {

      },
      cancel() {
      },
      initZDFn(keyword) {
        //获取诊断lst
        /* let params={
         keyword:keyword
       };
       getZDLst(params).then(res=>{
         console.log(res);
       })*/
      },
      initZZFn(keyword) {
        //获取症状Lst
        /*    let params={
         keyword:keyword
          };
          getZZLst(params).then(res=>{
            console.log(res);
          })*/
      },
      initData() {
        this.initZDFn();
        //获取相关因素Lst
        /*    let params={
            keyword:this.zdkeyWord
          };
          getYSLst(params).then(res=>{
            console.log(res);
          })*/
        //获取目标Lst
        /*   let params={
           keyword:this.zdkeyWord
         };
         getMBLst(params).then(res=>{
           console.log(res);
         })*/
        //获取目标Lst
        /*   let params={
           keyword:this.zdkeyWord
         };
         getCSLst(params).then(res=>{
           console.log(res);
         })*/
      },
      checkFn(flg, map) {
        switch (flg) {
          case 'cs':
            let indx = this.check.csIdLst.indexOf('1');
            if (indx > -1) {
              this.check.csIdLst.splice(indx, 1);
              this.check.csMapLst.splice(indx, 1);
            } else {
              this.check.csIdLst.push('1');
              this.check.csMapLst.push(map);
            }

        }
      }
    }
  };
</script>

<style scoped>
  @import "../../styles/subcommon.scss";
  .tc-div {
    width: 100%;
    height: 100%;
    overflow: hidden;
    padding: 0;
    margin: 0;
    background: transparent;
  }

  .add-div {
    box-sizing: border-box;
    width: 100%;
    min-height: 100%;
    height: auto;
    padding: 18px;
    /*overflow: hidden;*/
    /*overflow-y: auto;*/
  }

  .sublst {
    width: 100%;
    margin-top: 15px;
    border: 1px solid #e6e7ef;
    border-bottom: none;
  }

  .thead {
    width: 100%;
    height: 30px;
    background: #F7F8FC;
    color: #7F7F93;
    font-size: 14px;
    display: flex;
    flex-direction: row;
    align-items: stretch;
    border-bottom: 1px solid #E6E7EF;
  }

  .body-item {
    width: 100%;
    height: 40px;
    color: #33333F;
    font-size: 14px;
    display: flex;
    flex-direction: row;
    align-items: stretch;
    border-bottom: 1px solid #E6E7EF;
  }

  .itmchilddiv {
    display: flex;
    align-items: center;
    padding: 0 5px;
    box-sizing: border-box;
  }

  .thcenter {
    justify-content: center;
  }

  .r-xh {
    width: 40px;
  }

  .r-hlcs {
    width: calc(100% - 180px);
    flex-grow: 1;
    white-space: nowrap;
    text-overflow: ellipsis;
  }

  .r-cz {
    width: 100px;
  }

  .checkbox {
    width: 14px;
    height: 14px;
    background: url("../../assets/img/operate/weixuanzhong.png") no-repeat;
    background-size: 100% 100%;
    flex-shrink: 0;
  }

  .check-ok {
    background: url("../../assets/img/operate/xuanzhong.png") no-repeat;
    background-size: 100% 100%;
  }
</style>
