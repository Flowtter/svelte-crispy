<script>
	import Gallery from "./lib/components/Gallery.svelte";
	import LeftBar from "./lib/components/LeftBar/LeftBar.svelte";

	var display = "hide";
	var init = "init";
	setTimeout(() => {
		display = "";
		init = "hide";
	}, 500);

	let reload;
	function handleReload(event) {
		location.reload();
	}
</script>

<main class={display}>
	<LeftBar on:message={handleReload} />
	<Gallery />
</main>
<div class={init} />

<style>
	main {
		background-color: var(--primary);
		color: var(--white-text);
		min-width: 100%;
		min-height: 100%;
	}
	:global(body) {
		margin: 0;
		padding: 0;
	}
	* {
		--primary: #141b23;
		--secondary: #1b222f;
		--terciary: #f5a52a;
		--terciary-variant: #c57f15;
		--terciary-hover: #d48c1f;

		--exit: #e74c3c;
		--exit-hover: #dd4332;
		--exit-selected: #c0392b;

		--white-text: #f0f0f0;
	}
	.hide {
		display: none;
	}
	.init {
		height: 100vh;
		width: 100vw;
		background-color: var(--primary);
	}
</style>
