import api from './axios'

/**
 * Cuttings API
 * These functions map directly to Django ViewSets
 */

export const getCuttingsAssignments = () => {
    return api.get('cutting-assignments/')
}

export const createCuttingsAssignments = (data) => {
    return api.post('cutting-assignments/', data)
}

export const deleteCuttingsAssignments = (id) => {
    return api.delete(`cutting-assignments/${id}/`)
}