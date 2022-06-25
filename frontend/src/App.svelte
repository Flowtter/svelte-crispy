<script>
	import Gallery from "./lib/components/Gallery.svelte";
</script>

<main>
	<Gallery />
</main>

<style>
	main {
		background-color: grey;
		height: 100vh;
		widows: 100vw;
	}
	:global(body) {
		margin: 0;
		padding: 0;
	}
</style>
