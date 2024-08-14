import './assets/main.css'
import './index.css'

import { createApp } from 'vue'
import App from './App.vue'
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import  {library} from "@fortawesome/fontawesome-svg-core"
import { faHouse, faHeart,faMagnifyingGlass,faBackward, 
    faBackwardStep, faCirclePause, faCirclePlay, 
    faForwardStep, faForward } from '@fortawesome/free-solid-svg-icons';


library.add(faHouse,faHeart,faMagnifyingGlass,faBackward,faBackwardStep,faCirclePause,faCirclePlay
    ,faForwardStep,faForward
)

createApp(App)
.component("font-awesome-icon", FontAwesomeIcon)
.mount('#app')
