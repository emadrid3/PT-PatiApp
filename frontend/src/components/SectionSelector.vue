<script setup>
    /**
     * Dropdown selector for system main sections.
     */
    
     /* eslint-disable */
    defineProps({
      modelValue: {
        type: String,
        required: true
      }
    })
    
    defineEmits(['update:modelValue'])
    
    const sections = [
      'Workshops',
      'References',
      'Colors',
      'Materials',
      'Sizes',
      'Workshop Assignment'
    ]
    </script>
    
    <template>
      <div>
        <label><strong>Select Section</strong></label>
    
        <select
          :value="modelValue"
          @change="$emit('update:modelValue', $event.target.value)"
        >
          <option
            v-for="section in sections"
            :key="section"
            :value="section"
          >
            {{ section }}
          </option>
        </select>
      </div>
    </template>
    