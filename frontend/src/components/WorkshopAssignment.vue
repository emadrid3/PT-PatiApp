<script setup>
    import { ref, onMounted } from 'vue'
    import BaseCard from './BaseCard.vue'
    
    // APIs
    import { getWorkshops } from '../api/workshops.api.js'
    import { getReferences } from '../api/references.api.js'
    import { getColors } from '../api/colors.api.js'
    import { getMaterials } from '../api/materials.api.js'
    import { getSizes } from '../api/sizes.api.js'
    import { createCuttings, getCuttings } from '../api/cuttings.api.js'
    
    /**
     * Workshop Assignment / Job Batch Creation
     */
    
    const loading = ref(false)
    const cuttings = ref([])
    
    // Form state
    const form = ref({
      name: '',
      quantity: '',
      workshop: '',
      reference: '',
      color: '',
      material: '',
      size: '',
      notes: ''
    })
    
    // Select options
    const workshops = ref([])
    const references = ref([])
    const colors = ref([])
    const materials = ref([])
    const sizes = ref([])
    
    /**
     * Load data for selects
     */
    const loadInitialData = async () => {
      const [
        workshopsRes,
        referencesRes,
        colorsRes,
        materialsRes,
        sizesRes
      ] = await Promise.all([
        getWorkshops(),
        getReferences(),
        getColors(),
        getMaterials(),
        getSizes()
      ])
    
      workshops.value = workshopsRes.data
      references.value = referencesRes.data
      colors.value = colorsRes.data
      materials.value = materialsRes.data
      sizes.value = sizesRes.data
    }
    
    /**
     * Fetch existing job batches
     */
    const fetchJobBatches = async () => {
      const response = await getCuttings()
      cuttings.value = response.data
    }
    
    /**
     * Create job batch
     */
    const submit = async () => {
      loading.value = true
      try {
        await createCuttings({
          name: form.value.name,
          quantity: form.value.quantity,
          workshop: form.value.workshop,
          reference: form.value.reference,
          color: form.value.color,
          material: form.value.material,
          size: form.value.size,
          notes: form.value.notes
        })
    
        form.value = {
          name: '',
          quantity: '',
          workshop: '',
          reference: '',
          color: '',
          material: '',
          size: '',
          notes: ''
        }
    
        fetchJobBatches()
      } catch (error) {
        console.error('Error creating job batch', error)
      } finally {
        loading.value = false
      }
    }
    
    onMounted(async () => {
      await loadInitialData()
      await fetchJobBatches()
    })
    </script>
    
    <template>
      <BaseCard>
        <h2>📦 Job Batch Creation</h2>
    
        <div class="grid">
          <div>
            <label>Batch Name *</label>
            <input v-model="form.name" />
          </div>
    
          <div>
            <label>Quantity *</label>
            <input type="number" v-model="form.quantity" />
          </div>
    
          <div>
            <label>Assigned Workshop *</label>
            <select v-model="form.workshop">
              <option value="">Select workshop</option>
              <option v-for="w in workshops" :key="w.id" :value="w.id">
                {{ w.name }}
              </option>
            </select>
          </div>
    
          <div>
            <label>Reference *</label>
            <select v-model="form.reference">
              <option value="">Select reference</option>
              <option v-for="r in references" :key="r.id" :value="r.id">
                {{ r.name }}
              </option>
            </select>
          </div>
    
          <div>
            <label>Color *</label>
            <select v-model="form.color">
              <option value="">Select color</option>
              <option v-for="c in colors" :key="c.id" :value="c.id">
                {{ c.name }}
              </option>
            </select>
          </div>
    
          <div>
            <label>Material *</label>
            <select v-model="form.material">
              <option value="">Select material</option>
              <option v-for="m in materials" :key="m.id" :value="m.id">
                {{ m.name }}
              </option>
            </select>
          </div>
    
          <div>
            <label>Size *</label>
            <select v-model="form.size">
              <option value="">Select size</option>
              <option v-for="s in sizes" :key="s.id" :value="s.id">
                {{ s.name }}
              </option>
            </select>
          </div>
    
          <div class="full">
            <label>Additional Information</label>
            <textarea v-model="form.notes" rows="3"></textarea>
          </div>
        </div>
    
        <button class="btn-success" @click="submit" :disabled="loading">
          + Create New Job Batch
        </button>
      </BaseCard>
    
      <BaseCard>
        <h3>Created Job Batches ({{ cuttings.length }})</h3>
    
        <table v-if="cuttings.length">
          <thead>
            <tr>
              <th>ID</th>
              <th>Name</th>
              <th>Qty</th>
              <th>Workshop</th>
              <th>Ref</th>
              <th>Color</th>
              <th>Material</th>
              <th>Size</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="b in cuttings" :key="b.id">
              <td>{{ b.id }}</td>
              <td>{{ b.name }}</td>
              <td>{{ b.quantity }}</td>
              <td>{{ b.workshop_name }}</td>
              <td>{{ b.reference_name }}</td>
              <td>{{ b.color_name }}</td>
              <td>{{ b.material_name }}</td>
              <td>{{ b.size_name }}</td>
            </tr>
          </tbody>
        </table>
    
        <p v-else>No job batches created.</p>
      </BaseCard>
    </template>
    
    <style scoped>
    .grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 1rem;
    }
    
    .full {
      grid-column: span 3;
    }
    
    .btn-success {
      margin-top: 1.5rem;
      background: #16a34a;
      color: white;
      width: 100%;
      padding: 0.9rem;
      border-radius: 10px;
      font-weight: 600;
    }
    </style>
    