import type { LayoutServerLoad } from './$types';

export const load: LayoutServerLoad = async ({ cookies, url }) => {
	const token = cookies.get('token');
	const isAuthenticated = !!token;
	const isLoginPage = url.pathname === '/';

	return {
		isAuthenticated,
		isLoginPage
	};
};
