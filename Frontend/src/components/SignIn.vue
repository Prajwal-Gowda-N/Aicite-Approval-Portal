<script setup>
import router from '@/router';
import axios from 'axios';

import { ref } from 'vue';


const username=ref('')
const password=ref('')







const addForm= async()=>{
     const response={
        username:username.value,
        password:password.value
     } 
     try {
        const res = await axios.post("http://127.0.0.1:8000/signup/",response)
        console.log(res.data.data.token)
        localStorage.setItem("token",res.data.data.token)
     } catch (error) {
        console.log(error)
     }
     username.value=""
     password.value=""
}



// const signin=()=>{
  
//   watch(token, (newToken) => {
//     if (newToken === null) {
      
//     } else {
//       localStorage.setItem("token", newToken); 
//     }
//   }); 
//   }
</script>


<template>
   <form @submit.prevent="addForm" class="flex flex-col space-y-6 w-2/3 max-w-2xl h-auto mt-16 mx-auto p-8 bg-gradient-to-r from-red-100 via-red-200 to-red-300 shadow-lg rounded-xl border border-gray-200">
     <div class="flex flex-col">
       <label for="Username" class="text-lg font-semibold text-black mb-2">Username:</label>
       <input 
         type="text" 
         name="Username" 
         class="border border-red-500 rounded-md p-3 w-full focus:ring-2 focus:ring-red-600 focus:outline-none"
         v-model="username" 
         required 
         placeholder="Enter your username"
       />
     </div>
 
     <div class="flex flex-col">
       <label for="Password" class="text-lg font-semibold text-black mb-2">Password:</label>
       <input 
         type="password" 
         name="Password" 
         class="border border-red-500 rounded-md p-3 w-full focus:ring-2 focus:ring-red-600 focus:outline-none"
         v-model="password" 
         required 
         placeholder="Enter your password"
       />
     </div>
 
     <div class="w-full mt-6">
       <button 
         type="submit" 
         class="w-full py-3 bg-red-600 text-white rounded-md text-lg font-semibold hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-red-600 transition duration-200"
       >
         Submit
       </button>
     </div>
   </form>
 </template>


<style scoped>



input, button {
  transition: all 0.3s ease-in-out;
}

input:focus, button:hover {
  transform: translateY(-2px); 
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}
</style>