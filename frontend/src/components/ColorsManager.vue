<script setup>
    import { ref, onMounted } from 'vue'
    import BaseCard from './BaseCard.vue'
    import {
      getColors,
      createColors,
      deleteColors
    } from '../api/colors.api.js'
    
    /**
     * COLORS CRUD component connected to backend
     */
    
    const colorName = ref('')
    const colors = ref([])
    const loading = ref(false)
    
    /**
     * Fetch colors from DB (GET)
     */
    const fetchColors = async () => {
      loading.value = true
      try {
        const response = await getColors()
        colors.value = response.data
      } catch (error) {
        console.error('Error loading colors', error)
      } finally {
        loading.value = false
      }
    }
    
    /**
     * Create color (POST)
     */
    const addColor = async () => {
      if (!colorName.value) return
    
      try {
        await createColors({ name: colorName.value })
        colorName.value = ''
        fetchColors() // 🔁 refresh list
      } catch (error) {
        console.error('Error creating color', error)
      }
    }
    
    /**
     * Delete color (DELETE)
     */
    const removeColor = async (id) => {
      try {
        await deleteColors(id)
        fetchColors() // 🔁 refresh list
      } catch (error) {
        console.error('Error deleting color', error)
      }
    }
    
    /**
     * Lifecycle hook
     * Runs when component is mounted
     */
    onMounted(() => {
      fetchColors()
    })
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
    <h3>Color List ({{ colors.length }})</h3>

    <p v-if="loading">Loading...</p>

    <ul
        v-else
        style="list-style:none; padding:0; margin-top:1rem"
    >
        <li
        v-for="color in colors"
        :key="color.id"
        style="display:flex; justify-content:space-between; padding:0.6rem 0; border-bottom:1px solid #eee"
        >
        <span>
            <strong>ID-{{ color.id }}</strong> — {{ color.name }}
        </span>

        <button
            class="btn-danger"
            @click="removeColor(color.id)"
        >
            🗑
        </button>
        </li>
    </ul>
    </BaseCard>
</template>
