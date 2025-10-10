<script lang="ts">
	import { goto } from '$app/navigation';

	const menuItems = [
		{ name: 'Classroom', path: '../classroom', icon: '📚' },
		{ name: 'Departments', path: '../department', icon: '🏢' },
		{ name: 'Users', path: '/user', icon: '👥' },
		{ name: 'Faculty', path: '/faculty', icon: '🧑‍🏫' },
		{ name: 'Timetable', path: '/timetable', icon: '📅' }
	];

	function navigate(path: string) {
		goto(path);
	}
</script>

<div class="flex min-h-screen">
	<!-- Sidebar -->
	<aside
		class="flex w-64 flex-col p-6 text-white"
		style="background: linear-gradient(to bottom, #6A89A7, #c7d9ffff);"
	>
		<!-- Admin Panel Title -->
		<h1 class="mb-8 text-center text-3xl font-bold text-yellow-300 drop-shadow-lg">Admin Panel</h1>

		{#each menuItems as item}
			<button
				class="mb-3 flex items-center gap-4 rounded-lg px-4 py-3 font-medium text-gray-100
               shadow-md transition-all duration-300 hover:bg-white hover:text-blue-700"
				on:click={() => navigate(item.path)}
			>
				<span class="text-xl">{item.icon}</span>
				<span>{item.name}</span>
			</button>
		{/each}
	</aside>

	<!-- Main content with background -->
	<main
		class="flex-1 p-8"
		style="background-image: url('/dashboard-bg.jpg'); background-size: cover; background-position: center; min-height: 100vh;"
	>
		<div class="bg-opacity-80 min-h-full rounded-xl bg-white p-6 shadow-lg">
			<slot></slot>
		</div>
	</main>
</div>
