<!-- <h1>Welcome to SvelteKit</h1>
<p>
    Visit <a href="https://svelte.dev/docs/kit">svelte.dev/docs/kit</a> to read the
    documentation
</p> -->

<script lang="ts">
  import { requestJsonFromAPI } from "../localApiRequest.ts";
  import ButtonList from "./ButtonList.svelte";
  
  let rand = "0";

  const getRand = () => {
    requestJsonFromAPI("/api/rand")
      .then((data) => (rand = data.randomNumber))
  }
  
  let buttons: string[] = ["Home", "Set Image", "Gallery", "Reddit", "Options" ];
  let selectedButton: String = buttons[0];
  
  function handleSelect(button: String): void
  {
    selectedButton = button;
  }
</script>

<main>
  <h1>Your number is {rand}!</h1>
  <button on:click={getRand}>Get a random number</button>
  
  <h1>Select a Button</h1>
  <ButtonList
  buttons={buttons}
  selected={selectedButton}
  onSelect={handleSelect}
  />
  
  <p>Selected: {selectedButton || 'None'}</p>
  
</main>
  
<style>
  main {
    position: relative;
    max-width: 800px;
    margin: 0 auto;
    min-height: 101vh;
    padding: 1em;
  }
  
  main :global(.meta){
    color: #999;
    font-size: 12px;
    margin: 0 0 1em 0;
  }
</style>

