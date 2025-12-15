import api from './axios'

/**
 * References API
 * These functions map directly to Django ViewSets
 */

export const getReferences = () => {
    return api.get('references/')
}

export const createReference = (data) => {
    return api.post('references/', data)
}

export const deleteReference = (id) => {
    return api.delete(`references/${id}/`)
}