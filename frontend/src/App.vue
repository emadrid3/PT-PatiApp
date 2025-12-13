<script setup>
  import { ref } from 'vue'
  import SectionSelector from './components/SectionSelector.vue'
  import WorkshopManager from './components/WorkshopManager.vue'
  import ReferenceManager from './components/ReferencesMaganer.vue'
  import ColorManager from './components/ColorsManager.vue'
  
  /**
   * Root component
   */
  
  const selectedSection = ref('Workshops')
  </script>
  
  <template>
    <div class="container">
      <header className="text-center mb-8">
          <h1 className="text-3xl sm:text-4xl font-extrabold text-indigo-700 mb-2">
              Sistema de Gestión de Producción
          </h1>
          <p className="text-gray-600">Herramienta integral para datos maestros y lotes de trabajo.</p>
      </header>
      <SectionSelector v-model="selectedSection" />
  
      <div style="margin-top:2rem">
        <WorkshopManager v-if="selectedSection === 'Workshops'" />
        <ReferenceManager v-if="selectedSection === 'References'" />
        <ColorManager v-if="selectedSection === 'Colors'" />
      </div>
    </div>
  </template>
  