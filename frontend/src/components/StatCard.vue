<template>
    <div class="stat-card">
      <div class="stat-card__header">
        <span class="stat-card__title">{{ title }}</span>
      </div>
  
      <div class="stat-card__value">
        {{ value }}
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'StatCard',
    props: {
      title: String,
      value: [String, Number],
    },
  }
  </script>
  
  <style scoped>
  .stat-card {
    background: linear-gradient(135deg, #1f2937, #111827);
    border-radius: 16px;
    padding: 20px;
    color: #fff;
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
  }
  
  .stat-card__header {
    display: flex;
    align-items: center;
    gap: 8px;
    opacity: 0.9;
  }
  
  .stat-card__icon {
    font-size: 20px;
  }
  
  .stat-card__title {
    font-size: 14px;
  }
  
  .stat-card__value {
    margin-top: 12px;
    font-size: 36px;
    font-weight: 700;
  }
  </style>
  