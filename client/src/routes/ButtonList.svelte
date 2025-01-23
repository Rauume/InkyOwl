<script lang="ts">
  export let buttons: any[] = []; // Prop for button labels
  export let selected = null; // Current selected button
  export let onSelect: (value: string) => void = () => {}; // Callback for selection
</script>

<div class="button-list">
  {#each buttons as button}
    <button
      class:selected={selected === button}
      on:click={() => onSelect(button)}
    >
      {button}
    </button>
  {/each}
</div>

<style>
  .button-list button {
    margin: 5px;
    padding: 10px;
    border: 1px solid #ccc;
    background-color: #f5f5f5;
    cursor: pointer;
  }

  .button-list button.selected {
    background-color: #007bff;
    color: white;
    border-color: #007bff;
  }
</style>