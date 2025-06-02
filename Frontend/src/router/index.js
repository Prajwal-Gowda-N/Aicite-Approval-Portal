import App from "@/App.vue";
import { createRouter, createWebHistory } from "vue-router";
import About from "@/views/About.vue";
import App1 from "@/views/App1.vue";
import Home from "@/views/Home.vue";
import Sign from "@/views/Sign.vue";
import App2 from "@/views/App2.vue";
import LoggedIn from "@/views/LoggedIn.vue";

const router=createRouter(
    {history:createWebHistory(import.meta.env.BASE_URL),
    routes:[
        {
            path: '/Approval/',
            name: 'App1',
            component: App1
        },

        {
            path: '/Approval1/',
            name: 'App2',
            component: App2
        },
        {
            path:'/',
            name:'Home',
            component:Home
        },
        {
            path:'/login/',
            name:'login',
            component:Sign
        },
        {
            path:'/logged/',
            name:'loggedIn',
            component:LoggedIn
        },
        {
            path:'/About/',
            name:'About',
            component:About
        },
    ]}
)


router.beforeEach((to, from, next) => {
    const token = localStorage.getItem('token');
    
    // Check if the route requires authentication
    if (to.path === '/Approval/' && !token) {
      // If there's no token and the user tries to access /Approval, redirect to login
      next('/login');
    } else {
      // If there's a token or the route doesn't require it, allow the navigation
      next();
    }
  });

export default router