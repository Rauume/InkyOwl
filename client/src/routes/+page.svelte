<!-- <h1>Welcome to SvelteKit</h1>
<p>
    Visit <a href="https://svelte.dev/docs/kit">svelte.dev/docs/kit</a> to read the
    documentation
</p> -->

<script>
  import { requestFromAPI } from "../localApiRequest.ts";
  let rand = "0";

  const getRand = () => {
    // fetch("/api/rand")
    // console.log("button pressed")
    const randNumber = requestFromAPI("/api/rand")
      .then((d) => d.text())
      .then((d) => (rand = d));
  }
</script>

<h1>Your number is {rand}!</h1>
<button on:click={getRand}>Get a random number</button>
