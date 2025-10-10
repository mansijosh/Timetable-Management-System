import { redirect } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';

interface Department {
	id: number;
	name: string;
	year: number;
}

interface Faculty {
	id: number;
	name: string;
	department: Department;
}

export const load: PageServerLoad = async ({ cookies, fetch }) => {
	// Get token from cookie
	const token = cookies.get('token');

	// Redirect to login if no token
	if (!token) {
		throw redirect(302, '/');
	}

	try {
		// Fetch faculties from backend
		const response = await fetch('http://localhost:8000/faculty/', {
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
				faculties: [],
				error: errorData.detail || `Failed to fetch faculties: ${response.statusText}`
			};
		}

		const faculties: Faculty[] = await response.json();

		return {
			faculties,
			error: null
		};
	} catch (error) {
		if (error instanceof Response && error.status === 302) {
			throw error;
		}

		console.error('Error fetching faculties:', error);
		return {
			faculties: [],
			error: error instanceof Error ? error.message : 'Failed to fetch faculties'
		};
	}
};
