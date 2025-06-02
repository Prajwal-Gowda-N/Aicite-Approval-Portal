<script setup>
const imageUrl3 = new URL('@/assets/aicte.jpg', import.meta.url).href;
</script>


<template>
    <div class="min-h-screen bg-gradient-to-r from-red-50 via-red-100 to-red-200 py-8">
     
      <section class="container mx-auto px-6 py-12 bg-white rounded-xl shadow-lg mt-12 mb-16 hover:shadow-xl transition-all duration-300 ease-in-out">
        <div class="text-center mb-8">
         
          <h2 class="text-4xl font-medium text-red-600 mb-4">Our History</h2>
          <p class="text-lg text-gray-700 max-w-3xl mx-auto mb-6 leading-relaxed font-serif">
            The beginning of formal technical education in India can be dated back to the mid-19th century. Major policy initiatives in the pre-independence period played a crucial role, including the establishment of key institutions like IISc in Bangalore, the Institute for Sugar, Textile & Leather Technology in Kanpur, and the N.C.E. in Bengal.
          </p>
         
          <div class="text-center mb-12 flex justify-center">
            <img :src="imageUrl3" alt="Mother Teresa" class=" "/>
          </div>
        </div>
        
       
        <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          <div class="bg-white p-6 rounded-lg shadow-lg bg-opacity-90 border border-gray-200 hover:scale-105 transform hover:translate-y-2 hover:shadow-xl transition-all duration-300 ease-in-out">
            <h3 class="text-2xl font-semibold text-red-600 mb-4">Initial Set-up</h3>
            <p class="text-gray-700 mb-4">
              AICTE was formed in November 1945 as a national apex advisory body to assess and develop technical education in India. The goal was to coordinate efforts and ensure the sustainable growth of technical education.
            </p>
            <p class="text-gray-700">
              As outlined in the National Policy of Education (1986), AICTE's responsibilities include the planning, formulation, and maintenance of norms & standards for the sector.
            </p>
          </div>
  
         
          <div class="bg-white p-6 rounded-lg shadow-lg bg-opacity-90 border border-gray-200 hover:scale-105 transform hover:translate-y-2 hover:shadow-xl transition-all duration-300 ease-in-out">
            <h3 class="text-2xl font-semibold text-red-600 mb-4">Key Milestones</h3>
            <ul class="list-disc list-inside text-gray-700">
              <li><strong>1943:</strong> Constitution of the Technical Education Committee of the Central Advisory Board of Education (CABE).</li>
              <li><strong>1944:</strong> Preparation of the Sergeant Report to address technical education challenges.</li>
              <li><strong>1945:</strong> Formation of the All India Council for Technical Education (AICTE).</li>
            </ul>
          </div>
  
       
          <div class="bg-white p-6 rounded-lg shadow-lg bg-opacity-90 border border-gray-200 hover:scale-105 transform hover:translate-y-2 hover:shadow-xl transition-all duration-300 ease-in-out">
            <h3 class="text-2xl font-semibold text-red-600 mb-4">The AICTE Act of 1987</h3>
            <p class="text-gray-700 mb-4">
              The AICTE Act (No. 52 of 1987) formalized the establishment of AICTE with a focus on regulating and promoting technical education. The Act ensures the development and maintenance of norms and standards in technical education across India.
            </p>
            <p class="text-gray-700 mb-4">
              The Act extends AICTE's role to various disciplines, including Engineering, Technology, Architecture, Management, Pharmacy, and more.
            </p>
            <a href="#" class="text-red-600 underline hover:text-red-800 transition-all duration-300">Download the AICTE Act</a>
          </div>
        </div>
  
      
        <div class="mt-12 text-center">
          
          <h3 class="text-3xl font-medium text-red-600 mb-4">Role of National Working Group</h3>
          <p class="text-lg text-gray-700 max-w-3xl mx-auto">
            In response to the rapid expansion of technical institutions, the Ministry of Human Resource Development established the National Working Group to strengthen AICTE's statutory powers. The group's recommendations led to AICTE's restructuring, empowering it to oversee technical education and ensure standards were upheld.
          </p>
        </div>
      </section>
  
   
      <section class="bg-red-600 text-white py-12 mt-16">
        <div class="container mx-auto text-center">
       
          <h2 class="text-3xl font-medium mb-4">Contact Us</h2>
          <p class="text-lg mb-6">Have any questions or need support? Feel free to reach out to us:</p>
          <p class="text-lg mb-2"><strong>Email:</strong> info@aicte-india.org</p>
          <p class="text-lg mb-2"><strong>Phone:</strong> +91-11-12345678</p>
          <button class="bg-white text-red-600 px-6 py-2 rounded-lg shadow-md hover:shadow-lg hover:bg-red-600 hover:text-white transition-all duration-300">
            Get in Touch
          </button>
        </div>
      </section>
  
    
      <footer class="bg-white text-center py-4">
        <p class="text-red-600">&copy; 2024 AICTE. All Rights Reserved.</p>
      </footer>
    </div>
  </template>

<style scoped>

.bg-gradient-to-r {
  background: linear-gradient(to right, rgba(255, 0, 0, 0.1), rgba(255, 0, 0, 0.3));
}

.card:hover {
  transform: translateY(-10px);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
}


.bg-white:hover {
  transform: translateY(-10px);
  box-shadow: 0px 10px 20px rgba(0, 0, 0, 0.15);
  transition: all 0.3s ease-in-out;
}


button:hover {
  background-color: #ef4444; 
  color: white;
  transform: translateY(-2px);
}


.transform {
  transition: transform 0.3s ease-in-out;
}


h2, h3 {
  font-weight: 500;
  text-transform: uppercase;
}

h3 {
  font-size: 2rem;
  color: #e63946;
  font-family: 'Arial', sans-serif;
}

h2 {
  font-size: 2.5rem;
  color: #e63946;
  font-family: 'Roboto', sans-serif;
}


section {
  padding-top: 4rem;
  padding-bottom: 4rem;
}


p {
  font-family: 'Georgia', serif;
  font-size: 1.125rem; 
  line-height: 1.6;
  color: #333;
}

a {
  font-family: 'Arial', sans-serif;
  text-decoration: underline;
}

button {
  font-family: 'Roboto', sans-serif;
  font-weight: 600;
}
</style>