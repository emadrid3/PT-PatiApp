<script setup>
    import { onMounted, ref } from 'vue'
    import BaseCard from './BaseCard.vue'
    import {
      getSizes,
      createSizes,
      deleteSizes
    } from '../api/sizes.api.js'
    
    
    /**
     * Size CRUD component.
     */
    
    const sizesName = ref('')
    const sizes = ref([])
    const loading = ref(false)


    const fetchsizes = async () => {
      loading.value = true
      try {
        const response = await getSizes()
        sizes.value = response.data
      } catch (error) {
        console.error('Error loading sizes', error)
      } finally {
        loading.value = false
      }
    }
    
    /**
     * Create new size (POST)
     */
    const addsizes = async () => {
      if (!sizesName.value) return
    
      try {
        await createSizes({ name: sizesName.value })
        sizesName.value = ''
        fetchsizes()
      } catch (error) {
        console.error('Error creating reference', error)
      }
    }

    const removeSize = async (id) => {
      try {
        await deleteSizes(id)
        fetchsizes()
      } catch (error) {
        console.error('Error deleting reference', error)
      }
    }

    onMounted(() => {
        fetchsizes()
    })
    </script>
    
<template>
    <BaseCard>
    <h2>⚡ Sizes Management</h2>

    <div style="display:flex; gap:1rem; margin-top:1rem">
        <input
        v-model="sizesName"
        placeholder="Reference name"
        />
        <button class="btn-primary" @click="addsizes">
        +
        </button>
    </div>
    </BaseCard>

    <BaseCard>
    <h3>Sizes List ({{ sizes.length }})</h3>

    <ul style="list-style:none; padding:0; margin-top:1rem">
        <li
        v-for="w in sizes"
        :key="w.id"
        style="display:flex; justify-content:space-between; padding:0.6rem 0; border-bottom:1px solid #eee"
        >
        <span><strong>ID-{{ w.id }}</strong> — {{ w.name }}</span>

        <button class="btn-danger" @click="removeSize(w.id)">
            🗑
        </button>
        </li>
    </ul>
    </BaseCard>
</template>
    