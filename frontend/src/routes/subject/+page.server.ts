import { redirect } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';

interface Subject {
	id: number;
	name: string;
	professor?: { id: number; name: string };
	department?: { id: number; name: string };
}

export const load: PageServerLoad = async ({ cookies, fetch }) => {
	const token = cookies.get('token');

	if (!token) {
		throw redirect(302, '/');
	}

	try {
		const response = await fetch('http://localhost:8000/subject', {
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
				subjects: [],
				error: errorData.detail || `Failed to fetch subjects: ${response.statusText}`
			};
		}

		const subjects: Subject[] = await response.json();
		return {
			subjects,
			error: null
		};
	} catch (error) {
		console.error('Error fetching subjects:', error);
		return {
			subjects: [],
			error: error instanceof Error ? error.message : 'Failed to fetch subjects'
		};
	}
};
