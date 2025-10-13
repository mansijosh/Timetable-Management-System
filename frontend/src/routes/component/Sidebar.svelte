<script lang="ts">
	import { goto } from '$app/navigation';
	import * as Avatar from '$lib/components/ui/avatar/index.js';

	import {
		BookOpenText,
		Hotel,
		UserRoundPen,
		GraduationCap,
		BookMarked,
		CalendarDays
	} from 'lucide-svelte';

	const menuItems = [
		{ name: 'Classroom', path: '../classroom', icon: BookOpenText },
		{ name: 'Departments', path: '../department', icon: Hotel },
		{ name: 'Users', path: '/user', icon: UserRoundPen },
		{ name: 'Faculty', path: '/faculty', icon: GraduationCap },
		{ name: 'Subjects', path: '/subject', icon: BookMarked },
		{ name: 'Timetable', path: '/timetable', icon: CalendarDays }
	];

	function navigate(path: string) {
		goto(path);
	}
</script>

<div class="flex min-h-screen">
	<!-- Sidebar -->
	<aside
		class="flex w-64 flex-col justify-between p-6 text-white"
		style="background: linear-gradient(to bottom, #6A89A7, #c7d9ffff);"
	>
		<!-- Top Section -->
		<div>
			<h1 class="mb-8 text-center text-3xl font-bold text-black">Admin Panel</h1>

			{#each menuItems as item}
				<button
					class="mb-3 flex w-full items-center gap-4 rounded-lg px-4 py-3 font-medium text-gray-100
                    shadow-md transition-all duration-300 hover:bg-white hover:text-blue-700"
					on:click={() => navigate(item.path)}
				>
					<svelte:component this={item.icon} class="h-5 w-5 text-black" />

					<span>{item.name}</span>
				</button>
			{/each}
		</div>

		<!-- Bottom Section - Clickable Profile -->
		<button
			class="flex w-full flex-row items-center border-t border-gray-300 pt-6 transition-opacity hover:opacity-80"
			on:click={() => navigate('/profile')}
		>
			<Avatar.Root class="h-12 w-12">
				<Avatar.Image src="https://github.com/shadcn.png" alt="@shadcn" />
				<Avatar.Fallback>CN</Avatar.Fallback>
			</Avatar.Root>
			<p class="mt-2 pl-2 text-sm font-semibold text-black">xyz</p>
		</button>
	</aside>

	<!-- Main content with background -->
	<main
		class="flex-1 p-8"
		style=" background-size: cover; background-position: center; min-height: 100vh;"
	>
		<div class="bg-opacity-80 min-h-full rounded-xl bg-white p-6 shadow-lg">
			<slot></slot>
		</div>
	</main>
</div>
