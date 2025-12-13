<script setup>
    import { ref } from 'vue'
    import BaseCard from './BaseCard.vue'
    
    /**
     * Workshop CRUD mock component.
     */
    
    const workshopName = ref('')
    const workshops = ref([
      { id: 1, name: 'Taller Textil del Sol' },
      { id: 2, name: 'Costuras Rápidas' }
    ])
    
    const addWorkshop = () => {
      if (!workshopName.value) return
    
      workshops.value.push({
        id: Date.now(),
        name: workshopName.value
      })
    
      workshopName.value = ''
    }
    
    const removeWorkshop = (id) => {
      workshops.value = workshops.value.filter(w => w.id !== id)
    }
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
        <h3>Workshop List ({{ workshops.length }})</h3>
    
        <ul style="list-style:none; padding:0; margin-top:1rem">
          <li
            v-for="w in workshops"
            :key="w.id"
            style="display:flex; justify-content:space-between; padding:0.6rem 0; border-bottom:1px solid #eee"
          >
            <span><strong>ID-{{ w.id }}</strong> — {{ w.name }}</span>
    
            <button class="btn-danger" @click="removeWorkshop(w.id)">
              🗑
            </button>
          </li>
        </ul>
      </BaseCard>
    </template>
    