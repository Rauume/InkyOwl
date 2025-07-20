<script lang="ts">
  import { onMount } from "svelte";

  interface Source {
    name: string;
    active: boolean;
  }

  let timerValues = [
    { id: 5, text: "5 Mins" },
    { id: 10, text: "10 Mins" },
    { id: 30, text: "30 Mins" },
    { id: 60, text: "1 Hours" },
    { id: 60, text: "2 Hours" },    
  ];

  let sources: Source[] = $state([]);
  let newItemText: string = "";
  let isDirty: boolean = $state(false);
  let selectedPeriod = $state();

  onMount(async () => {
    try {
      const data = await fetch("http://10.0.1.114:3000/sources/get");
      sources = await data.json();
    } catch (error) {
      console.error("Failed to parse JSON:", error);
    }
  });

  function removeItem(idToRemove: string) {
    sources = sources.filter((item) => item.name !== idToRemove);
  }

  function addItem() {
    sources.push({ name: newItemText, active: true });
  }

  async function updateServer() {
    if (sources.length > 0) {
      try {
        const response = await fetch("http://10.0.1.114:3000/reddit/set", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },

          body: JSON.stringify(sources),
        });
      } catch (error) {
        console.error(error);
      }
    }
  }

  $effect(() => {
    updateServer();
  });

  function handleSubmit(event) {
    event.preventDefault();
    alert(
      `answered question ${selectedPeriod.id} (${selectedPeriod.text}) with`,
    );
  }
</script>

<div class="list-container">
  <h2>Source Settings</h2>

  <ul class="item-list">
    {#each sources as item (item.name)}
      <li class="list-item" class:inactive={!item.active}>
        <div class="checkbox-container">
          <input
            type="checkbox"
            class="item-checkbox"
            bind:checked={item.active}
            autocomplete="off"
          />
        </div>

        <span class="item-title">{item.name}</span>
      </li>
    {:else}
      <p
        style="text-align: center; color: #777;    /* border: 1px solid #ddd; */
"
      >
        No items in the list.
      </p>
    {/each}
  </ul>

  <h2>How Often?</h2>

  <form onsubmit={handleSubmit}>
    <text> Update every </text>
    <select bind:value={selectedPeriod} onchange={() => ("")}>
      {#each timerValues as timerValue}
        <option value={timerValue}>
          {timerValue.text}
        </option>
      {/each}
    </select>

    <!-- <input bind:value={answer} /> -->

  </form>
  
  <text> From [9AM] to [8PM] </text>
  
  
</div>
<button disabled={isDirty} type="submit"> Submit </button>

<h2>Test</h2>

<style>
  .list-container {
    /* max-width: 650px; */
    /* width: max-content; */
    /* max-width: fit-content; */
    /* width: 20rem; */
    /* height: fit-content; */

    /* max-width: calc(100vw - 8px * 2); */
    /* max-height: calc(100vh - 80px * 2); */
    /* min-height: 20rem; */
    width: 80vw;
    max-width: 50rem;
    /* display: grid; */
    padding: 20px;

    margin: 40px;
    
    border-radius: 8px;
    /* padding: 10px; */
    background-color: #f9f9f9;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);

    /* padding-left: 1.5rem; */
    /* padding-right: 1.5rem; */
  }

  h2 {
    text-align: center;
    color: #333;
    margin-bottom: 20px;
  }

  .item-list {
    list-style: none; /* Remove default list bullets */
    padding: 15px 0; /* Note for later, the 0 is important, keeping the element fully left aligned.*/
  }

  .list-item {
    display: flex;
    align-items: center;
    padding: 12px 15px;
    margin-bottom: 10px;
    background-color: #fff;
    border: 1px solid #eee;
    border-radius: 6px;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.08);
    transition: all 0.2s ease-in-out;
  }

  .list-item:last-child {
    margin-bottom: 0;
  }

  .list-item:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  }

  .list-item.inactive {
    background-color: #f0f0f0;
    color: #999;
    opacity: 0.7;
  }

  .checkbox-container {
    margin-right: 15px;
    display: flex;
    align-items: center;
  }

  .item-checkbox {
    width: 20px;
    height: 20px;
    cursor: pointer;
    accent-color: #4caf50;
  }

  .item-title {
    font-size: 1.1em;
    color: #555;
    flex-grow: 1; /* Allows title to take available space */
    /* Add a strike-through for inactive items */
    text-decoration: none; /* Default */
    transition: text-decoration 0.2s ease;
  }

  .list-item.inactive .item-title {
    text-decoration: line-through;
    color: #777;
  }
</style>
