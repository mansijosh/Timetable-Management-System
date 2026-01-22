<script lang="ts">
	import type { SvelteComponent } from 'svelte';

	export let title: string;
	export let subtitle: string;

	
	export let Icon:
		| (new (...args: any[]) => SvelteComponent)
		| null = null;
</script>

<div class="mb-6 rounded-lg bg-white p-6 shadow-md">
	<h1 class="mb-2 flex items-center gap-2 text-3xl font-bold">
		{#if Icon}
			<svelte:component this={Icon} class="h-8 w-8 p-1" />
		{/if}
		{title}
	</h1>

	<p class="text-gray-600">{subtitle}</p>
</div>
