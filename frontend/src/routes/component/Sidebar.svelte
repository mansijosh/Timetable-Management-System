<script lang="ts">
	import { goto } from '$app/navigation';

	// List of sidebar items
	const menuItems = [
		{ name: 'Classroom', path: '../classroom' },
		{ name: 'Departments', path: '../department' },
		{ name: 'Users', path: '/users' },
		{ name: 'Faculty', path: '/faculty' },
		{ name: 'Timetable', path: '/timetable' }
	];

	function navigate(path: string) {
		goto(path);
	}
</script>

<div class="flex min-h-screen">
	<!-- Sidebar -->
	<aside class="flex w-64 flex-col bg-gray-800 p-4 text-white">
		<h1 class="mb-6 text-2xl font-bold">Admin Panel</h1>

		{#each menuItems as item}
			<button
				class="mb-2 rounded px-4 py-2 text-left hover:bg-gray-700"
				on:click={() => navigate(item.path)}
			>
				{item.name}
			</button>
		{/each}
	</aside>

	<!-- Main content -->
	<main class="flex-1 bg-gray-100 p-6">
		<slot></slot>
		<!-- Page content will appear here -->
	</main>
</div>
