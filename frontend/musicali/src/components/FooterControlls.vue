<template>
<div class="footer-main grid grid-rows-3 grid-flow-col gap-6">
    <span>
        <songImage/>
    </span>
    <span>
        <h4>{{title}}</h4>
        <p>{{singer}}</p>

    </span>
    <span class="controlls grid  grid-flow-col gap-4">
        <button><font-awesome-icon icon="backward" size="lg" /> </button>
        <button><font-awesome-icon icon="backward-step" size="lg" /></button>
        <button @click="pause = !pause">
            <font-awesome-icon  icon="circle-pause" v-if="pause" size="lg"/>
            <font-awesome-icon icon="circle-play" v-else size="lg" />
        </button>
        <button><font-awesome-icon icon="forward-step" size="lg" /></button>
        <button><font-awesome-icon icon="forward" size="lg" /></button>
        
    </span>
    <span>

        
    </span>

</div>

</template>
<script setup>

import songImage from '../components/songImage.vue'


defineProps({
    title: String,
    singer: String,
})




</script>

<style scoped>

.footer-main{
    color:white;
    width:100%;
    height: 40%;
    display: flex;
    background-color: #000000;
}

.controlls{

}
button{
    width: 35px;
}


</style>