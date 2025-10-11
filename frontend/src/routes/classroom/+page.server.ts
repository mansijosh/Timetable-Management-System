import { redirect } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';

interface Department {
	id: number;
	name: string;
	year: number;
}

interface Classroom {
	id: number;
	building_name: string;
	room_no: string;
	capacity: number;
	department: Department;
}

export const load: PageServerLoad = async ({ cookies, fetch }) => {
	// Get token from cookie
	const token = cookies.get('token');

	// If no token, redirect to login
	if (!token) {
		throw redirect(302, '/');
	}

	try {
		// Fetch classrooms from FastAPI backend
		const response = await fetch('http://localhost:8000/classroom/', {
			method: 'GET',
			headers: {
				Authorization: `Bearer ${token}`,
				'Content-Type': 'application/json'
			}
		});

		if (!response.ok) {
			// If unauthorized, clear cookie and redirect to login
			if (response.status === 401) {
				cookies.delete('token', { path: '/' });
				throw redirect(302, '/');
			}

			const errorData = await response.json().catch(() => ({ detail: 'Unknown error' }));
			return {
				classrooms: [],
				error: errorData.detail || `Failed to fetch classrooms: ${response.statusText}`
			};
		}

		const classrooms: Classroom[] = await response.json();

		return {
			classrooms,
			error: null
		};
	} catch (error) {
		// If it's a redirect, re-throw it
		if (error instanceof Response && error.status === 302) {
			throw error;
		}

		console.error('Error fetching classrooms:', error);
		return {
			classrooms: [],
			error: error instanceof Error ? error.message : 'Failed to fetch classrooms'
		};
	}
};
