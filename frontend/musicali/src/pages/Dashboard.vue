<template>
    <div class="dashboard-main grid grid-flow-col">

        <div>
            <aside>
                <div class="side_wrapper">
                    <LeftSidebar/>
                </div>
            </aside>
           
        </div>

        <div>
            <main>
                <searchbar/>
                
            </main>
        </div>

        <div>
            <footer class="footer-main">
                <FooterControlls title="Gangster paradise" singer="somebody"/>
            </footer>
        </div>

    </div>
</template>


<script setup>
import LeftSidebar from '../components/LeftSideBar.vue'
import searchbar from '../components/searchBar.vue'
import FooterControlls from '../components/FooterControlls.vue';
</script>
<style scoped>

.dashboard-main{
    display: flex;
    flex-direction: column;
    
}

.footer-main {
  width: 100%;
  height: 60px; /* Adjust the footer height */
  display: flex;
  z-index: 999;
  position: fixed;
  left: 0%;
  bottom: 0%;
}
</style>
