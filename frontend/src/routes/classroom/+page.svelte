<script lang="ts">
	import type { PageData } from './$types';
	import { Building2 } from 'lucide-svelte';

	interface Props {
		data: PageData;
	}

	let { data }: Props = $props();
</script>

<div class="min-h-screen bg-gray-100 p-8">
	<div class="mx-auto max-w-7xl">
		<div class="mb-6 rounded-lg bg-white p-6 shadow-md">
			<h1 class="mb-2 flex items-center gap-2 text-3xl font-bold">
				<Building2 class="h-8 w-8 p-1" />
				Classrooms
			</h1>

			<p class="text-gray-600">Manage all classrooms and their details</p>
		</div>

		<div class="rounded-lg bg-white p-6 shadow-md">
			<div class="mb-4 flex items-center justify-between">
				<h2 class="text-2xl font-semibold">All Classrooms</h2>
				<span class="rounded-full bg-blue-100 px-3 py-1 text-sm font-medium text-blue-800">
					Total: {data.classrooms?.length || 0}
				</span>
			</div>

			{#if data.classrooms && data.classrooms.length > 0}
				<div class="overflow-x-auto">
					<table class="min-w-full divide-y divide-gray-200">
						<thead class="bg-gray-50">
							<tr>
								<th
									class="px-6 py-3 text-left text-xs font-medium tracking-wider text-gray-500 uppercase"
								>
									Room No
								</th>
								<th
									class="px-6 py-3 text-left text-xs font-medium tracking-wider text-gray-500 uppercase"
								>
									Building
								</th>
								<th
									class="px-6 py-3 text-left text-xs font-medium tracking-wider text-gray-500 uppercase"
								>
									Department
								</th>
								<th
									class="px-6 py-3 text-left text-xs font-medium tracking-wider text-gray-500 uppercase"
								>
									Year
								</th>
								<th
									class="px-6 py-3 text-left text-xs font-medium tracking-wider text-gray-500 uppercase"
								>
									Capacity
								</th>
							</tr>
						</thead>
						<tbody class="divide-y divide-gray-200 bg-white">
							{#each data.classrooms as classroom}
								<tr class="hover:bg-gray-50">
									<td class="px-6 py-4 text-sm font-medium whitespace-nowrap text-gray-900">
										{classroom.room_no}
									</td>
									<td class="px-6 py-4 text-sm whitespace-nowrap text-gray-700">
										{classroom.building_name}
									</td>
									<td class="px-6 py-4 text-sm text-gray-700">
										{classroom.department?.name || 'N/A'}
									</td>
									<td class="px-6 py-4 text-sm whitespace-nowrap text-gray-700">
										{classroom.department?.year || 'N/A'}
									</td>
									<td class="px-6 py-4 text-sm whitespace-nowrap text-gray-700">
										<span
											class="inline-flex rounded-full bg-green-100 px-2 py-1 text-xs font-semibold text-green-800"
										>
											{classroom.capacity}
										</span>
									</td>
								</tr>
							{/each}
						</tbody>
					</table>
				</div>
			{:else}
				<div class="py-12 text-center text-gray-500">
					<svg
						class="mx-auto h-12 w-12 text-gray-400"
						fill="none"
						stroke="currentColor"
						viewBox="0 0 24 24"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							stroke-width="2"
							d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"
						/>
					</svg>
					<p class="mt-4 text-lg font-medium">No classrooms found</p>
					<p class="mt-1 text-sm">There are no classrooms in the system yet.</p>
				</div>
			{/if}
		</div>

		{#if data.error}
			<div class="mt-4 rounded-lg bg-red-100 p-4 text-red-700">
				<div class="flex">
					<svg class="h-5 w-5 text-red-400" fill="currentColor" viewBox="0 0 20 20">
						<path
							fill-rule="evenodd"
							d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z"
							clip-rule="evenodd"
						/>
					</svg>
					<div class="ml-3">
						<p class="font-semibold">Error loading classrooms:</p>
						<p class="mt-1">{data.error}</p>
					</div>
				</div>
			</div>
		{/if}
	</div>
</div>
