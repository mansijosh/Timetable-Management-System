<script lang="ts">
	import { goto } from '$app/navigation';
	import PageHeader from '$lib/component/PageHeader.svelte';
	import { LayoutDashboard } from 'lucide-svelte';
</script>

<div class="min-h-screen bg-gray-100 p-8">
	<div class="mx-auto max-w-3xl">
		<PageHeader
			title="Create Department"
			subtitle="Add a new department"
			Icon={LayoutDashboard}
		/>

		<div class="rounded-lg bg-white p-6 shadow-md">
			<form method="POST" class="space-y-4">
				
				
				<div>
					<label
						for="department-name"
						class="mb-1 block text-sm font-medium"
					>
						Department Name <span class="text-red-500">*</span>
					</label>
					<input
						id="department-name"
						name="name"
						required
						class="w-full rounded-md border px-3 py-2"
						placeholder="Enter department name"
					/>
				</div>

				
				<div>
					<label
						for="department-year"
						class="mb-1 block text-sm font-medium"
					>
						Year <span class="text-red-500">*</span>
					</label>
					<input
						id="department-year"
						type="number"
						name="year"
						required
						class="w-full rounded-md border px-3 py-2"
						placeholder="Enter year"
					/>
				</div>

				

				
				<div class="flex justify-end gap-3">
					<button
						type="button"
						on:click={() => goto('/departments')}
						class="rounded-md border px-4 py-2"
					>
						Cancel
					</button>

					<button
						type="submit"
						class="rounded-md bg-blue-600 px-4 py-2 text-white hover:bg-blue-700"
					>
						Save
					</button>
				</div>

			</form>
		</div>
	</div>
</div>
