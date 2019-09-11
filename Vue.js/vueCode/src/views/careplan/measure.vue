<template>
  <div class="page-main d-flex a-stretch">
    <div class="left-content">
      <div class="con-title">
        <span class="model-title f-16">护理诊断</span>
        <div class="search">
          <input type="text" class="search-input" v-model="zdkeyWord" placeholder="护理诊断关键字" />
        </div>
      </div>
      <div class="con">
        <div class="leftitem" v-for="(md,indx) in ZDLst" :class="checkZDId===md.id?'active':''" @click="changZDFn(md.id)" :key="'zd_'+indx">
          <div class="xh">{{indx+1}}</div>
          <div class="moremsg">{{md.name}}</div>
        </div>
      </div>
    </div>
    <div class="right-content flex-grow">
      <div class="con-title">
        <span class="model-title f-16">护理措施</span>
        <div class="search">
          <input type="text" class="search-input" placeholder="护理措施关键字" />
        </div>
        <div class="flex-grow"></div>
        <div class="rightbtn">
          <div class="addbtn" @click="openWindow">新增</div>
        </div>
      </div>
      <div class="con rightcon">
        <div class="thead">
          <div class="r-xh thcls">序号</div>
          <div class="r-hllx thcls">护理类型</div>
          <div class="r-hlfl thcls">护理分类</div>
          <div class="r-hlcs thcls">护理措施</div>
          <div class="r-cz thcls">操作</div>
        </div>
        <div class="tbody">
          <div class="l-con r-xh">
            <div class="tdcls" v-for="(md,indx) in CSLst" :key="'xh_'+indx">{{indx+1}}</div>
          </div>
          <div class="r-con">
            <div class="r-item" v-for="(md,indx) in fzCSLst" :key="'cs_'+indx">
              <div class="namediv bd1">{{md.name}}</div>
              <div class="ritdiv">
                <div class="ritdivone" v-for="(m,ind) in md.children" :key="'fl_'+ind">
                <div class="namediv bd1">
                  {{m.name}}
                </div>
                <div class="ritdiv">
                  <div class="ritdivone"  v-for="(cs,ind) in m.children" :key="'cs_'+ind">
                  <div  class="rtd-hlcs tdcls bd1">{{cs.nurse_measure}}</div>
                  <div class="r-cz tdcls td-center pl0 bd1">
                    <img class="operate" src="../../assets/img/operate/Compose.png">
                    <img class="operate ml-10" src="../../assets/img/operate/Trash.png">
                  </div>
                  </div>
                </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <!--<div @click="openWindow">弹出窗</div>-->
    </div>
    <pop-page ref="addCs"
              maxwth="792px"
              maxhigt="80%"
              :title="addMaptitle"
              @sureFn="sureFn">
      <div class="add-div">
        <table class="subtable">
          <tr>
            <td class="td-title">
              <font class="import-flg">*</font>措施名称
            </td>
            <td>
              <input type="text" class="text-input" placeholder="请输入护理措施名称" v-model="addMap.name">
            </td>
          </tr>
          <tr>
            <td class="td-title">
              护理类型
            </td>
            <td>
              <drop-ctrl ctrltype="signle" place="请选择..."></drop-ctrl>
            </td>
          </tr>
          <tr>
            <td class="td-title">
              护理分类
            </td>
            <td>
              <drop-ctrl ctrltype="signle" place="请选择..."></drop-ctrl>
            </td>
          </tr>
          <tr>
            <td class="td-title">
              <font class="import-flg">*</font>措施内容
            </td>
            <td class="multi-text">
              <textarea placeholder="请输入..." class="text-input" v-model="addMap.contentmsg"></textarea>
            </td>
          </tr>
          <tr>
            <td class="td-title">
              措施描述
            </td>
            <td class="multi-text">
              <textarea placeholder="请输入..." class="text-input" v-model="addMap.desc"></textarea>
            </td>
          </tr>
          <tr>
            <td class="td-title">相关图片</td>
            <td class="auto-height">
              <img-upload :imgurl="addMap.imgLst"></img-upload>
            </td>
          </tr>
          <tr>
            <td class="td-title">
              参考文献
            </td>
            <td>
              <input type="text" class="text-input" placeholder="请输入..." v-model="addMap.lookmsg">
            </td>
          </tr>
        </table>
      </div>
    </pop-page>
  </div>
