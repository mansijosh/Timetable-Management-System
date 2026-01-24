import { redirect, fail, type Actions } from '@sveltejs/kit';

export const actions: Actions = {
	default: async ({ request, cookies, fetch }) => {
		const token = cookies.get('token');

		if (!token) {
			throw redirect(302, '/');
		}

		const data = await request.formData();
		const name = data.get('name')?.toString();
		const year = data.get('year')?.toString();
		

		if (!name || !year) {
			return fail(400, { error: 'Name and year are required' });
		}

		const response = await fetch('http://localhost:8000/department/', {
			method: 'POST',
			headers: {
				Authorization: `Bearer ${token}`,
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({
				name,
				year: Number(year),
				
			})
		});

		if (!response.ok) {
			const err = await response.json().catch(() => ({ detail: 'Create failed' }));
			return fail(response.status, {
				error: err.detail || 'Failed to create department'
			});
		}

		
		throw redirect(303, '/department');
	}
};
