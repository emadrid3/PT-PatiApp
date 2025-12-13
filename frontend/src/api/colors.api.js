import api from './axios'

/**
 * Colors API
 * These functions map directly to Django ViewSets
 */

export const getColors = () => {
    return api.get('colors/')
}

export const createColors = (data) => {
    return api.post('colors/', data)
}

export const deleteColors = (id) => {
    return api.delete(`colors/${id}/`)
}