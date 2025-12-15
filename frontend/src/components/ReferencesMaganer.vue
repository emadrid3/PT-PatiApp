<script setup>
    import { onMounted, ref } from 'vue'
    import BaseCard from './BaseCard.vue'
    import {
      getReferences,
      createReference,
      deleteReference
    } from '../api/references.api.js'
    
    
    /**
     * References CRUD mock component.
     */
    
    const referencesName = ref('')
    const references = ref([])
    const loading = ref(false)


    const fetchReferences = async () => {
      loading.value = true
      try {
        const response = await getReferences()
        references.value = response.data
      } catch (error) {
        console.error('Error loading references', error)
      } finally {
        loading.value = false
      }
    }
    
    /**
     * Create new reference (POST)
     */
    const addReferences = async () => {
      if (!referencesName.value) return
    
      try {
        await createReference({ name: referencesName.value })
        referencesName.value = ''
        fetchReferences()
      } catch (error) {
        console.error('Error creating reference', error)
      }
    }

    const removeReference = async (id) => {
      try {
        await deleteReference(id)
        fetchReferences()
      } catch (error) {
        console.error('Error deleting reference', error)
      }
    }

    onMounted(() => {
        fetchReferences()
    })
    </script>
    
<template>
    <BaseCard>
    <h2>⚡ References Management</h2>

    <div style="display:flex; gap:1rem; margin-top:1rem">
        <input
        v-model="referencesName"
        placeholder="Reference name"
        />
        <button class="btn-primary" @click="addReferences">
        +
        </button>
    </div>
    </BaseCard>

    <BaseCard>
    <h3>References List ({{ references.length }})</h3>

    <ul style="list-style:none; padding:0; margin-top:1rem">
        <li
        v-for="w in references"
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
    