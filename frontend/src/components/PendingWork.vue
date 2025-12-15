<script setup>
    import { ref, onMounted, computed, watch } from 'vue'
    import BaseCard from './BaseCard.vue'
    
    // APIs
    import { getWorkshops } from '../api/workshops.api.js'
    import { getReferences } from '../api/references.api.js'
    import { getColors } from '../api/colors.api.js'
    import { getMaterials } from '../api/materials.api.js'
    import { getSizes } from '../api/sizes.api.js'
    import { createCuttings, getCuttings } from '../api/cuttings.api.js'
    
    /**
     * Work pending  / Job Creation
     */
    
    const loading = ref(false)
    const cuttings = ref([])
    
    // Form state
    const form = ref({
      quantity_by_reference: 0,
      quantity_by_color: 0,
      quantity_by_size: 0,
      reference: '',
      color: '',
      material: '',
      size: '',
      additional_information: ''
    })
    
    // Select options
    const workshops = ref([])
    const references = ref([])
    const colors = ref([])
    const materials = ref([])
    const sizes = ref([])
    
    // Computed total quantity
    const quantity_by_reference = computed(() => {
    const colorQty = Number(form.value.quantity_by_color) || 0
    const sizeQty = Number(form.value.quantity_by_size) || 0

    return colorQty + sizeQty
    })
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
     * Fetch existing job workshop
     */
    const fetchJobBatches = async () => {
      const response = await getCuttings()
      cuttings.value = response.data
    }
    
    /**
     * Create job Workshop
     */
    const submit = async () => {
      loading.value = true
      try {
        await createCuttings({
          quantity_by_reference: form.value.quantity_by_reference,
          quantity_by_color: form.value.quantity_by_color,
          quantity_by_size: form.value.quantity_by_size,
          reference: form.value.reference,
          color: form.value.color,
          material: form.value.material,
          size: form.value.size,
          additional_information: form.value.additional_information
        })
    
        form.value = {
          quantity_by_color: '',
          quantity_by_reference: '',
          quantity_by_size: '', 
          reference: '',
          color: '',
          material: '',
          size: '',
          additional_information: ''
        }
    
        fetchJobBatches()
      } catch (error) {
        console.error('Error creating job Workshop', error)
      } finally {
        loading.value = false
      }
    }
    
    onMounted(async () => {
      await loadInitialData()
      await fetchJobBatches()
    })

    watch(quantity_by_reference, (newValue) => {
        form.value.quantity_by_reference = newValue
    })
    </script>
    
    <template>
      <BaseCard>
        <h2>📦 Pending Work</h2>
    
        <div class="grid">
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
            <label>Quantity</label>
            <input
                type="number"
                :value="quantity_by_reference"
                disabled
                class="readonly-input"
            />
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
            <label>Quantity by Color *</label>
            <input type="number" v-model="form.quantity_by_color" />
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

          <div>
            <label>Quantity by Size *</label>
            <input type="number" v-model="form.quantity_by_size" />
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
    
          <div class="full">
            <label>Additional Information *</label>
            <textarea v-model="form.additional_information" rows="3"></textarea>
          </div>
        </div>
        
    
        <button class="btn-success" @click="submit" :disabled="loading">
          Add Pending Work
        </button>
      </BaseCard>
    
      <BaseCard>
        <h3>Job Pending List ({{ cuttings.length }})</h3>
        <table v-if="cuttings.length" class="styled-table">
        <thead>
            <tr>
            <th>ID</th>
            <th>CANT.</th>
            <th>REF.</th>
            <th>COLOR</th>
            <th>CANT. COLOR</th>
            <th>MATERIAL</th>
            <th>TALLA</th>
            <th>CANT. TALLA</th>
            </tr>
        </thead>

        <tbody>
            <tr v-for="b in cuttings" :key="b.id">
            <td>{{ b.id }}</td>
            <td>{{ b.quantity_by_reference }}</td>
            <td>{{ b.reference_name }}</td>
            <td>{{ b.color_name }}</td>
            <td>{{ b.quantity_by_color }}</td>
            <td>{{ b.material_name }}</td>
            <td>{{ b.size_name }}</td>
            <td>{{ b.quantity_by_size }}</td>
            </tr>
        </tbody>
        </table>

        <!-- Empty state -->
        <div v-else class="empty-state">
        No hay lotes creados.
        </div>
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

    .styled-table {
  width: 100%;
  border-collapse: collapse;
  background: #ffffff;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
}

.styled-table thead {
  background: #f8fafc;
}

.styled-table th {
  padding: 14px 12px;
  text-align: left;
  font-size: 12px;
  font-weight: 600;
  color: #6b7280;
  text-transform: uppercase;
  border-bottom: 1px solid #e5e7eb;
}

.styled-table td {
  padding: 14px 12px;
  font-size: 14px;
  color: #374151;
  border-bottom: 1px solid #f1f5f9;
}

.styled-table tbody tr:hover {
  background: #f9fafb;
}

/* Styles for the text field container */
.form-group.full {
    grid-column: span 2; /* Takes up the entire column */
    margin-bottom: 1rem; /* Adds margin at the bottom for spacing */
}

/* Styles for the label */
label {
    font-weight: bold; /* Makes the label text bold */
    margin-bottom: 0.5rem; /* Adds space below the label */
    display: block; /* Ensures the label occupies its own line */
}

/* Styles for the text area (textarea) */
textarea {
    width: 100%; /* Makes the text area take up the full width */
    padding: 1rem; /* Adds padding inside the text area */
    border-radius: 8px; /* Rounds the corners of the text area */
    border: 1px solid #ccc; /* Sets a light gray border */
    font-size: 1rem; /* Defines the font size */
    font-family: Arial, sans-serif; /* Sets the font family */
    resize: vertical; /* Allows the user to resize the height of the text area */
    box-sizing: border-box; /* Ensures padding is included in the width and height */
    transition: border-color 0.3s ease, box-shadow 0.3s ease; /* Adds smooth transitions for border and shadow changes */
}

/* Styles when the text area is focused (focus state) */
textarea:focus {
    border-color: #4CAF50; /* Changes the border color to green when focused */
    box-shadow: 0 0 8px rgba(76, 175, 80, 0.5); /* Adds a green glow around the text area */
    outline: none; /* Removes the default focus outline */
}

/* Placeholder styles */
textarea::placeholder {
    color: #999; /* Sets the placeholder text color to light gray */
    font-style: italic; /* Makes the placeholder text italic */
}


/* Empty state */
.empty-state {
  text-align: center;
  padding: 2rem;
  font-style: italic;
  color: #6b7280;
  background: #ffffff;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
}

.readonly-input {
  background: #f8fafc;
  cursor: not-allowed;
  color: #374151;
  font-weight: 600;
}

</style>
    