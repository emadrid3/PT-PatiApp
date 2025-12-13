import api from './axios'

/**
 * Workshops API
 * These functions map directly to Django ViewSets
 */

export const getWorkshops = () => {
    return api.get('work-shops/')
}

export const createWorkshop = (data) => {
    return api.post('work-shops/', data)
}

export const deleteWorkshop = (id) => {
    return api.delete(`work-shops/${id}/`)
}