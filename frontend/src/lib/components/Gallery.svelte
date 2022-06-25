<script>
    import axios from "axios";
    import { API_URL } from "../../variables.js";
    import Image from "./Image.svelte";

    axios
        .get(API_URL)
        .then((response) => {
            const res = response.data;
            images = [];
            for (let i = 0; i < res.images.length; i++) {
                images.push(res.images[i].name);
            }
        })
        .catch((error) => {
            console.log(error);
        });

    let images;
</script>

{#if images}
    <div class="gallery">
        {#each images as image}
            <Image src={API_URL + "/images/" + image} />
        {/each}
    </div>
{/if}

<style>
    .gallery {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
    }
</style>
