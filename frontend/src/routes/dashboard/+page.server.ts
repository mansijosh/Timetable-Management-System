import { redirect } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';

interface Stat {
	name: string;
	count: number;
	description: string;
}

export const load: PageServerLoad = async ({ cookies, fetch }) => {
	const token = cookies.get('token');
	if (!token) throw redirect(302, '/');

	try {
		const response = await fetch('http://localhost:8000/dashboard/stats', {
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

			return {
				stats: [],
				error: 'Failed to fetch stats'
			};
		}

		const apiStats = await response.json();

	
		const stats: Stat[] = [
			{
				name: 'Subjects',
				count: apiStats.total_subjects,
				description: 'Total subjects available in the system'
			},
			{
				name: 'Departments',
				count: apiStats.total_departments,
				description: 'Total departments in the college'
			},
			{
				name: 'Classrooms',
				count: apiStats.total_classrooms,
				description: 'Total classrooms allocated'
			},
			{
				name: 'Faculty',
				count: apiStats.total_faculties,
				description: 'Total faculty members'
			}
		];
		

		return {
			stats,
			error: null
		};
	} catch (error) {
		return {
			stats: [],
			error: 'Failed to fetch stats'
		};
	}
};
