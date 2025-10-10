<script lang="ts">
	import { goto } from '$app/navigation';
	import { writable } from 'svelte/store';

	// --- Common state ---
	const showLogin = writable(false); // false = show register by default

	// Login stores
	const loginEmail = writable('');
	const loginPassword = writable('');
	const loginError = writable('');

	// Register stores
	const regUsername = writable('');
	const regEmail = writable('');
	const regPassword = writable('');
	const regError = writable('');
	const regSuccess = writable('');

	// --- Login Function ---
	async function loginUser() {
		loginError.set('');
		const formData = new URLSearchParams();
		formData.append('username', $loginEmail);
		formData.append('password', $loginPassword);

		try {
			const res = await fetch('http://localhost:8000/auth/login', {
				method: 'POST',
				headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
				body: formData
			});

			if (!res.ok) {
				const data = await res.json();
				loginError.set(data.detail || 'Login failed');
				return;
			}

			const data = await res.json();
			localStorage.setItem('token', data.access_token);
			goto('/dashboard');
		} catch (err: unknown) {
			if (err instanceof Error) loginError.set(err.message);
			else loginError.set(String(err));
		}
	}

	// --- Register Function ---
	async function registerUser() {
		regError.set('');
		regSuccess.set('');

		// simple client-side email check to avoid 422 roundtrip
		const basicEmailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
		if (!$regEmail || !basicEmailRegex.test($regEmail)) {
			regError.set('Please enter a valid email address.');
			return;
		}

		const user = {
			username: $regUsername,
			email: $regEmail,
			password: $regPassword
		};

		try {
			const res = await fetch('http://localhost:8000/auth/register', {
				method: 'POST',
				headers: { 'Content-Type': 'application/json' },
				body: JSON.stringify(user)
			});

			if (!res.ok) {
				const data = await res.json();
				// FastAPI may return {detail: "..."} or {detail: [{msg: "..."}, ...]}
				let message = 'Registration failed';
				if (data?.detail) {
					if (typeof data.detail === 'string') message = data.detail;
					else if (Array.isArray(data.detail) && data.detail.length) {
						message =
							data.detail
								.map((e: any) => e.msg || e.detail || '')
								.filter(Boolean)
								.join('; ') || message;
					}
				}
				regError.set(message);
				return;
			}

			regSuccess.set('✅ Registration successful! You can now login.');
			// Clear fields
			regUsername.set('');
			regEmail.set('');
			regPassword.set('');
			showLogin.set(true); // automatically show login after successful registration
		} catch (err: unknown) {
			if (err instanceof Error) regError.set(err.message);
			else regError.set(String(err));
		}
	}

	function toggleForm() {
		showLogin.update((v) => !v);
	}
</script>

<div class="flex min-h-screen items-center justify-center bg-gray-100">
	<div class="w-full max-w-md rounded bg-white p-8 shadow-md">
		<h1 class="mb-6 text-center text-3xl font-bold" style="font-family: 'Poppins', sans-serif;">
			Welcome to TimetableIQ
		</h1>

		{#if $showLogin}
			<!-- --- LOGIN FORM --- -->
			<h2 class="mb-4 text-center text-2xl font-semibold">Login</h2>

			{#if $loginError}
				<div class="mb-4 rounded bg-red-100 p-2 text-red-700">{$loginError}</div>
			{/if}

			<input
				type="email"
				placeholder="Email"
				bind:value={$loginEmail}
				class="mb-4 w-full rounded border p-3 focus:ring-2 focus:ring-blue-400 focus:outline-none"
			/>
			<input
				type="password"
				placeholder="Password"
				bind:value={$loginPassword}
				class="mb-4 w-full rounded border p-3 focus:ring-2 focus:ring-blue-400 focus:outline-none"
			/>
			<button
				on:click={loginUser}
				class="mb-2 w-full rounded bg-blue-500 py-3 text-white transition-colors hover:bg-blue-600"
			>
				Login
			</button>

			<p class="mt-2 text-center text-sm text-gray-600">
				Don't have an account?
				<span class="cursor-pointer text-blue-500 hover:underline" on:click={toggleForm}
					>Register here</span
				>
			</p>
		{:else}
			<!-- --- REGISTER FORM --- -->
			<h2 class="mb-4 text-center text-2xl font-semibold">Register</h2>

			{#if $regError}
				<div class="mb-4 rounded bg-red-100 p-2 text-red-700">{$regError}</div>
			{/if}
			{#if $regSuccess}
				<div class="mb-4 rounded bg-green-100 p-2 text-green-700">{$regSuccess}</div>
			{/if}

			<input
				type="text"
				placeholder="Username"
				bind:value={$regUsername}
				class="mb-4 w-full rounded border p-3 focus:ring-2 focus:ring-green-400 focus:outline-none"
			/>
			<input
				type="email"
				placeholder="Email"
				bind:value={$regEmail}
				class="mb-4 w-full rounded border p-3 focus:ring-2 focus:ring-green-400 focus:outline-none"
			/>
			<input
				type="password"
				placeholder="Password"
				bind:value={$regPassword}
				class="mb-4 w-full rounded border p-3 focus:ring-2 focus:ring-green-400 focus:outline-none"
			/>
			<button
				on:click={registerUser}
				class="mb-2 w-full rounded bg-green-500 py-3 text-white transition-colors hover:bg-green-600"
			>
				Register
			</button>

			<p class="mt-2 text-center text-sm text-gray-600">
				Already have an account?
				<span class="cursor-pointer text-blue-500 hover:underline" on:click={toggleForm}
					>Login here</span
				>
			</p>
		{/if}
	</div>
</div>
