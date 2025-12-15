<template>
    <div class="table-card">
      <h3 class="table-title">Assignments</h3>
  
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Cutting</th>
            <th>Workshop</th>
            <th>Status</th>
            <th>Qty Color</th>
            <th>Qty Size</th>
          </tr>
        </thead>
  
        <tbody>
          <tr v-if="loading">
            <td colspan="6">Loading...</td>
          </tr>
  
          <tr v-for="item in items" :key="item.id">
            <td>#{{ item.id }}</td>
            <td>#{{ item.cutting }}</td>
            <td>#{{ item.workshop }}</td>
            <td>
              <span :class="['status', item.status]">
                {{ item.status }}
              </span>
            </td>
            <td>{{ item.quantity_by_color }}</td>
            <td>{{ item.quantity_by_size }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script>
  export default {
    name: 'AssignmentsTable',
    props: {
      items: Array,
      loading: Boolean,
    },
  }
  </script>
  
  <style scoped>
  .table-card {
    background: #111827;
    border-radius: 16px;
    padding: 20px;
    color: #e5e7eb;
  }
  
  .table-title {
    margin-bottom: 12px;
    font-size: 18px;
  }
  
  table {
    width: 100%;
    border-collapse: collapse;
  }
  
  th,
  td {
    padding: 12px;
    text-align: left;
  }
  
  thead {
    background: #1f2937;
  }
  
  tbody tr:hover {
    background: #1f2937;
  }
  
  .status {
    padding: 4px 10px;
    border-radius: 999px;
    font-size: 12px;
    text-transform: capitalize;
  }
  
  .status.completed {
    background: #065f46;
    color: #d1fae5;
  }
  
  .status.pending {
    background: #78350f;
    color: #fde68a;
  }
  </style>
  