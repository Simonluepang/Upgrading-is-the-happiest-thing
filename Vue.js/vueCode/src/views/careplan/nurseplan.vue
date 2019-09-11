<template>
    <div class="page-main">
      <div style="width: 200px;margin: 20px;">
        <drop-ctrl ctrltype="single" :lines="false"></drop-ctrl>
      </div>
    </div>
</template>

<script>
  import dropCtrl from '@/components/doc-com/drop-ctrl'
   export default {
    name: 'nurseplan',
    components:{dropCtrl},
  };
</script>

<style scoped>

</style>
