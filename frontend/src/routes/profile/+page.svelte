<script lang="ts">
	import type { PageData } from './$types';
	import * as Avatar from '$lib/components/ui/avatar/index.js';
	import { User, Mail, LogOut } from 'lucide-svelte';
	import { goto } from '$app/navigation';

	export let data: PageData;

	function handleLogout() {
		document.cookie = 'token=; path=/; max-age=0';
		goto('/');
	}
</script>

<div class="mx-auto max-w-4xl">
	{#if data.error}
		<div class="rounded-lg bg-red-50 p-4 text-red-800">
			<p class="font-semibold">Error loading profile</p>
			<p class="text-sm">{data.error}</p>
		</div>
	{:else if data.user}
		<div class="overflow-hidden rounded-xl bg-white shadow-lg">
			<div class="p-8" style="background: linear-gradient(to bottom, #6A89A7, #c7d9ffff);">
				<div class="flex items-center justify-between">
					<div class="flex items-center gap-6">
						<Avatar.Root class="h-24 w-24 border-4 border-white shadow-lg">
							<Avatar.Image src={data.user.avatar || 'https://github.com/shadcn.png'} alt={data.user.username} />
							<Avatar.Fallback class="text-2xl">{data.user.username?.charAt(0).toUpperCase()}</Avatar.Fallback>
						</Avatar.Root>
						<div class="text-white">
							<h2 class="text-3xl font-bold">{data.user.username}</h2>
							<p class="mt-1 text-blue-100">{data.user.email}</p>
						</div>
					</div>

					<button
						on:click={handleLogout}
						class="flex items-center gap-2 rounded-lg bg-red-500 px-4 py-2 font-semibold text-white shadow-md transition-all hover:bg-red-600"
					>
						<LogOut class="h-5 w-5" />
						Logout
					</button>
				</div>
			</div>

			<div class="p-8">
				<div class="grid gap-6 md:grid-cols-2">
					<div class="flex items-start gap-4 rounded-lg border border-gray-200 p-4">
						<div class="rounded-full p-3" style="background-color: #c7d9ff;">
							<User class="h-5 w-5" style="color: #6A89A7;" />
						</div>
						<div>
							<p class="text-sm font-medium text-gray-500">Username</p>
							<p class="mt-1 text-lg font-semibold text-gray-800">{data.user.username}</p>
						</div>
					</div>

					<div class="flex items-start gap-4 rounded-lg border border-gray-200 p-4">
						<div class="rounded-full p-3" style="background-color: #c7d9ff;">
							<Mail class="h-5 w-5" style="color: #6A89A7;" />
						</div>
						<div>
							<p class="text-sm font-medium text-gray-500">Email</p>
							<p class="mt-1 text-lg font-semibold text-gray-800">{data.user.email}</p>
						</div>
					</div>
				</div>
			</div>
		</div>
	{:else}
		<div class="rounded-lg bg-gray-50 p-8 text-center">
			<p class="text-gray-600">Loading profile...</p>
		</div>
	{/if}
</div>