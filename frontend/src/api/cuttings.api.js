import api from './axios'

/**
 * Cuttings API
 * These functions map directly to Django ViewSets
 */

export const getCuttings = () => {
    return api.get('cuttings/')
}

export const createCuttings = (data) => {
    return api.post('cuttings/', data)
}

export const deleteCuttings = (id) => {
    return api.delete(`cuttings/${id}/`)
}