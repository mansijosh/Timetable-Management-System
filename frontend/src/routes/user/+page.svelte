<script lang="ts">
	import type { PageData } from './$types';
	import { Users } from 'lucide-svelte';

	interface Props {
		data: PageData;
	}

	let { data }: Props = $props();
</script>

<div class="min-h-screen bg-gray-100 p-8">
	<div class="mx-auto max-w-6xl">
		<div class="mb-6 rounded-lg bg-white p-6 shadow-md">
			<h1 class="mb-2 flex items-center gap-2 text-3xl font-bold">
				<Users class="h-8 w-8 p-1" />
				Users
			</h1>
			<p class="text-gray-600">Welcome to TimetableIQ</p>
		</div>

		<div class="rounded-lg bg-white p-6 shadow-md">
			<h2 class="mb-4 text-2xl font-semibold">Users</h2>

			{#if data.users && data.users.length > 0}
				<div class="overflow-x-auto">
					<table class="min-w-full divide-y divide-gray-200">
						<thead class="bg-gray-50">
							<tr>
								<th
									class="px-6 py-3 text-left text-xs font-medium tracking-wider text-gray-500 uppercase"
								>
									Username
								</th>
								<th
									class="px-6 py-3 text-left text-xs font-medium tracking-wider text-gray-500 uppercase"
								>
									Email
								</th>
							</tr>
						</thead>
						<tbody class="divide-y divide-gray-200 bg-white">
							{#each data.users as user}
								<tr class="hover:bg-gray-50">
									<td class="px-6 py-4 text-sm font-medium whitespace-nowrap text-gray-900">
										{user.username}
									</td>
									<td class="px-6 py-4 text-sm whitespace-nowrap text-gray-700">
										{user.email}
									</td>
								</tr>
							{/each}
						</tbody>
					</table>
				</div>
			{:else}
				<div class="py-8 text-center text-gray-500">
					<p>No users found.</p>
				</div>
			{/if}
		</div>

		{#if data.error}
			<div class="mt-4 rounded-lg bg-red-100 p-4 text-red-700">
				<p class="font-semibold">Error loading users:</p>
				<p>{data.error}</p>
			</div>
		{/if}
	</div>
</div>