</template>

<script>
  import popPage from '@/components/poppage'
  import dropCtrl from '@/components/doc-com/drop-ctrl';
  import imgUpload from '@/components/upload';
  import {getZDLst,getCSLst} from '@/api/nurseplan'
  export default {
    name: 'measure',
    components:{popPage,dropCtrl,imgUpload},
    data(){
      return{
        checkZDId:"1",//选中诊断id
        ZDLst:[{id:'1',name:"测试数据111"},{id:'2',name:"测试数据2222"},{id:'3',name:"测试数据3333"}],//诊断列表数据
        zdkeyWord:"",//诊断查询关键字
        cskeyWord:"",//措施查询关键字
        CSLst:[
          {
            id:"1",
            nurse_type:"基本类型",
            nurse_classify:"活动",
            nurse_measure:"健康教育-卧床休息"
          },
          {
            id:"2",
            nurse_type:"基本类型",
            nurse_classify:"体液容量",
            nurse_measure:"监测入量"
          },
          {
            id:"3",
            nurse_type:"基本类型",
            nurse_classify:"体液容量",
            nurse_measure:"监测出量"
          },
          {
            id:"4",
            nurse_type:"护理类型",
            nurse_classify:"活动",
            nurse_measure:"健康教育-卧床休息"
          },
          {
            id:"5",
            nurse_type:"护理类型",
            nurse_classify:"体液容量",
            nurse_measure:"监测入量"
          },
          {
            id:"6",
            nurse_type:"护理类型",
            nurse_classify:"体液容量",
            nurse_measure:"监测出量"
          },
        ],//措施列表数据
        fzCSLst:[],//措施分组后数据
        addMaptitle:'新增护理措施',//区分新增还是编辑
        addMap:{
          name:"",
          type:"",
          model:"",
          contentmsg:"",
          desc:"",
          lookmsg:"",
          imgLst:[]
        }
      }
    },
    watch:{
      zdkeyWord:{
        handler(){
          this.getZDLstFn();
        },
        immediate:true
      },
      cskeyWord:{
        handler(){
          this.getCSLstFn();
        },
        immediate:true
      }
    },
    created(){

    },
    mounted(){

    },
    methods:{
      openWindow(){
        this.$refs.addCs.showCustom();
      },
      changZDFn(zdid){
        this.checkZDId=zdid;
      },
      getTreeData(valLst,keyname) {
        var keylst = [];
        var result=[];
        valLst.map(it=>{
          let indx=keylst.indexOf(it[keyname]);
          if(indx>-1){
            result[indx].children.push(it);
          }else{
            var oneitem={
              name:it[keyname],
              children:[]
            };
            keylst.push(it[keyname]);
            oneitem.children.push(it);
            result.push(oneitem);
          }
        });
        return result;
      },
      dealCSLst () {
        let retLst=[];
        let oldLst=this.CSLst;
        let treeMap1=this.getTreeData(oldLst,'nurse_type');
        treeMap1.map(it=>{
          var oneitem={
            name:it.name,
            children:[]
          }
          oneitem.children=this.getTreeData(it.children,'nurse_classify');
          retLst.push(oneitem);
        })

        this.fzCSLst=retLst;
      },
      getZDLstFn(){
        console.log("获取lst")
       /* let params={
          keyword:this.zdkeyWord
        };
        getZDLst(params).then(res=>{
          console.log(res);
        })*/
      },
      getCSLstFn(){
        console.log("获取cslst")
       /* let params={
          keyword:this.cskeyWord
        };
        getCSLst(params).then(res=>{
          console.log(res);
        })*/
       this.dealCSLst();
      },
      sureFn(){

      }
    }
  };
</script>

