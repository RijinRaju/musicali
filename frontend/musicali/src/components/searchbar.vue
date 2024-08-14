<template>
    <div class="search-main">
        <button><font-awesome-icon icon="magnifying-glass" /></button>
        <input type="text" placeholder="search">
    </div>

</template>


<script>
export default {
    name: 'searchbar'
}
</script>

<style scoped>
.search-main {
    border: 1px solid #303030;
    border-radius: 100px;
    padding: 8px 10px;
    display: flex;
    position: relative;
    bottom: 280px;
    gap: 5px;
    width: 500px;
    margin: 0 auto;
    margin-left: 20em;
    /* margin-top: 10px; */
    background-color: #303030;
}

button {
    background-color: transparent;
    border: none;
    margin: 0;
    cursor: pointer;
}

input {
    border: none;
    outline: none;
    width: 100%;
    background-color: #303030;
}
</style>