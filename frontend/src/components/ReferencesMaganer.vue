<script setup>
    import { ref } from 'vue'
    import BaseCard from './BaseCard.vue'
    
    /**
     * References CRUD mock component.
     */
    
    const referencesName = ref('')
    const references = ref([
      { id: 1, name: 'REF #1' },
      { id: 2, name: 'REF #2' }
    ])
    
    const addReferences = () => {
      if (!referencesName.value) return
    
      references.value.push({
        id: Date.now(),
        name: referencesName.value
      })
    
      referencesName.value = ''
    }
    
    const removeReference = (id) => {
      references.value = references.value.filter(w => w.id !== id)
    }
    </script>
    
    <template>
      <BaseCard>
        <h2>⚡ References Management</h2>
    
        <div style="display:flex; gap:1rem; margin-top:1rem">
          <input
            v-model="referencesName"
            placeholder="Reference name"
          />
          <button class="btn-primary" @click="addReferences">
            +
          </button>
        </div>
      </BaseCard>
    
      <BaseCard>
        <h3>References List ({{ references.length }})</h3>
    
        <ul style="list-style:none; padding:0; margin-top:1rem">
          <li
            v-for="w in references"
            :key="w.id"
            style="display:flex; justify-content:space-between; padding:0.6rem 0; border-bottom:1px solid #eee"
          >
            <span><strong>ID-{{ w.id }}</strong> — {{ w.name }}</span>
    
            <button class="btn-danger" @click="removeReference(w.id)">
              🗑
            </button>
          </li>
        </ul>
      </BaseCard>
    </template>
    