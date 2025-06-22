<script lang="ts">
  import { onMount } from "svelte";

  interface Subreddit {
    name: string;
    active: boolean;
  }

  let subreddits: Subreddit[] = $state([]);
  let newItemText: string = "";

  onMount(async () => {
    try {
      const data = await fetch(
        `http://10.0.1.114:3000/reddit/get`,
      );
      subreddits = await data.json();
    } catch (error) {
      console.error("Failed to parse JSON:", error);
    }
  });

  function removeItem(idToRemove: string) {
    subreddits = subreddits.filter((item) => item.name !== idToRemove);
  }

  function addItem() {
    subreddits.push({ name: newItemText, active: true });
  }

  async function updateServer() {
    if (subreddits.length > 0) {
      try {
        const response = await fetch("http://10.0.1.114:3000/reddit/set", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },

          body: JSON.stringify(subreddits),
        });
      } catch (error) {
        console.error(error);
      }
    }
  }

  $effect(() => {
    updateServer();
  });
</script>

<div class="list-container">
  <h2>Sub-reddits</h2>

  <ul class="item-list">
    {#each subreddits as item (item.name)}
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

        <button class="remove-button" onclick={() => removeItem(item.name)}>
          Remove
        </button>
      </li>
    {:else}
      <p style="text-align: center; color: #777;">No items in the list.</p>
    {/each}
  </ul>

  <div class="item-input">
    <input
      type="text"
      bind:value={newItemText}
      placeholder="Enter new item text"
    />
    <button class="add-sub-button" onclick={addItem}>Add Subreddit</button>
  </div>
</div>

<style>
  .list-container {
    max-width: 450px;
    margin: 20px auto;
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 10px;
    background-color: #f9f9f9;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
  }

  h2 {
    text-align: center;
    color: #333;
    margin-bottom: 20px;
  }

  .item-list {
    list-style: none; /* Remove default list bullets */
    padding: 0;
    margin: 10;
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

  .remove-button {
    background-color: #f44336;
  }

  .remove-button:hover {
    background-color: #d32f2f;
  }

  .add-sub-button {
    background-color: #7fbbb3;
  }

  .item-input {
    display: flex;
    gap: 8px;
    border-radius: 8px;
  }

  input[type="text"] {
    flex: 1;
    padding: 8px;
    min-width: 150px;
    font-size: 1rem;
  }
</style>
