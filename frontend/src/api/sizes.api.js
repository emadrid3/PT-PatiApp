import api from './axios'

/**
 * Sizes API
 * These functions map directly to Django ViewSets
 */

export const getSizes = () => {
    return api.get('sizes/')
}

export const createSizes = (data) => {
    return api.post('sizes/', data)
}

export const deleteSizes = (id) => {
    return api.delete(`sizes/${id}/`)
}