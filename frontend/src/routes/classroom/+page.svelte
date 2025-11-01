<script lang="ts">
	import type { PageData } from './$types';
	import { Building2, Trash2 } from 'lucide-svelte';
	import { enhance } from '$app/forms';

	interface Props {
		data: PageData;
	}

	let { data }: Props = $props();
</script>

<div class="min-h-screen bg-gray-100 p-8">
	<div class="mx-auto max-w-7xl">
		<!-- Header -->
		<div class="mb-6 rounded-lg bg-white p-6 shadow-md">
			<h1 class="mb-2 text-3xl font-bold flex items-center gap-2">
				<Building2 class="w-8 h-8 p-1" />
				Classrooms
			</h1>
			<p class="text-gray-600">Manage all classrooms and their details</p>
		</div>

		<!-- Table -->
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
								<th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider text-gray-500">Room No</th>
								<th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider text-gray-500">Building</th>
								<th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider text-gray-500">Department</th>
								<th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider text-gray-500">Year</th>
								<th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider text-gray-500">Capacity</th>
								<th class="px-6 py-3 text-center text-xs font-medium uppercase tracking-wider text-gray-500">Actions</th>
							</tr>
						</thead>
						<tbody class="divide-y divide-gray-200 bg-white">
							{#each data.classrooms as classroom}
								<tr class="hover:bg-gray-50">
									<td class="px-6 py-4 text-sm font-medium text-gray-900">{classroom.room_no}</td>
									<td class="px-6 py-4 text-sm text-gray-700">{classroom.building_name}</td>
									<td class="px-6 py-4 text-sm text-gray-700">{classroom.department?.name || 'N/A'}</td>
									<td class="px-6 py-4 text-sm text-gray-700">{classroom.department?.year || 'N/A'}</td>
									<td class="px-6 py-4 text-sm text-gray-700">
										<span class="inline-flex rounded-full bg-green-100 px-2 py-1 text-xs font-semibold text-green-800">
											{classroom.capacity}
										</span>
									</td>
									<td class="px-6 py-4 text-center">
										<form method="POST" action="?/deleteClassroom" use:enhance>
											<input type="hidden" name="id" value={classroom.id} />
											<button type="submit" class="text-red-600 hover:text-red-800" title="Delete Classroom">
												<Trash2 class="w-5 h-5 inline-block" />
											</button>
										</form>
									</td>
								</tr>
							{/each}
						</tbody>
					</table>
				</div>
			{:else}
				<div class="py-12 text-center text-gray-500">
					<p class="mt-4 text-lg font-medium">No classrooms found</p>
				</div>
			{/if}
		</div>

		{#if data.error}
			<div class="mt-4 rounded-lg bg-red-100 p-4 text-red-700">
				<p class="font-semibold">Error loading classrooms:</p>
				<p>{data.error}</p>
			</div>
		{/if}
	</div>
</div>
