<script setup>
    import { ref, onMounted } from 'vue'
    import BaseCard from './BaseCard.vue'
    import {
      getWorkshops,
      createWorkshop,
      deleteWorkshop
    } from '../api/workshops.api'
    
    /**
     * Workshop CRUD connected to Django REST API
     */
    
    const workshopName = ref('')
    const workshops = ref([])
    const loading = ref(false)
    
    const fetchWorkshops = async () => {
      loading.value = true
      try {
        const response = await getWorkshops()
        workshops.value = response.data
      } catch (error) {
        console.error('Error loading workshops', error)
      } finally {
        loading.value = false
      }
    }
    
    const addWorkshop = async () => {
      if (!workshopName.value) return
    
      try {
        await createWorkshop({ name: workshopName.value })
        workshopName.value = ''
        fetchWorkshops()
      } catch (error) {
        console.error('Error creating workshop', error)
      }
    }
    
    const removeWorkshop = async (id) => {
      try {
        await deleteWorkshop(id)
        fetchWorkshops()
      } catch (error) {
        console.error('Error deleting workshop', error)
      }
    }
    
    onMounted(fetchWorkshops)
    </script>
    
    <template>
      <BaseCard>
        <h2>⚡ Workshop Management</h2>
    
        <div style="display:flex; gap:1rem; margin-top:1rem">
          <input
            v-model="workshopName"
            placeholder="Workshop name"
          />
          <button class="btn-primary" @click="addWorkshop">
            + Create
          </button>
        </div>
      </BaseCard>
    
      <BaseCard>
        <h3>Workshop List</h3>
    
        <p v-if="loading">Loading...</p>
    
        <ul v-else style="list-style:none; padding:0; margin-top:1rem">
          <li
            v-for="w in workshops"
            :key="w.id"
            style="display:flex; justify-content:space-between; padding:0.6rem 0; border-bottom:1px solid #eee"
          >
            <span>
              <strong>ID-{{ w.id }}</strong> — {{ w.name }}
            </span>
    
            <button class="btn-danger" @click="removeWorkshop(w.id)">
              🗑
            </button>
          </li>
        </ul>
      </BaseCard>
    </template>
    