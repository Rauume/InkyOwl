<!-- MAINPAGE  -->
<script lang="ts">
  import ImageModal from "./ImageModal.svelte";
  let img: any;
  let currentImage: string;
  const promise = getLatestImage();

  async function getLatestImage() {
    const data = await fetch(`http://10.0.1.114:3000/api/last_image`);
    currentImage = await data.json();
    console.log(currentImage);
  }
</script>

<div class="box">
  <!-- <img class="m-image" loading="lazy" src={currentImage.url} alt="random img" /> -->
  {#await promise}
    Loading
  {:then _}
    <ImageModal img={currentImage} />
  {/await}
</div>

<style>
  main {
    position: relative;
    max-width: 800px;
    margin: 0 auto;
    min-height: 101vh;
    padding: 1em;
  }

  main :global(.meta) {
    color: #999;
    font-size: 12px;
    margin: 0 0 1em 0;
  }
  
  .box {
    position: relative;    
		width: 300px;
		border: 1px solid #aaa;
		border-radius: 2px;
		box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.1);
		padding: 1em;
		/* margin: 0 0 1em 0; */
    margin: 0 auto;    
	}
</style>
