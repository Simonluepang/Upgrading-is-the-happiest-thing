<template>
<div class="selectbox b-box" @click="openShow">
  <div class="select-show d-flex a-center" :class="{placeHolder:!selectedItem.displaySelect}">{{selectedItem.displaySelect || '请选择...'}}</div>
  <ul class="select-options b-box myscroll" v-if="show">
    <li class="options-item nodata" @click="show=false" v-if="!data.length">{{nodata}}</li>
    <li class="options-item" @click="selectOption(item)" v-for="(item,index) in data" :key="index">
      <slot :item="item">
        {{item.displaylabel}}
      </slot>
    </li>
  </ul>
</div>

</template>

<script>
export default {
  name: 'DropDown',
  props:{
    nodata:{
      type:String,
      default:"没有选项"
    },
    data:{
      default(){
        return [
          // {
          //   value:'1',
          //   displaylabel:"测试",
          //   displaySelect:'测试'
          // }
        ];
      },
      type:Array,
    }
  },
  data(){
    return {
      show:false,
      selectedItem:{},
    }
  },
  filters:{
    searchFilter(arr){
      return arr
    }
  },
  mounted(){
    document.addEventListener('click',this.gloableClickHandle.bind(this));
  },
  destroyed(){
    document.removeEventListener('click',this.gloableClickHandle);
  },
  methods:{
    openShow(){
      this.show = true;
    },
    selectOption(item){
      this.show = false;
      this.selectedItem = {...item}
    },
    gloableClickHandle(e){
      if(!this.$el.contains(e.target)) {
        this.show = false;
      }
    }
  }
}
</script>
<style lang="scss" scoped>
.placeHolder{
  color: #aaa;
}
  .selectbox{
    display: inline-block;
    min-width: 200px;
    height: 35px;
    padding: 5px 10px;
    position: relative;
    background-color: #fff;
    color: #555;
    border: 1px solid #aaa;
    border-radius: 4px;	
    z-index: 2;
    box-sizing: border-box;
    cursor: pointer;
    &::before{
      content: "";
      position: absolute;
      width: 0;
      height: 0;
      border: 7px solid transparent;
      border-top-color: #ccc;
      top: 13px;
      right: 10px;
      cursor: pointer;
      z-index: -2;
    }
    .select-show{
      height: 100%;
    }
    .select-options{
      position: absolute;
      width: 100%;
      min-height: 30px;
      max-height: 200px;
      overflow: auto;
      top: 36px;
      left: 0;
      padding: 5px 0px;
      border: 1px solid #aaa;
      border-radius: 4px;	
      background: #fff;
      .options-item{
        padding: 5px 10px;
        cursor: pointer;
        &:hover{
          background: #f1f1f1
        }
      }
      .nodata{
       cursor: no-drop;
      }
    }
  }
  .select {
		display: inline-block;
		width: 300px;
		position: relative;
		vertical-align: middle;
		padding: 0;
		overflow: hidden;
		background-color: #fff;
		color: #555;
		border: 1px solid #aaa;
		text-shadow: none;
		border-radius: 4px;	
		transition: box-shadow 0.25s ease;
		z-index: 2;
	}
 
	.select:hover {
		box-shadow: 0 1px 4px rgba(0, 0, 0, 0.15);
	}
 
	.select:before {
    content: "";
    position: absolute;
    width: 0;
    height: 0;
    border: 7px solid transparent;
    border-top-color: #ccc;
    top: 13px;
    right: 10px;
    cursor: pointer;
    z-index: -2;
	}
	.select select {
		cursor: pointer;
		padding: 6px;
		width: 100%;
		border: none;
		background: transparent;
		background-image: none;
		-webkit-appearance: none;
		-moz-appearance: none;
	}
 
	.select select:focus {
		outline: none;
	}

</style>

