<!-- MAINPAGE  -->
<script lang="ts">
	import { onMount, onDestroy } from "svelte";
	import ImageModal from "./ImageModal.svelte";
	import { fade } from "svelte/transition";
	let currentImage: ImageResponse = $state();
	const promise = getLatestImage();
	let eventSource: EventSource;
	let messages: any[] = [];

	async function getLatestImage() {
		const data = await fetch(`http://10.0.1.114:3000/current_image`);
		currentImage = await data.json();
	}
	
	async function getNewImage() {
		fetch("http://10.0.1.114:3000/get_new_image")
	}

	onMount(() => {
		eventSource = new EventSource("http://10.0.1.114:3000/image_updates");

		eventSource.onopen = (event) => {
			// console.log("SSE connection opened:", event);
			messages = [
				{
					timestamp: new Date().toLocaleTimeString(),
					text: "Connection established. Waiting for updates...",
				},
				...messages,
			];
		};

		//When a message is recieved from SSE updates
		eventSource.onmessage = (event) => {
			// console.log("SSE message received:", event.data);			
			currentImage = JSON.parse(event.data);
		};
	});

	onDestroy(() => {
		// Clean up the EventSource connection when the component is unmounted
		if (eventSource) {
			// console.log("Closing SSE connection on component destroy.");
			eventSource.close();
		}
	});
</script>

<div class="box">
	{#await promise}
		Loading
	{:then _}
		{#key currentImage.url}
			<p transition:fade>
				<ImageModal
					img={currentImage.url}
					alt={currentImage.file_name}
				/>
			</p>
			<ul>
				<!-- <li><strong>URL:</strong> {currentImage.url}</li> -->
				<li><strong>File Name:</strong> {currentImage.file_name}</li>
				<li><strong>Source:</strong> {currentImage.source}</li>
				<li>
					<strong>Added:</strong>
					{new Date(currentImage.date_added).toLocaleString()}
				</li>
			</ul>
		{/key}
	{/await}
	<button onclick={getNewImage}> Get New Image </button>
</div>

<style>
	.box {
		max-width: 450px;
		margin: 20px auto;
		min-width: 300px;
		border: 1px solid #ddd;
		border-radius: 8px;
		padding: 10px;
		background-color: #f9f9f9;
		box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
	}
</style>
