import api from './axios'

/**
 * Cuttings API
 * These functions map directly to Django ViewSets
 */

export const getCuttings = () => {
    return api.get('materials/')
}

export const createCuttings = (data) => {
    return api.post('materials/', data)
}

export const deleteCuttings = (id) => {
    return api.delete(`materials/${id}/`)
}