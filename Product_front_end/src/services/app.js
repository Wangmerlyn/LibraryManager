import { request } from '@umijs/max';

export async function login(params) {
    return request('/api/login', {
        method: 'POST',
        data: params
    });
}