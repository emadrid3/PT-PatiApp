<script setup>
    import { onMounted, ref } from 'vue'
    import BaseCard from './BaseCard.vue'
    import {
      getMaterials,
      createMaterials,
      deleteMaterials
    } from '../api/materials.api.js'
    
    
    /**
     * materials CRUD mock component.
     */
    
    const materialsName = ref('')
    const materials = ref([])
    const loading = ref(false)


    const fetchmaterials = async () => {
      loading.value = true
      try {
        const response = await getMaterials()
        materials.value = response.data
      } catch (error) {
        console.error('Error loading materials', error)
      } finally {
        loading.value = false
      }
    }
    
    /**
     * Create new reference (POST)
     */
    const addmaterials = async () => {
      if (!materialsName.value) return
    
      try {
        await createMaterials({ name: materialsName.value })
        materialsName.value = ''
        fetchmaterials()
      } catch (error) {
        console.error('Error creating reference', error)
      }
    }

    const removeReference = async (id) => {
      try {
        await deleteMaterials(id)
        fetchmaterials()
      } catch (error) {
        console.error('Error deleting reference', error)
      }
    }

    onMounted(() => {
        fetchmaterials()
    })
    </script>
    
<template>
    <BaseCard>
    <h2>Materials Management</h2>

    <div style="display:flex; gap:1rem; margin-top:1rem">
        <input
        v-model="materialsName"
        placeholder="Reference name"
        />
        <button class="btn-primary" @click="addmaterials">
        +
        </button>
    </div>
    </BaseCard>

    <BaseCard>
    <h3>Materials List ({{ materials.length }})</h3>

    <ul style="list-style:none; padding:0; margin-top:1rem">
        <li
        v-for="w in materials"
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
    