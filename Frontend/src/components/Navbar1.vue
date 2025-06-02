<script setup>
import { ref, watch } from 'vue';
import { useRouter } from 'vue-router';

const imageUrl3 = new URL('@/assets/logo.webp', import.meta.url).href;
const router = useRouter();


const isHovered = ref(false);

const isModalVisible = ref(false);  
const token = ref(localStorage.getItem("token"));

watch(token, (newToken) => {
  if (newToken) {
    localStorage.setItem('token', newToken); // Store token in localStorage
  } else {
    localStorage.removeItem('token'); // Remove token if it's null or logged out
  }
});

const handleMouseEnter = () => {
  isHovered.value = true;
  if (token.value === null) {
    
    isModalVisible.value = true;
  }
};

const handleMouseLeave = () => {
  isHovered.value = false;
};


const Logout = () => {
  token.value = null; // Set token to null
  router.push('/login')
  
};




const closeModal = () => {
  isModalVisible.value = false
  
  
};
</script>

<template>
  <Navbar class="flex flex-row bg-red-600 justify-around w-full h-16 border-b-2 border-solid border-red-700 shadow-lg">
    <div class="flex flex-row w-2/6">
      <img :src="imageUrl3" alt="Mother Teresa"  class="w-2/6 "/>
    </div>
    <div class="flex flex-row w-11/12 space-x-48">
    <div class="w-24 h-10 text-white mt-3 rounded-lg hover:bg-red-700 hover:shadow-2xl hover:scale-110 transition-all duration-300">
      <RouterLink to="/" class="block text-center py-2 font-semibold">Home</RouterLink>
    </div>

    <div class="w-24 h-10 text-white mt-3 rounded-lg hover:bg-red-700 hover:shadow-2xl hover:scale-110 transition-all duration-300">
      <RouterLink to="/About/" class="block text-center py-2 font-semibold">About</RouterLink>
    </div>

    <div class="w-24 h-10 text-white mt-3 rounded-lg hover:bg-red-700 hover:shadow-2xl hover:scale-110 transition-all duration-300" 
         @mouseenter="handleMouseEnter" 
         @mouseleave="handleMouseLeave">
      <RouterLink to="/Approval/" class="block text-center py-2 font-semibold">Approval</RouterLink>
    </div>

    <div class="w-24 h-10 text-white mt-3 rounded-lg hover:bg-red-700 hover:shadow-2xl hover:scale-110 transition-all duration-300">
      <div>
        <RouterLink v-if="token===null" to="/login/" class="block text-center py-2 font-semibold">SignIn</RouterLink>
        <RouterLink v-if="token!==null" to="/login/" @click="Logout" class="block text-center py-2 font-semibold">Logout</RouterLink>
        
      </div>
    </div>
    <!-- <div class="w-24 h-10 text-white mt-3 rounded-lg hover:bg-red-700 hover:shadow-2xl hover:scale-110 transition-all duration-300">
      <div>
        <button @click="logout()">Logout</button>
      </div>
    </div> -->
  </div>
  </Navbar>


  <div v-if="isModalVisible" class="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center z-50">
    <div class="bg-white p-6 rounded-lg w-1/3">
      <h2 class="text-xl text-center text-red-600 font-semibold mb-4">Login Required</h2>
      <p class="text-center mb-4">You must be logged in to access the Approval section. Please sign in first.</p>
      <div class="text-center">
        <button @click="closeModal" class="bg-red-600 text-white px-4 py-2 rounded-md hover:bg-red-700">Close</button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.Navbar {
  font-family: 'Arial', sans-serif;
  letter-spacing: 1px;
}

.Navbar a {
  transition: transform 0.3s ease, box-shadow 0.3s ease, background-color 0.3s ease;
}

.Navbar a:hover {
  transform: translateY(-5px);
  box-shadow: 0 6px 15px rgba(0, 0, 0, 0.2);
  background-color: #e53e3e; 
}

.Navbar .w-24:hover {
  transform: scale(1.1);
  transition: transform 0.3s, box-shadow 0.3s ease-in-out;
}


.fixed {
  position: fixed;
}

.bg-opacity-50 {
  background-color: rgba(0, 0, 0, 0.5);
}

.bg-white {
  background-color: white;
}

.text-red-600 {
  color: #e53e3e; 
}

button {
  cursor: pointer;
}
</style>






