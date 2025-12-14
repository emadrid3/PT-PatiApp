<script setup>
    import { ref, onMounted, computed } from 'vue'
    /**
     * Workshop Assignment component.
     */
    import BaseCard from './BaseCard.vue'

    // APIs
    import { getWorkshops } from '../api/workshops.api.js'
    import { getCuttings } from '../api/cuttings.api.js'

    /**
     * Workshop Assignment 
     */
    
    const loading = ref(false)
    const WorkshopAssignment = ref([])

    const form = ref({
        workshops: '',
        cuttings: '',
        cut_date: '',
    })
    
    // Select options
    const workshops = ref([])
    const cuttings = ref([])

    /**
     * Load data for selects
     */
     const loadInitialData = async () => {
      const [
        workshopsRes,
        cuttingsRes,
      
      ] = await Promise.all([
        getWorkshops(),
        getCuttings(),
      ])
        workshops.value = workshopsRes.data
        cuttings.value = cuttingsRes.data
    }

    onMounted(async () => {
      await loadInitialData()
    })

    const selectedCutting = computed(() => {
    return cuttings.value.find(
        c => c.id === form.value.cuttings
    )
    })
</script>
    
<template>
    <BaseCard>
        <h2>🔧 Workshop Assignment</h2>
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
           <!--  <select v-model="form.cuttings">
                <option value="">Select</option>
                <option v-for="w in cuttings" :key="w.id" :value="w.id">
                {{ w.name }}
                </option>
            </select> -->
            <select v-model="form.cuttings">
                <option value="">Select pending work</option>
                <option
                    v-for="c in cuttings"
                    :key="c.id"
                    :value="c.id"
                >
                    {{ "BATCH " + c.id }} |
                    {{ c.reference_name }} |
                    {{ c.color_name }} |
                    Size {{ c.size_name }} |
                    Qty {{ c.quantity_by_reference }}
                </option>
            </select>
            <BaseCard v-if="selectedCutting">
  <h3>📄 Cutting Details</h3>

  <table class="info-table">
    <tbody>
      <tr>
        <th>ID</th>
        <td>{{ selectedCutting.id }}</td>
      </tr>

      <tr>
        <th>Reference</th>
        <td>{{ selectedCutting.reference_name }}</td>
      </tr>

      <tr>
        <th>Quantity by Reference</th>
        <td>{{ selectedCutting.quantity_by_reference }}</td>
      </tr>

      <tr>
        <th>Color</th>
        <td>{{ selectedCutting.color_name }}</td>
      </tr>

      <tr>
        <th>Quantity by Color</th>
        <td>{{ selectedCutting.quantity_by_color }}</td>
      </tr>

      <tr>
        <th>Material</th>
        <td>{{ selectedCutting.material_name }}</td>
      </tr>

      <tr>
        <th>Size</th>
        <td>{{ selectedCutting.size_name }}</td>
      </tr>

      <tr>
        <th>Quantity by Size</th>
        <td>{{ selectedCutting.quantity_by_size }}</td>
      </tr>
    </tbody>
  </table>
</BaseCard>
        </div>
    </div>
    </BaseCard>
     
</template>

<style scoped>
.info-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 1rem;
}

.info-table th {
  text-align: left;
  background: #f8fafc;
  padding: 0.6rem 0.8rem;
  width: 35%;
  font-weight: 600;
  color: #374151;
}

.info-table td {
  padding: 0.6rem 0.8rem;
  border-left: 1px solid #e5e7eb;
  color: #111827;
}

.info-table tr {
  border-bottom: 1px solid #e5e7eb;
}
</style>
    