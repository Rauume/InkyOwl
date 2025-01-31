<script lang="ts">
	import {fade} from 'svelte/transition'
    
	export let img
	let click;
	let showModal = click ? true : false;
    
    function handleKeydown(event: KeyboardEvent) {
		if (event.key === "Escape") {
			showModal = false;
		}
	}

</script>

<div class="image-wrapper">
<!-- svelte-ignore a11y_click_events_have_key_events, a11y_no_noninteractive_element_interactions -->
<img class="image" loading="lazy" onclick={()=>{
	showModal = !showModal;
}} src={img.url} crossorigin="anonymous" alt="random img"/>
</div>

{#if showModal}
<!-- svelte-ignore a11y_click_events_have_key_events, a11y_no_static_element_interactions -->
<div 
class="modal" transition:fade={{duration: 100}}
onclick={(e) => {showModal = !showModal}}
>
	<!-- Give an obvious close button, even if it doesnt change anything-->
	<div
	class="close">
		x
	</div>
	
	<div class="modal-image">
		<img class="m-image" loading="lazy" src={img.url} alt="Loading"/>
	</div>
</div>
{/if}

<!-- exit image using Esc key -->
<svelte:window on:keydown|preventDefault={handleKeydown} />

<style>
	img:before {
background:black;
	}
	.m-image{

		width:100%;
		height:auto;
		max-height:500px;
		object-fit: scale-down;
	}
	.close {
		cursor: pointer;
		font-size: 3rem;
		position: absolute;
		right: 0;
		color: white;
		margin-right:1.5rem;
		top:0;
	}
	.image {
		cursor: pointer;
		width:100%;
		max-width:400px;
		max-height:400px;
  	transition: 0.125s;
	}
	
	.image:hover {
		opacity: 0.7;
	}
	
	img:active {
		opacity: 0.5;
	}
	
	.modal-image {
	  margin: auto;
  	display: block;
  	width: 80%;
  	max-width: 100%;	
	}
	.modal {
  	position: fixed;
		z-index: 2;
  	padding-top: 100px;
  	left: 0;
  	top: 0;
  	width: 100%;
  	height: 100%;
  	overflow: auto;
  	background-color: rgb(0,0,0);
  	background-color: rgba(0,0,0,0.9);
	}
</style>