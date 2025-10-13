import type { PageServerLoad } from './$types';
import { redirect } from '@sveltejs/kit';

export const load: PageServerLoad = async ({ cookies, fetch }) => {
	const token = cookies.get('token');

	if (!token) {
		throw redirect(302, '/');
	}

	try {
		const response = await fetch('http://localhost:8000/user/me', {
			method: 'GET',
			headers: {
				Authorization: `Bearer ${token}`,
				'Content-Type': 'application/json'
			}
		});

		if (!response.ok) {
			if (response.status === 401) {
				cookies.delete('token', { path: '/' });
				throw redirect(302, '/');
			}

			const errorData = await response.json().catch(() => ({ detail: 'Unknown error' }));
			return {
				user: null,
				error: errorData.detail || `Failed to fetch profile: ${response.statusText}`
			};
		}

		return {
			user: await response.json(),
			error: null
		};
	} catch (error) {
		if (error instanceof Response && error.status === 302) {
			throw error;
		}

		return {
			user: null,
			error: error instanceof Error ? error.message : 'Failed to fetch profile'
		};
	}
};