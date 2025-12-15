<template>
  <BaseCard class="dashboard">
    <h1 class="dashboard-title">Production Dashboard</h1>

    <!-- KPI Cards -->
    <div class="stats-grid">
      <StatCard title="Assignments" :value="totalAssignments"  />
      <StatCard title="Completed" :value="completedAssignments"  />
      <StatCard title="Pending" :value="pendingAssignments"  />
      <StatCard title="Qty by Color" :value="totalByColor"  />
      <StatCard title="Qty by Size" :value="totalBySize"  />
    </div>

    <!-- Chart -->
    <div class="chart-card chart-card--small">
      <h3 class="chart-title">Status Overview</h3>
      <div class="chart-wrapper">
        <canvas ref="statusChart"></canvas>
      </div>
    </div>

    <!-- Table -->
    <AssignmentsTable :items="assignments" :loading="loading" />
  </BaseCard>
</template>

<script>
import { ref, onMounted, computed } from 'vue'
import { Chart, PieController, ArcElement, Tooltip, Legend } from 'chart.js'
import BaseCard from './BaseCard.vue'
import StatCard from '@/components/StatCard.vue'
import AssignmentsTable from '@/components/AssignmentsTable.vue'
import { getCuttingsAssignments } from '../api/cuttingAssignments.api.js'

Chart.register(PieController, ArcElement, Tooltip, Legend)

export default {
  name: 'ProductionDashboard',
  components: {
    BaseCard,
    StatCard,
    AssignmentsTable,
  },
  setup() {
    const assignments = ref([])
    const loading = ref(false)
    const statusChart = ref(null)

    const loadData = async () => {
      loading.value = true
      try {
        const { data } = await getCuttingsAssignments()
        assignments.value = data
        renderChart()
      } catch (e) {
        console.error(e)
      } finally {
        loading.value = false
      }
    }

    const totalAssignments = computed(() => assignments.value.length)
    const completedAssignments = computed(
      () => assignments.value.filter(a => a.status === 'completed').length
    )
    const pendingAssignments = computed(
      () => assignments.value.filter(a => a.status !== 'completed').length
    )

    const totalByColor = computed(() =>
      assignments.value.reduce((s, a) => s + a.quantity_by_color, 0)
    )

    const totalBySize = computed(() =>
      assignments.value.reduce((s, a) => s + a.quantity_by_size, 0)
    )

    const renderChart = () => {
      if (!statusChart.value) return

      new Chart(statusChart.value, {
        type: 'pie',
        data: {
          labels: ['Completed', 'Pending'],
          datasets: [
            {
              data: [
                completedAssignments.value,
                pendingAssignments.value,
              ],
              backgroundColor: ['#10b981', '#f59e0b'],
            },
          ],
        },
      })
    }

    onMounted(loadData)

    return {
      assignments,
      loading,
      totalAssignments,
      completedAssignments,
      pendingAssignments,
      totalByColor,
      totalBySize,
      statusChart,
    }
  },
}
</script>

<style scoped>
.dashboard {
  padding: 24px;
  color: #e5e7eb;
}

.dashboard-title {
  font-size: 26px;
  font-weight: 700;
  margin-bottom: 24px;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 16px;
  margin-bottom: 32px;
}

.chart-card {
  background: #111827;
  border-radius: 16px;
  padding: 20px;
  margin-bottom: 32px;
}

.chart-card--small {
  max-width: 320px;
}

.chart-title {
  font-size: 14px;
  font-weight: 600;
  margin-bottom: 8px;
}

.chart-wrapper {
  position: relative;
  height: 160px;
}

/* BaseCard background */
.dashboard {
  background-color: #031021; /* Background color for BaseCard */
  border-radius: 12px;
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
}
</style>
