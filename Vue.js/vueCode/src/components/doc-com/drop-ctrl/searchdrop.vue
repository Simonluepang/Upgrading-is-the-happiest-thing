<template>
  <!--<div class="drop-main" ref="sel" @keyup.down="keyDownFn"
       @keyup.enter="keyRightFn"
       @keyup.right="keyRightFn"
       @keyup.up="keyUpFn">-->
  <div class="drop-main" ref="sel">
    <div>
      <div @click="tiggerDrop" class="div-input drop-input nowarp"
           :contenteditable="canEdit"
           @blur="giveValue"><span class="place" v-if="checkStr===''">{{place}}</span>{{checkStr}}
      </div>
    </div>
    <div class="drop-content1" :class="position==='bottom'?'drop-bottom':'drop-top'" v-if="dropStatus">
      <div class="search">
        <input type="text" class="search-input" :placeholder="place" v-model="searchkeyword"/>
      </div>
      <div class="drop-scrollcont myscroll">
        <div class="drop-item" v-for="(md,indx) in alloperate" :key="'dit_'+indx"
             :class="{'drop-active':checkArr.indexOf(md)>-1&&ctrltype==='signle','drop-check':checkArr.indexOf(md)>-1&&ctrltype==='multi'}"
             @click="checkItem(md)">
          <div class="checkbox" v-if="ctrltype==='multi'"></div>
          <div class="drop-item-msg">{{md}}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'index',
    props: {
      ctrltype: {
        type: String,
        // default: 'multi'
        default: 'signle'
      },
      alloperate: {
        type: Array,
        default() {
          return ['11', '22', '33'];
        }
      },
      checkLst: {
        type: String,
        default: ''
      },
      searchplace:{
        type:String,
        default:""
      },
      place:{
        type:String,
        default:""
      },
      canEdit:{
        type:Boolean,
        default:false
      }
    },
    data() {
      return {
        dropStatus: false,//下拉是否展开
        position: 'bottom',
        checkArr: [],
        checkStr: '',
        searchkeyword:""
        // nowfocus: ''
      };
    },
    mounted() {
      this.computePos();
      document.addEventListener('click', (e) => {
        if (!this.$el.contains(e.target)) this.dropStatus = false;
      });
    },
    watch: {
      checkLst: function () {
        if (this.checkLst !== '') {
          this.checkArr = this.checkLst.split(',');
          this.checkStr = this.checkLst;
        /*  if (this.ctrltype === 'signle') {
            this.nowfocus = this.checkStr;
          }*/
        } else {
          this.checkArr = [];
          this.checkStr = '';
          // this.nowfocus = '';
        }
      },
      searchkeyword:{
        handler(){
          this.$emit("reloadData",this.searchkeyword)
        }
      }
    },
    methods: {
      tiggerDrop() {
        this.dropStatus = !this.dropStatus;
      },

      hideDrop() {
        this.dropStatus = false;
      },
      checkItem(md) {
        if (this.ctrltype === 'multi') {
          let indx = this.checkArr.indexOf(md);
          if (indx > -1) {
            this.checkArr.splice(indx, 1);
          } else {
            this.checkArr.push(md);
            this.checkStr = this.checkArr.toString();
          }
        } else {
          this.checkArr = [];
          this.checkArr.push(md);
          this.checkStr = this.checkArr.toString();
          // this.nowfocus = this.checkArr.toString();
          this.hideDrop();
        }
      },
      giveValue() {
        this.$emit('change', this.checkArr);
      },
      keyDownFn() {
        if (this.dropStatus) {
          var indx = this.alloperate.indexOf(this.nowfocus);
          if (indx > -1 && indx + 1 < this.alloperate.length) {
            this.nowfocus = this.alloperate[indx + 1];
          } else {
            this.nowfocus = this.alloperate[0];
          }
        }
      },
      keyRightFn() {
        this.checkItem(this.nowfocus);
      },
      keyUpFn() {
        if (this.dropStatus) {
          var indx = this.alloperate.indexOf(this.nowfocus);
          if (indx > 0) {
            this.nowfocus = this.alloperate[indx - 1];
          } else {
            this.nowfocus = this.alloperate[0];
          }
        }
      },
      getElementTop(element) {
        var actualTop = element.offsetTop;
        var current = element.offsetParent;
        while (current !== null) {
          actualTop += current.offsetTop;
          current = current.offsetParent;
        }
        return actualTop;
      },
      computePos() {
        let elHeight = this.$refs.sel.offsetHeight;
        let absPos = this.getElementTop(this.$refs.sel);

        let docScrollHei = document.body.scrollTop
          || document.documentElement.scrollTop || 0;

        let docHeight = document.documentElement.clientHeight
          || document.body.clientHeight || 0;

        if ((elHeight + absPos + 200 - docScrollHei) > docHeight) {
          this.position = 'top';
        } else {
          this.position = 'bottom';
        }
      }
    }
  };
</script>

<style lang="scss" scoped>
  .nowarp {
    white-space: nowrap;
    overflow-x: auto;
  }

  .drop-main {
    position: relative;
    width: 100%;

    .drop-content1 {
      position: absolute;
      left: 0;
      border: 1px solid #e6e7ef;
      border-radius: 3px;
      background: #fff;
      box-shadow: 0 0 3px 1px rgba(0,0,0,0.1);
      width: 100%;
      padding: 5px 0;
      height: 350px;
      box-sizing: border-box;
      overflow: hidden;
      z-index: 100;
      .search{height: 40px;box-sizing:border-box;padding:0 15px;display: flex;align-items: center;}

      .drop-scrollcont{
        width: 100%;
        height: calc(100% - 40px);
        box-sizing: border-box;
        overflow: hidden;
      }
      .drop-item {
        height: auto;
        min-height: 30px;
        width: 100%;
        padding: 0 10px;
        box-sizing: border-box;
        background: #fff;
        cursor: pointer;
        font-size: 14px;
        display: flex;
        align-items: center;
        flex-direction: row;

        .checkbox {
          width: 14px;
          height: 14px;
          background: url("../../../assets/img/operate/weixuanzhong.png") no-repeat;
          background-size: 100% 100%;
          flex-shrink: 0;
        }

        /* .check-ok {
           width: 14px;
           height: 14px;
           background: url("../../../assets/img/operate/xuanzhong.png") no-repeat;
           background-size: 100% 100%;
           flex-shrink: 0;
         }*/

        .drop-item-msg {
          flex-grow: 1;
          box-sizing: border-box;
          padding: 3px 0;
          padding-left: 10px;
          display: flex;
          align-items: center;
          font-size: 14px;
        }
      }

      .drop-active {
        background-color: #f7f8fc;
        color: #0db4c7;
      }

      .drop-check {
        .checkbox {
          background: url("../../../assets/img/operate/xuanzhong.png") no-repeat;
          background-size: 100% 100%;
        }
      }

      .drop-focus {
        background: #f2f2f2;
      }

      .drop-item:hover {
        background: #F7F8FC;
        transition: .5s all;
      }
    }

    .drop-bottom {
      top: calc(100% + 5px);
    }

    .drop-top {
      bottom: calc(100% + 5px);
    }
  }
</style>
