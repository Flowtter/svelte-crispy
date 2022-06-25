<script>
    import axios from "axios";
    import { onMount } from "svelte";
    import { API_URL } from "../../variables";

    export let src;

    // $: basename = src.split("/").pop();
    const fetch = () => {
        axios
            .get(API_URL + "/images/" + src.split("/").pop() + "/info")
            .then((response) => {
                const res = response.data;
                enabled = res.enabled ? "enabled" : "disabled";
            });
    };
    onMount(fetch);

    let enabled;

    function handleClick() {
        axios.get(API_URL + "/images/" + src.split("/").pop() + "/switch");
        enabled = enabled == "disabled" ? "enabled" : "disabled";
    }
</script>

<div class="photo">
    <img {src} alt="" class={enabled} />
    <button class="info" on:click={handleClick}>&times</button>
</div>

<style>
    .disabled {
        filter: brightness(40%);
    }
    .photo {
        width: calc(1920px / 5);
        height: calc(1080px / 5);
        background-color: #f5a52a;
        display: flex;
        justify-content: center;
        border-radius: 2vh;
        position: relative;
        margin: 1vh;
    }
    img {
        width: 94%;
        height: 90%;
        object-fit: cover;
        margin: auto;
        display: block;
        border-radius: 2vh;
    }
    .info {
        position: absolute;
        right: 0px;
        bottom: 0px;
        height: 50px;
        width: 50px;
        border-radius: 15px 0 15px 0;
        font-size: 3em;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    button {
        text-align: center;
        padding: 12px 20px;
        box-sizing: border-box;
        border: none;
        border-radius: 1vh;
        background-color: var(--terciary);
        outline: none;
        cursor: pointer;
        border: none;
        color: var(--white-text);
        margin-bottom: 0;
        font-size: large;
        /* width: 2vw !important; */
    }
    button:hover {
        transition: all 0.2s;
        background-color: var(--terciary-variant);
    }
</style>
