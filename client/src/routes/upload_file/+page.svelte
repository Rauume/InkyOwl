<script lang="ts">
    let selectedFile: Blob;

    const handleFileChange = (event: any) => {
        selectedFile = event.target.files[0];
    };

    const submitForm = async () => {
        const formData = new FormData();
        formData.append("file", selectedFile);

        try {
            const response = await fetch("http://10.0.1.114:3000/upload", {
                method: "POST",
                body: formData,
            });

            if (!response.ok) {
                throw new Error("Network response was not ok");
            }

            const data = await response.json();
            console.log(data);
        } catch (error) {
            // console.error(
            //     "There was a problem with the fetch operation:",
            //     error,
            // );
        }
    };
</script>

<!-- HTML form to collect file input -->
<form on:submit|preventDefault={submitForm}>
    <div>
        <label for="file">Choose an image file:</label>
        <input
            id="file"
            type="file"
            accept="image/*"
            on:change={handleFileChange}
        />
    </div>
    <button type="submit">Upload</button>
</form>
