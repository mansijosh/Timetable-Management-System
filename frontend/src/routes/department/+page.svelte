<script lang="ts">
	import type { PageData } from './$types';

	interface Props {
		data: PageData;
	}

	let { data }: Props = $props();
</script>

<div class="min-h-screen bg-gray-100 p-8">
	<div class="mx-auto max-w-6xl">
		<div class="mb-6 rounded-lg bg-white p-6 shadow-md">
			<h1 class="mb-2 text-3xl font-bold" style="font-family: 'Poppins', sans-serif;">Dashboard</h1>
			<p class="text-gray-600">Welcome to TimetableIQ</p>
		</div>

		<div class="rounded-lg bg-white p-6 shadow-md">
			<h2 class="mb-4 text-2xl font-semibold">Departments</h2>

			{#if data.departments && data.departments.length > 0}
				<div class="grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-3">
					{#each data.departments as department}
						<div class="rounded-lg border p-4 transition-shadow hover:shadow-md">
							<h3 class="text-lg font-semibold text-gray-800">{department.name}</h3>
							{#if department.description}
								<p class="mt-2 text-sm text-gray-600">{department.description}</p>
							{/if}
							<div class="mt-3 text-xs text-gray-500">
								ID: {department.id}
							</div>
						</div>
					{/each}
				</div>
			{:else}
				<div class="py-8 text-center text-gray-500">
					<p>No departments found.</p>
				</div>
			{/if}
		</div>

		{#if data.error}
			<div class="mt-4 rounded-lg bg-red-100 p-4 text-red-700">
				<p class="font-semibold">Error loading departments:</p>
				<p>{data.error}</p>
			</div>
		{/if}
	</div>
</div>
