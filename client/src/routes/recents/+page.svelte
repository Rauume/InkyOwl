<script lang="ts">
	import ImageModal from "../ImageModal.svelte";
	// import ImageResponse from "../ImageResponse";
	let images: ImageResponse[] = [];

	const promise = getLatestImages();

	async function getLatestImages() {
		const data = await fetch(`http://10.0.1.114:3000/recent_images`);
		images = await data.json();
		console.log(images);
	}
</script>

<div class="grid">
	{#await promise}
		Loading
	{:then _}
		{#each images as img (img)}
			<div class="grid-item">
				<ImageModal img={img.url} alt={""} />
			</div>
		{/each}
	{/await}
</div>

<style>
	.grid {
		max-width: 450px;
		display: grid;
		grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
		grid-gap: 1.8rem;
	}
	.grid-item {
		display: flex;
		justify-content: center;
		align-items: center;
		max-width: 400px;
	}
</style>
