<template>
    <div class="card">
      <slot />
    </div>
  </template>
  
  <style scoped>
  .card {
    background: var(--card);
    border-radius: 16px;
    padding: 1.5rem;
    margin-bottom: 1.5rem;
    box-shadow: 0 10px 25px rgba(0,0,0,0.05);
  }
  </style>
  