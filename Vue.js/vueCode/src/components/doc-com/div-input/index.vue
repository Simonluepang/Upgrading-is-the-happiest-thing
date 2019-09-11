<template>
  <div class="div-input-wrap"
    :class="{bb:bottomBorder}"
    :contentEditable="isEdit" ref="DivInput"
    @keydown.enter="enterKey"
    @focus="divFocus"
    @blur="divBlur"
    @input="divKeyup"
    v-html="innerText"
    >
  </div>
</template>

<script>
export default {
  name: 'DivInput',
  props:{
    value:"",
    bottomBorder:{
      type:Boolean,
      value:false
    },
    isEdit:{
      type:Boolean,
      default:true,
    },
    service:{
      type:Object,
      default(){
        return {}
      }
    },
  },
  watch:{
    value(val){
      console.log(val)
      if (this.isChange) {
        this.innerText = this.value
      }
    }

  },
  data(){
    return {
      oldvalue:"",
      newValue:"",
      timmer:null,
      innerText: this.value,
      isChange: true
    }
  },
  methods:{
    divFocus(e){
      this.isChange = false
      if(!this.$refs.DivInput.innerHTML){
        let html = `<div></br></div>`;
        this.$refs.DivInput.innerHTML = html;
      }
      this.isChange = false
      this.$emit('divFocus',e)
    },
    divBlur(e){
      this.isChange = true
      this.$emit('divBlur',e)
    },
    divKeyup(e) {
      if(this.timmer) {
        clearTimeout(this.timmer);
        this.timmer = null;
      }
      this.newValue = this.$refs.DivInput.innerText;
      if(this.oldvalue !=this.newValue) {
        this.timmer = setTimeout(()=>{
          this.oldvalue = this.newValue;
          clearTimeout(this.timmer);
          this.timmer = null;
          this.$emit('input',this.newValue);
          this.$emit('divChange',this.newValue);
        },300)
      }
    },
    enterKey(e){
      e.preventDefault();
      return
    }
  }
}
</script>
<style lang="scss" scoped>
  .div-input-wrap{
    min-width: 40px;
    height: 20px;
    line-height: 20px;
  }
  .bb{
     border-bottom: 1px solid #333;
  }
</style>

