<script lang="ts">
	import { goto } from '$app/navigation';
	import { onMount } from 'svelte';
	import * as Avatar from '$lib/components/ui/avatar/index.js';
	import { user } from '$lib/stores/userStore'; // import the store
	import { get } from 'svelte/store';

	const menuItems = [
		{ name: 'Classroom', path: '/classroom', icon: '📚' },
		{ name: 'Departments', path: '/department', icon: '🏢' },
		{ name: 'Users', path: '/user', icon: '👥' },
		{ name: 'Faculty', path: '/faculty', icon: '🧑‍🏫' },
		{ name: 'Subjects', path: '/subject', icon: '📖' },
		{ name: 'Timetable', path: '/timetable', icon: '📅' }
	];

	function navigate(path: string) {
		goto(path);
	}

	let showProfile = false;

	// Helper to read JWT from cookie
	function getCookie(name: string) {
		const value = `; ${document.cookie}`;
		const parts = value.split(`; ${name}=`);
		if (parts.length === 2) return parts.pop()?.split(';').shift();
	}

	async function fetchUser() {
		const token = getCookie('token');
		if (!token) {
			user.set({ name: '', email: '', avatar: '' });
			return;
		}

		try {
			const res = await fetch('http://localhost:8000/profile/me', {
				headers: {
					'Authorization': `Bearer ${token}`,
					'Accept': 'application/json'
				}
			});
			if (res.ok) {
				const data = await res.json();
				user.set({
					name: data.username,
					email: data.email,
					avatar: ''
				});
			} else {
				user.set({ name: '', email: '', avatar: '' });
			}
		} catch (err) {
			console.error(err);
			user.set({ name: '', email: '', avatar: '' });
		}
	}

	onMount(fetchUser);

	function logout() {
		document.cookie = 'token=; path=/; max-age=0';
		user.set({ name: '', email: '', avatar: '' }); // reset user immediately
		goto('/'); // go to login/register page
	}
</script>

<div class="flex min-h-screen">
	<aside class="flex w-64 flex-col justify-between p-6 text-white"
	       style="background: linear-gradient(to bottom, #6A89A7, #c7d9ffff);">

		<div>
			<h1 class="mb-8 text-center text-3xl font-bold text-yellow-300 drop-shadow-lg">
				Admin Panel
			</h1>

			{#each menuItems as item}
				<button
					class="mb-3 flex w-full items-center gap-4 rounded-lg px-4 py-3 font-medium text-white
					       shadow-md transition-all duration-300 hover:bg-white hover:text-blue-700"
					on:click={() => navigate(item.path)}
				>
					<span class="text-xl">{item.icon}</span>
					<span>{item.name}</span>
				</button>
			{/each}
		</div>

		<!-- Profile -->
		<div class="relative">
			<div class="flex items-center border-t border-gray-300 pt-6 cursor-pointer"
			     on:click={() => showProfile = !showProfile}>
				<Avatar.Root class="h-12 w-12 rounded-full border-2 border-gray-300 overflow-hidden">
					{#if $user.avatar}
						<Avatar.Image src={$user.avatar} alt={$user.name} />
					{:else}
						<Avatar.Fallback class="bg-blue-500 text-white flex items-center justify-center font-bold">
							{$user.name ? $user.name.slice(0, 2).toUpperCase() : 'GU'}
						</Avatar.Fallback>
					{/if}
				</Avatar.Root>
				<p class="ml-3 text-sm font-semibold text-black">{$user.name || 'Guest'}</p>
			</div>

			{#if showProfile}
				<div class="absolute bottom-20 left-0 w-64 rounded-lg bg-white shadow-lg p-4 z-50">
					<p class="font-semibold text-black">{$user.name || 'Guest'}</p>
					<p class="text-sm text-gray-500">{$user.email || '-'}</p>
					<button class="mt-3 w-full rounded bg-blue-500 px-3 py-2 text-white hover:bg-blue-600"
					        on:click={logout}>
						Logout
					</button>
				</div>
			{/if}
		</div>
	</aside>

	<main class="flex-1 p-8"
	      style="background-size: cover; background-position: center; min-height: 100vh;">
		<div class="bg-opacity-80 min-h-full rounded-xl bg-white p-6 shadow-lg">
			<slot></slot>
		</div>
	</main>
</div>
