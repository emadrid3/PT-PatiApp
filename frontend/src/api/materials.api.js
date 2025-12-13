import api from './axios'

/**
 * Materials API
 * These functions map directly to Django ViewSets
 */

export const getMaterials = () => {
    return api.get('materials/')
}

export const createMaterials = (data) => {
    return api.post('materials/', data)
}

export const deleteMaterials = (id) => {
    return api.delete(`materials/${id}/`)
}