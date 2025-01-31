<script lang="ts">
	import ImageModal from "../ImageModal.svelte";
	let images: any[] = [];
	let allImages: String[] = [];

	const promise = data();

	async function data() {
		const d = await fetch(`http://10.0.1.114:3000/api/recent_images`);
		const list = await d.json();
		allImages = [...list];
		images = [...allImages.slice(0, 5)];
		console.log(list);
	}
</script>

<div class="grid">
	{#await promise}
		Loading
	{:then _}
		{#each images as img (img.url)}
			<div class="grid-item">
				<ImageModal {img} />
			</div>
		{/each}
	{/await}
</div>

<style>
	.grid {
		display: grid;
		grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
		grid-gap: 0.8rem;
	}
</style>
