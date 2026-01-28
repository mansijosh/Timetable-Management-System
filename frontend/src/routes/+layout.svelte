<script lang="ts">
	import '../app.css';

	import favicon from '$lib/assets/favicon.svg';
	import Sidebar from './component/Sidebar.svelte';

	let { children } = $props();
	import Sidebar from './component/Sidebar.svelte';

	let { children, data } = $props();
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
</svelte:head>

<div class="flex min-h-screen">
	<Sidebar />
	<div class="flex-1 p-6">
		{@render children?.()}
		<!-- renders the page content -->
	</div>
</div>

{#if data.isAuthenticated && !data.isLoginPage}
	<Sidebar>
		{@render children?.()}
	</Sidebar>
{:else}
	{@render children?.()}
{/if}
