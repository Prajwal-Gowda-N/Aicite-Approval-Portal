<script setup>
        const imageUrl3 = new URL('@/assets/Intake.png', import.meta.url).href;


</script>

<template>
    <div class="flex flex-col mx-auto my-auto mt-6 w-10/12 h-full p-6 border rounded-md shadow-lg bg-white">
      <!-- Header Section -->
      <div class="text-center mb-6">
        <h1 class="text-2xl font-semibold text-gray-700">Allowed Acite Intake</h1>
      </div>
  
      <!-- Image Section (Increased size) -->
      <div class="flex justify-center mb-6">
        <img :src="imageUrl3" alt="Mother Teresa" class="w-4/6 h-64 rounded-lg shadow-md"/>
      </div>
  
      <!-- Next Button Section -->
      <div class="flex justify-center">
        <RouterLink to="/Approval1/" class="text-center py-2 px-6 font-semibold bg-red-600 text-white rounded-md shadow-lg hover:bg-red-700 transition duration-300 ease-in-out">
          Next
        </RouterLink>
      </div>
    </div>
  </template>
  
  <style scoped>
  /* Styling for the container */
  .bg-white {
    background-color: #fff;
  }
  
  /* Header styling */
  h1 {
    font-size: 1.5rem;
    font-weight: 600;
    color: #333;
  }
  

  img {
    max-width: 100%;
    border-radius: 0.5rem;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  }
  

  button, .router-link-active {
    font-weight: 600;
    color: #fff;
    background-color: #e53e3e;
    padding: 0.75rem 2rem;
    border-radius: 0.5rem;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    transition: all 0.3s ease;
  }
  
  button:hover, .router-link-active:hover {
    background-color: #c53030;
    transform: translateY(-3px);
  }
  </style>
  
  