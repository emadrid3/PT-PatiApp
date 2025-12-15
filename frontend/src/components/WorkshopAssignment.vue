<script setup>
    import { ref, onMounted, computed, watch } from 'vue'
    
    /**
     * Components
     */
    import BaseCard from './BaseCard.vue'
    
    /**
     * APIs
     */
    import { getWorkshops } from '../api/workshops.api.js'
    import { getCuttings } from '../api/cuttings.api.js'
    import { createCuttingsAssignments } from '../api/cuttingAssignments.api.js'

    
    /**
     * State
     */
    const loading = ref(false)
    
    const form = ref({
      workshops: '',
      cuttings: '',
      quantity_ref_assigned: 0,
      quantity_color_assigned: 0,
      cut_date: '',
      status: 'pending',
      additional_information: ''
    })
    
    const workshops = ref([])
    const cuttings = ref([])
    
    /**
     * Load initial data
     */
    const loadInitialData = async () => {
      const [workshopsRes, cuttingsRes] = await Promise.all([
        getWorkshops(),
        getCuttings()
      ])
    
      workshops.value = workshopsRes.data
      cuttings.value = cuttingsRes.data
    }
    
    onMounted(loadInitialData)
    
        /**
     * Create new reference (POST)
     */
     const submit = async () => {
    try {
        loading.value = true

        // Validaciones mínimas
        if (
        !form.value.workshops ||
        !form.value.cuttings ||
        !form.value.cut_date
        ) {
        alert('Please fill all required fields')
        return
        }

        const payload = {
        workshop: form.value.workshops,
        cutting: form.value.cuttings,
        quantity_by_size: form.value.quantity_ref_assigned,
        quantity_by_color: form.value.quantity_color_assigned,
        cut_date: form.value.cut_date,
        status: form.value.status,
        additional_information: form.value.additional_information
        }
        await createCuttingsAssignments(payload)

        alert('Workshop assignment created successfully ✅')

        // Reset form
        form.value = {
        workshops: '',
        cuttings: '',
        quantity_ref_assigned: 0,
        quantity_color_assigned: 0,
        cut_date: '',
        status: 'pending',
        additional_information: ''
        }
        } catch (error) {
            console.error(error)
            alert('Error creating assignment ❌')
        } finally {
            loading.value = false
    }
    }

    /**
     * Selected cutting
     */
    const selectedCutting = computed(() =>
      cuttings.value.find(c => c.id === form.value.cuttings)
    )
    
    /**
     * Max quantities
     */
    const maxQuantityBySize = computed(() =>
      selectedCutting.value ? selectedCutting.value.quantity_by_size : 0
    )
    
    const maxQuantityByColor = computed(() =>
      selectedCutting.value ? selectedCutting.value.quantity_by_color : 0
    )
    
    /**
     * Limit assigned quantities
     */
    watch(
      () => form.value.quantity_ref_assigned,
      value => {
        if (value > maxQuantityBySize.value) {
          form.value.quantity_ref_assigned = maxQuantityBySize.value
        }
      }
    )
    
    watch(
      () => form.value.quantity_color_assigned,
      value => {
        if (value > maxQuantityByColor.value) {
          form.value.quantity_color_assigned = maxQuantityByColor.value
        }
      }
    )
    </script>
    
    <template>
      <!-- Header -->
      <BaseCard>
        <h2>Workshop Assignment</h2>
        <p>Assign tasks to workshops here.</p>
    
        <div class="grid">
          <div>
            <label>Assigned Workshop *</label>
            <select v-model="form.workshops">
              <option value="">Select Work Table</option>
              <option v-for="w in workshops" :key="w.id" :value="w.id">
                {{ w.name }}
              </option>
            </select>
          </div>
    
          <div>
            <label>Assigned Pending Work *</label>
            <select v-model="form.cuttings">
              <option value="">Select pending work</option>
              <option v-for="c in cuttings" :key="c.id" :value="c.id">
                {{ `BATCH ${c.id}` }} |
                {{ c.reference_name }} |
                {{ c.color_name }} |
                Size {{ c.size_name }} |
                Qty {{ c.quantity_by_size }}
              </option>
            </select>
          </div>
        </div>
      </BaseCard>
    
      <!-- Cutting details -->
      <BaseCard v-if="selectedCutting">
        <h3>📄 Cutting Details</h3>
    
        <table class="info-table">
          <tbody>
            <tr><th>ID</th><td>{{ selectedCutting.id }}</td></tr>
            <tr><th>Reference</th><td>{{ selectedCutting.reference_name }}</td></tr>
            <tr><th>Quantity by Reference</th><td>{{ selectedCutting.quantity_by_reference }}</td></tr>
            <tr><th>Color</th><td>{{ selectedCutting.color_name }}</td></tr>
            <tr><th>Quantity by Color</th><td>{{ selectedCutting.quantity_by_color }}</td></tr>
            <tr><th>Material</th><td>{{ selectedCutting.material_name }}</td></tr>
            <tr><th>Size</th><td>{{ selectedCutting.size_name }}</td></tr>
            <tr><th>Quantity by Size</th><td>{{ selectedCutting.quantity_by_size }}</td></tr>
          </tbody>
        </table>
    
        <!-- Assign quantities -->
        <div class="assign-section">
          <h3>📦 Assign Quantities</h3>
    
          <div class="assign-grid">
            <div class="field">
              <label>
                Quantity by Reference
                <small>(max {{ maxQuantityBySize }})</small>
              </label>
              <input
                type="number"
                v-model.number="form.quantity_ref_assigned"
                :max="maxQuantityBySize"
                min="0"
              />
            </div>
    
            <div class="field">
              <label>
                Quantity by Color
                <small>(max {{ maxQuantityByColor }})</small>
              </label>
              <input
                type="number"
                v-model.number="form.quantity_color_assigned"
                :max="maxQuantityByColor"
                min="0"
              />
            </div>
          </div>
        </div>
    
        <!-- Delivery date (FULL WIDTH, BELOW) -->
        <div class="delivery-section">
          <h3>📅 Delivery Date</h3>
    
          <div class="field">
            <label>Date when the order must be ready *</label>
            <input type="date" v-model="form.cut_date" />
          </div>
        </div>
    
        <!-- Assignment details -->
        <div class="details-section">
          <h3>📝 Assignment Details</h3>
    
          <div class="details-grid">
            <div class="field">
              <label>Status *</label>
              <select v-model="form.status">
                <option value="pending">Pending</option>
                <option value="in_progress">In Progress</option>
                <option value="completed">Completed</option>
                <option value="cancelled">Cancelled</option>
              </select>
            </div>
    
            <div class="field full">
                <label class="field-label">Additional Information</label>

                <textarea
                    v-model="form.additional_information"
                    class="textarea"
                    rows="4"
                    placeholder="Add any relevant notes or instructions for this assignment..."
                ></textarea>

                <small class="field-hint">
                    Optional — include instructions or notes for the workshop regarding this assignment.
                </small>
            </div>
          </div>
        </div>
    
        <button class="btn-success" @click="submit" :disabled="loading">
          Add Workshop Assignment
        </button>
      </BaseCard>
    </template>
    
    <style scoped>
    .grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 1rem;
    }
    
    .info-table {
      width: 100%;
      border-collapse: collapse;
      margin-top: 1rem;
    }
    
    .info-table th {
      background: #f8fafc;
      padding: 0.6rem;
      width: 35%;
      text-align: left;
    }
    
    .info-table td {
      padding: 0.6rem;
      border-left: 1px solid #e5e7eb;
    }
    
    .assign-section,
    .delivery-section,
    .details-section {
      margin-top: 2rem;
    }
    
    .assign-grid,
    .details-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 1rem;
    }
    
    .details-grid .full {
      grid-column: span 2;
    }
    
    .field label {
      display: block;
      font-weight: 500;
      margin-bottom: 0.3rem;
    }
    
    .field small {
      color: #6b7280;
      font-size: 0.8rem;
    }
    
    
    .btn-success {
      margin-top: 2rem;
      width: 100%;
      padding: 0.9rem;
      background: #16a34a;
      color: white;
      font-weight: 600;
      border-radius: 10px;
    }

    /* Textarea container */
    .field.full {
    display: flex;
    flex-direction: column;
    }

    /* Label */
    .field-label {
    font-weight: 600;
    margin-bottom: 0.4rem;
    color: #111827;
    }

    /* Textarea style */
    .textarea {
    width: 100%;
    min-height: 120px;
    padding: 0.75rem 0.85rem;
    border-radius: 10px;
    border: 1px solid #d1d5db;
    background-color: #ffffff;
    font-family: inherit;
    font-size: 0.95rem;
    line-height: 1.4;
    resize: vertical;
    transition: border-color 0.2s ease, box-shadow 0.2s ease;
    }

    /* Focus effect */
    .textarea:focus {
    outline: none;
    border-color: #16a34a;
    box-shadow: 0 0 0 3px rgba(22, 163, 74, 0.15);
    }

    /* Placeholder */
    .textarea::placeholder {
    color: #9ca3af;
    }

    /* Helper text */
    .field-hint {
    margin-top: 0.35rem;
    font-size: 0.8rem;
    color: #6b7280;
    }
    </style>
    