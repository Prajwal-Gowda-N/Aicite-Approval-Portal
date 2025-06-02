<script setup>
import { ref } from 'vue';
import axios from 'axios';
const Program=ref('')
const Level=ref('')
const Courses=ref(null)
const Intake=ref(null)
const Maximum=ref(null)
const Division=ref(null)
const Email=ref('')



const addForm= async()=>{
      const response={
        Program:Program.value,
        Level:Level.value,
        Courses:Courses.value,
        Intake:Intake.value,
        Maximum:Maximum.value,
        Division:Division.value,
        Email:Email.value
      }
      console.log(response)

      try {
         const res= await axios.post('http://127.0.0.1:8000/Approval/',response)
      } catch (error) {
         console.log(error)
      }

      Program.value=""
      Level.value=""
      Courses.value=null
      Intake.value=null
      Division.value=null
      Maximum.value=null
      Email.value=""
}

</script>

<template>
    <form @submit.prevent="addForm" class="border flex flex-col space-y-6 w-2/3 max-w-2xl mt-16 mx-auto p-6 bg-white shadow-lg rounded-lg border-2 border-red-500">
    
      <div class="flex flex-col space-y-2 w-full">
        <label for="Program" class="text-lg font-semibold text-gray-700 text-left">Program:</label>
        <select class="border border-red-500 rounded-md p-3 text-lg focus:outline-none focus:ring-2 focus:ring-red-600 w-full" id="Program" v-model="Program" required>
          <option value="Engineering">Engineering and Technology</option>
          <option value="Applied">Applied Arts and Crafts</option>
          <option value="Design">Design</option>
          <option value="Hotel">Hotel Management & Catering Technology</option>
          <option value="Computer">Computer Applications</option>
          <option value="Management">Management</option>
          <option value="Planning">Planning</option>
        </select>
      </div>
  

      <div class="flex flex-col space-y-2 w-full">
        <label for="Level" class="text-lg font-semibold text-gray-700 text-left">Level:</label>
        <select class="border border-red-500 rounded-md p-3 text-lg focus:outline-none focus:ring-2 focus:ring-red-600 w-full" id="Level" v-model="Level" required>
          <option value="Diploma">Diploma</option>
          <option value="Undergraduate">Undergraduate</option>
          <option value="Postgraduate">Postgraduate</option>
        </select>
      </div>
  
  
      <div class="flex flex-col space-y-2 w-full">
        <label for="Courses" class="text-lg font-semibold text-gray-700 text-left">Courses:</label>
        <select class="border border-red-500 rounded-md p-3 text-lg focus:outline-none focus:ring-2 focus:ring-red-600 w-full" id="Courses" v-model="Courses" required>
          <option :value="6">6</option>
          <option :value="5">5</option>
          <option :value="3">3</option>
        </select>
      </div>
  
 
      <div class="flex flex-col space-y-2 w-full">
        <label for="Intake" class="text-lg font-semibold text-gray-700 text-left">Intake per Division:</label>
        <select class="border border-red-500 rounded-md p-3 text-lg focus:outline-none focus:ring-2 focus:ring-red-600 w-full" id="Intake" v-model="Intake" required>
          <option :value="60">60</option>
          <option :value="30">30</option>
          <option :value="15">15</option>
          <option :value="120">120</option>
        </select>
      </div>
  
     
      <div class="flex flex-col space-y-2 w-full">
        <label for="Maximum" class="text-lg font-semibold text-gray-700 text-left">Maximum Intake:</label>
        <select class="border border-red-500 rounded-md p-3 text-lg focus:outline-none focus:ring-2 focus:ring-red-600 w-full" id="Maximum" v-model="Maximum" required>
          <option :value="360">360</option>
          <option :value="120">120</option>
          <option :value="90">90</option>
          <option :value="150">150</option>
          <option :value="180">180</option>
        </select>
      </div>
  
     
      <div class="flex flex-col space-y-2 w-full">
        <label for="Division" class="text-lg font-semibold text-gray-700 text-left">Division:</label>
        <select class="border border-red-500 rounded-md p-3 text-lg focus:outline-none focus:ring-2 focus:ring-red-600 w-full" id="Division" v-model="Division" required>
          <option :value="6">6</option>
          <option :value="12">12</option>
          <option :value="5">5</option>
          <option :value="3">3</option>
          <option :value="1">1</option>
        </select>
      </div>
  
     
      <div class="flex flex-col space-y-2 w-full">
        <label for="email" class="text-lg font-semibold text-gray-700 text-left">Email:</label>
        <input type="email" v-model="Email" class="border border-red-500 rounded-md p-3 text-lg focus:outline-none focus:ring-2 focus:ring-red-600 w-full" id="email" />
      </div>
  
     
      <div class="flex justify-center w-full mt-6">
        <button type="submit" class="bg-red-600 text-white font-semibold py-3 px-12 rounded-md shadow-md hover:bg-red-700 transition-all duration-300 transform hover:scale-105">
          Submit
        </button>
      </div>
    </form>
  </template>
  
  <style scoped>
 
  form {
    display: flex;
    flex-direction: column;
    align-items: flex-start; 
    padding: 2rem;
    background-color: white;
    border-radius: 12px;
    box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
    border: 2px solid #e53e3e;
    max-width: 700px;
    width: 100%;
  }
  
 
  h2 {
    color: #e53e3e;
    font-size: 2.5rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1px;
  }
  
 
  .mb-6 {
    margin-bottom: 1.5rem;
  }
  
 
  label {
    font-size: 1.1rem;
    color: #4a4a4a;
    font-weight: 600;
    text-align: left;
  }
  
  
  input, select {
    font-size: 1.1rem;
    padding: 1rem;
    border-radius: 8px;
    border: 2px solid #e53e3e; 
  }
  
  input:focus, select:focus {
    outline: none;
    box-shadow: 0 0 5px rgba(255, 0, 0, 0.3);
    border-color: #e53e3e;
  }
  

  button {
    background-color: #e53e3e;
    color: white;
    font-size: 1.1rem;
    padding: 12px 24px;
    border-radius: 8px;
    cursor: pointer;
    transition: all 0.3s ease;
  }
  
  button:hover {
    background-color: #c53030;
    transform: scale(1.05);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  }
  </style>
  
  
  