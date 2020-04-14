import Vue from "vue/dist/vue.js"
import VueMathPlugin from './VueMathPlugin.js'
import Vuex from 'vuex'

Vue.use(VueMathPlugin)
Vue.use(Vuex)

var store = new Vuex.Store({
    state:{message:"hello!"},
    mutations:{

    },
    actions:{},
    getters:{},
})

var data = {
    item:30
};
var TextComponent = Vue.extend({
    data:function(){
        return data;
    },
    template:
        '<div>'+
            '度数<input v-model="item">'+
        '</div>'
});
Vue.component('text-component',TextComponent)
new Vue({
    el:'#app',
    data:data,
    store:store
})