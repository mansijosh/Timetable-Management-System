<script lang="ts">
	import { Users } from 'lucide-svelte';
	import type { PageData } from './$types';

	interface Props {
		data: PageData;
	}

	let { data }: Props = $props();
</script>

<div class="min-h-screen bg-gray-100 p-8">
	<div class="mx-auto max-w-7xl">
		<div class="mb-6 rounded-lg bg-white p-6 shadow-md">
			
			<h1 class="mb-2 text-3xl font-bold flex items-center gap-2" >
	<Users  class="w-8 h-8 p-1" />
	Faculties
</h1>
			<p class="text-gray-600">Manage all faculties and their details</p>
		</div>

		<div class="rounded-lg bg-white p-6 shadow-md">
			<div class="mb-4 flex items-center justify-between">
				<h2 class="text-2xl font-semibold">All Faculties</h2>
				<span class="rounded-full bg-blue-100 px-3 py-1 text-sm font-medium text-blue-800">
					Total: {data.faculties?.length || 0}
				</span>
			</div>

			{#if data.faculties && data.faculties.length > 0}
				<div class="overflow-x-auto">
					<table class="min-w-full divide-y divide-gray-200">
						<thead class="bg-gray-50">
							<tr>
								<th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider text-gray-500">
									Name
								</th>
								<th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider text-gray-500">
									Department
								</th>
								<th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider text-gray-500">
									Year
								</th>
							</tr>
						</thead>
						<tbody class="divide-y divide-gray-200 bg-white">
							{#each data.faculties as faculty}
								<tr class="hover:bg-gray-50">
									<td class="whitespace-nowrap px-6 py-4 text-sm font-medium text-gray-900">
										{faculty.name}
									</td>
									<td class="px-6 py-4 text-sm text-gray-700">
										{faculty.department?.name || 'N/A'}
									</td>
									<td class="whitespace-nowrap px-6 py-4 text-sm text-gray-700">
										{faculty.department?.year}
									</td>
								</tr>
							{/each}
						</tbody>
					</table>
				</div>
			{:else}
				<div class="py-12 text-center text-gray-500">
					<p class="mt-4 text-lg font-medium">No faculties found</p>
					<p class="mt-1 text-sm">There are no faculties in the system yet.</p>
				</div>
			{/if}
		</div>

		{#if data.error}
			<div class="mt-4 rounded-lg bg-red-100 p-4 text-red-700">
				<p class="font-semibold">Error loading faculties:</p>
				<p>{data.error}</p>
			</div>
		{/if}
	</div>
</div>
