<script setup>
    import { ref } from 'vue'
    import BaseCard from './BaseCard.vue'
    
    /**
     * COLORS CRUD mock component.
     */
    
    const colorName = ref('')
    const color = ref([
      { id: 1, name: 'Rojo' },
      { id: 2, name: 'Azul' }
    ])
    
    const addColor = () => {
      if (!colorName.value) return
    
      color.value.push({
        id: Date.now(),
        name: colorName.value
      })
    
      colorName.value = ''
    }
    
    const removeColor = (id) => {
      color.value = color.value.filter(w => w.id !== id)
    }
    </script>
    
    <template>
      <BaseCard>
        <h2>⚡ Color Management</h2>
    
        <div style="display:flex; gap:1rem; margin-top:1rem">
          <input
            v-model="colorName"
            placeholder="Color name"
          />
          <button class="btn-primary" @click="addColor">
            +
          </button>
        </div>
      </BaseCard>
    
      <BaseCard>
        <h3>Color List ({{ color.length }})</h3>
    
        <ul style="list-style:none; padding:0; margin-top:1rem">
          <li
            v-for="w in color"
            :key="w.id"
            style="display:flex; justify-content:space-between; padding:0.6rem 0; border-bottom:1px solid #eee"
          >
            <span><strong>ID-{{ w.id }}</strong> — {{ w.name }}</span>
    
            <button class="btn-danger" @click="removeColor(w.id)">
              🗑
            </button>
          </li>
        </ul>
      </BaseCard>
    </template>
    