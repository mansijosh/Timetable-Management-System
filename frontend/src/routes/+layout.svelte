<script lang="ts">
	import '../app.css';

	import favicon from '$lib/assets/favicon.svg';
	import Sidebar from './component/Sidebar.svelte';

	let { children, data } = $props();
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
</svelte:head>

{#if data.isAuthenticated && !data.isLoginPage}
	<Sidebar>
		{@render children?.()}
	</Sidebar>
{:else}
	{@render children?.()}
{/if}