<style scoped lang="scss">
  @import "../../styles/subcommon.scss";
  .left-content {
    width: 25%;
    max-width: 300px;
    padding-right: 10px;
    background: #f1f2f7;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
  }

  .con {
    width: 100%;
    height: 100%;
    background: #fff;
    overflow: hidden;
    overflow-y: auto;
    flex-grow: 1;
    .leftitem{
      width: 100%;
      min-height: 40px;
      box-sizing: border-box;
      border-left: 5px solid #fff;
      color:#33333F;
      font-size: 14px;
      display: flex;
      flex-direction: row;
      align-items: stretch;
      cursor: pointer;
      .xh{
        display: flex;
        width: 40px;
        justify-content: center;
        align-items: center;
      }
      .moremsg{
        display: flex;
        flex-grow: 1;
        align-items: center;
        width: calc(100% - 40px);
        padding: 10px;
      }
    }
    .active{
      border-left: 5px solid #0DB4C8;
      background: #E9FAFB;
    }
  }
  .rightcon{
    overflow: hidden;
    padding: 0 15px;
    display: flex;
    flex-direction: column;
    .thead{
      width: 100%;
      height: 35px;
      background: #F7F8FC;
      border:1px solid #E6E7EF;
      color:#7F7F93;
      font-size: 14px;
      display: flex;
      flex-direction: row;
      align-items: stretch;
    }
    .tbody{
      width: 100%;
      /*flex-grow: 1;*/
      display: flex;
      flex-direction: row;
      overflow: hidden;
      overflow-y: auto;
      /*align-items: stretch;*/
    }
    .l-con{
      display: flex;
      flex-direction: column;
      align-items: stretch;
      div{
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 14px;
        height: 35px;
        border-right:  1px solid #e6e7ef;
        border-bottom: 1px solid #e6e7ef;
        border-left: 1px solid #e6e7ef;
        width: 100%;
        box-sizing: border-box;
        color:#33333F;
      }
    }
    .r-con{
      width: calc(100% - 40px);
    }

    .thcls{display: flex;align-items: center;justify-content: center;}
    .tdcls{
      display: flex;
      border-right:1px solid #E6E7EF;
      align-items: center;
      padding:0 5px;
      box-sizing: border-box;
    }
    .bd1{border-bottom: 1px solid #e6e7ef;border-right: 1px solid #e6e7ef;}
    .td-center{
      justify-content: center;
    }
    .r-item{
      width: 100%;
      background: #fff;
      color:#33333F;
      font-size: 14px;
      height: auto;
      display: flex;
      flex-direction: row;
      align-items: stretch;
      flex-shrink: 0;
    }
    .r-xh{width: 40px;}
    .r-hllx{width: 100px;}
    .r-hlfl{width: 100px;}
    .r-hlcs{width: calc(100% - 340px);flex-grow: 1;white-space: nowrap;text-overflow: ellipsis;}
    .rtd-hlcs{width: calc(100% - 100px);flex-grow: 1;white-space: nowrap;text-overflow: ellipsis;}
    .r-cz{width: 100px;}
    .pl0{padding-left: 0 !important;}
    .namediv{
      display: flex;
      width: 100px;
      min-height: 35px;
      align-items: center;
      justify-content: center;
      box-sizing: border-box;
    }
    .ritdiv{
      /*display: flex;*/
      width: calc(100% - 100px);
      flex-grow: 1;
      min-height: 35px;
    }
    .ritdivone{
      width: 100%;
      display: flex;
      flex-direction: row;
      min-height: 35px;
    }
  }
  .right-content {
    background: #fff;
    overflow: hidden;
    display: flex;
    flex-direction: column;
  }
  .search{box-sizing:border-box;padding:0 15px;max-width: 300px;}
  .rightbtn{box-sizing:border-box;padding:0 15px;justify-self: flex-end;}
  .con-title{
    height:60px;
    display: flex;
    flex-direction: row;
    align-items: center;
    background: #fff;
  }
  .model-title{
    height: 30px;
    width: auto;
    text-align: center;
    line-height: 30px;
    justify-content: center;
    box-sizing: border-box;
    display: flex;
    align-items: center;
    color:#fff;
    background:rgba(18,182,201,1);
    border-bottom-right-radius: 30px;
    border-top-right-radius: 30px;
    min-width: 95px;
  }
  .ml-10{margin-left: 10px;}
  .operate{cursor: pointer;}


  .add-div {
    box-sizing: border-box;
    width: 100%;
    min-height: 100%;
    height: auto;
    padding: 18px;
    /*overflow: hidden;*/
    /*overflow-y: auto;*/
  }
</style>
