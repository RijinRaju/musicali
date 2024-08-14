<template>
    <aside class="left-sidebar">
        <!-- Your sidebar content here -->

        <header>
            <div class="sidebar-header">
                <p>Musicali</p>
            </div>
        </header>
        <div class="menu">
            <div class="menu-item grid  grid-flow-col">
                <div>
                    <font-awesome-icon icon="house" />
                </div>
                <div>
                    Dashboard
                </div>

            </div>
            
            <div class="menu-item grid grid-flow-col">
                <div>
                    <font-awesome-icon icon="heart" />
                </div>
                <div>
                    Favorite
                </div>
                
            </div>
            <!-- Add other menu items -->
        </div>
    </aside>
</template>


<style scoped>
.left-sidebar {
    width: 230px;
    /* Adjust the width as needed */
    background-color: #111111;
    /* Background color similar to the design */
    color: white;
    display: flex;
    flex-direction: column;
    padding: 20px;
    /* Add padding for spacing */
    height: 100vh;
    /* Full viewport height */
    position: fixed;
    /* Keeps the sidebar fixed on the left */
    top: 0;
    left: 0;
}

.menu {
    display: flex;
    flex-direction: column;
    margin-top: 50px;
    padding: 5px;
}

.menu-item {
    margin: 10px 0;
    padding: 10px;
    cursor: pointer;
    transition: background-color 0.3s;
}

.menu-item:hover {
    background-color: #880daf;
    /* Change color on hover */
    border-radius: 5px;
}

header {
    display: flex;
    justify-content: center;
}

.sidebar-header {
    font-weight: bold;
    font-size: x-large;
    font-family: Arial, Helvetica, sans-serif;
}
</style>