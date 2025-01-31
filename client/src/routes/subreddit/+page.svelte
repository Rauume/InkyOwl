<script lang="ts">
	import { requestJsonFromAPI } from "../localApiRequest";
	let rand = "0";

	const getRand = () => {
		requestJsonFromAPI("/api/rand").then(
			(data) => (rand = data.randomNumber),
		);
	};
	import ButtonList from "../ButtonList.svelte";

	let buttons: string[] = [
		"Home",
		"Set Image",
		"Gallery",
		"Reddit",
		"Options",
	];
	let selectedButton: String = buttons[0];

	function handleSelect(button: String): void {
		selectedButton = button;
	}
</script>

<header>Subreddit support WIP</header>

<main>
	<h1>Your number is {rand}!</h1>
	<button on:click={getRand}>Get a random number</button>

	<h1>Select a Button</h1>
	<ButtonList {buttons} selected={selectedButton} onSelect={handleSelect} />

	<p>Selected: {selectedButton || "None"}</p>
</main>

<style>
	.grid {
		display: grid;
		grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
		grid-gap: 0.8rem;
	}
</style>
