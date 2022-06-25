<script>
    import axios from "axios";
    import { API_URL } from "../../variables";

    export let src;

    // $: basename = src.split("/").pop();

    axios
        .get(API_URL + "/images/" + src.split("/").pop() + "/info")
        .then((response) => {
            const res = response.data;
            enabled = res.enabled ? "enabled" : "disabled";
        });

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
        filter: brightness(50%);
    }
    .photo {
        width: 20vw;
        height: 25vh;
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
        background-color: #f5a52a;
        outline: none;
        cursor: pointer;
        border: none;
        color: #f0f0f0;
        margin-bottom: 0;
        font-size: large;
        /* width: 2vw !important; */
    }
    button:hover {
        transition: all 0.2s;
        background-color: #ac7523;
    }
</style>
