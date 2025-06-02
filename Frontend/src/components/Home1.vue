<script setup>
const imageUrl1 = new URL('@/assets/CV-Raman-Banner_2.jpg', import.meta.url).href;
const imageUrl2 = new URL('@/assets/har gobing khorana_0.jpg', import.meta.url).href;
const imageUrl3 = new URL('@/assets/Homi Jehangir Bhabha.jpg', import.meta.url).href;
const imageUrl4 = new URL('@/assets/mother teresa.jpg', import.meta.url).href;
</script>

<template>
  <div class="bg-white text-gray-900 min-h-screen font-sans">

    <section class="bg-gradient-to-r from-red-600 to-red-400 text-white py-20 text-center">
      <h2 class="text-4xl font-bold">Welcome to AICTE</h2>
      <p class="mt-4 text-xl">All India Council for Technical Education (AICTE) was set up in November 1945 as a national-level Apex Advisory Body to conduct a survey on the facilities available for technical education and to promote development in the country in a coordinated and integrated manner.</p>
      <RouterLink to="/about" class="mt-6 inline-block px-8 py-3 bg-white text-red-600 rounded-lg text-lg hover:bg-red-100 hover:text-red-800">About AICTE</RouterLink>
    </section>

    
    <section class="py-16">
      <h2 class="text-3xl font-semibold text-center text-red-600 mb-8">Latest Announcements</h2>
      <div class="container mx-auto grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        <div class="bg-white p-6 rounded-lg shadow-lg hover:shadow-2xl transform transition-all duration-300 hover:scale-105">
          <h4 class="text-2xl font-semibold text-red-600">Public Notice for Approval Process 2025-26</h4>
          <p class="mt-2 text-gray-700"><a href="https://www.aicte-india.org/sites/default/files/approval/2025-26/Public%20Notice%202025-26.pdf" class="text-red-600 hover:underline">View Notice</a></p>
        </div>
        <div class="bg-white p-6 rounded-lg shadow-lg hover:shadow-2xl transform transition-all duration-300 hover:scale-105">
          <h4 class="text-2xl font-semibold text-red-600">AICTE Scholarship Application Deadline</h4>
          <p class="mt-2 text-gray-700"><a href="https://aicte-india.org/sites/default/files/Circular%20regarding%20BBA%20and%20BCA%20and%20BMS.pdf" class="text-red-600 hover:underline">Learn More</a></p>
        </div>
        <div class="bg-white p-6 rounded-lg shadow-lg hover:shadow-2xl transform transition-all duration-300 hover:scale-105">
          <h4 class="text-2xl font-semibold text-red-600">Selected List for ATAL Online FDP A.Y 2024-25</h4>
          <p class="mt-2 text-gray-700"><a href="https://www.aicte-india.org/sites/default/files/ATAL%20Online%206%20Days%20Faculty%20Development%20Programme%20Selected%20List%20for%20A.Y%202024-25.pdf" class="text-red-600 hover:underline">View List</a></p>
        </div>
      </div>
    </section>

   
    <section class="bg-gray-100 py-16">
      <h2 class="text-3xl font-semibold text-center text-red-600 mb-8">Scholarship Opportunities</h2>
      <div class="container mx-auto grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        <div class="bg-white p-6 rounded-lg shadow-lg hover:shadow-2xl transform transition-all duration-300 hover:scale-105">
          <h4 class="text-2xl font-semibold text-red-600">National e-Scholarship</h4>
          <p class="text-gray-700 mt-2">A platform to access various scholarships for students.</p>
          <a href="https://scholarships.gov.in/" class="text-red-600 hover:underline mt-4 block">Learn More</a>
        </div>
        <div class="bg-white p-6 rounded-lg shadow-lg hover:shadow-2xl transform transition-all duration-300 hover:scale-105">
          <h4 class="text-2xl font-semibold text-red-600">Pragati and Saksham</h4>
          <p class="text-gray-700 mt-2">Scholarships for girls and differently-abled students.</p>
          <a href="https://scholarships.gov.in/" class="text-red-600 hover:underline mt-4 block">Learn More</a>
        </div>
        <div class="bg-white p-6 rounded-lg shadow-lg hover:shadow-2xl transform transition-all duration-300 hover:scale-105">
          <h4 class="text-2xl font-semibold text-red-600">India Innovation Initiative</h4>
          <p class="text-gray-700 mt-2">India's largest innovation challenges supported by CII and Department of Science & Technology.</p>
          <a href="https://scholarships.gov.in/" class="text-red-600 hover:underline mt-4 block">Learn More</a>
        </div>
      </div>
    </section>


    <section class="py-16 bg-white">
      <h2 class="text-3xl font-semibold text-center text-red-600 mb-8">Eminent and Unforgettable Figures</h2>
      <div class="overflow-hidden relative">
        <div class="flex animate-marquee space-x-8">
          <div class="flex-shrink-0 w-72">
            <img :src="imageUrl1" alt="CV Raman" class="w-full h-auto rounded-lg shadow-lg"/>
          </div>
          <div class="flex-shrink-0 w-72">
            <img :src="imageUrl2" alt="Har Gobind Khorana" class="w-full h-auto rounded-lg shadow-lg"/>
          </div>
          <div class="flex-shrink-0 w-72">
            <img :src="imageUrl3" alt="Homi Jehangir Bhabha" class="w-full h-auto rounded-lg shadow-lg"/>
          </div>
          <div class="flex-shrink-0 w-72">
            <img :src="imageUrl4" alt="Mother Teresa" class="w-full h-auto rounded-lg shadow-lg"/>
          </div>
        </div>
      </div>
    </section>


    <footer class="bg-red-600 py-4 text-center text-white">
      <p>&copy; 2024 AICTE. All Rights Reserved.</p>
    </footer>
  </div>
</template>

<style scoped>

.bg-gradient-to-r {
  background: linear-gradient(to right, #e53e3e, #f56565); 
}


.bg-white:hover {
  background-color: #f7fafc;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
  transform: translateY(-5px);
}

.bg-white {
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

img:hover {
  transform: scale(1.05);
}


@keyframes marquee {
  0% {
    transform: translateX(100%);
  }
  100% {
    transform: translateX(-100%);
  }
}


.animate-marquee {
  animation: marquee 40s linear infinite;
}

.overflow-hidden {
  overflow: hidden;
}

.flex {
  display: flex;
}

.space-x-8 {
  gap: 2rem;
}

.w-72 {
  width: 18rem;
}

.text-red-600 {
  color: #e53e3e; 
}

.bg-red-600 {
  background-color: #e53e3e; 
}

.text-white {
  color: white;
}

.text-center {
  text-align: center;
}

.font-semibold {
  font-weight: 600;
}

.text-xl {
  font-size: 1.25rem;
}

.text-2xl {
  font-size: 1.5rem;
}

.text-3xl {
  font-size: 1.875rem;
}

.text-lg {
  font-size: 1.125rem;
}

.text-gray-700 {
  color: #4a5568;
}

.bg-gray-100 {
  background-color: #f7fafc;
}

.bg-white {
  background-color: white;
}
</style>
