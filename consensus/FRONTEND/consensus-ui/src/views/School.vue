<template>
    <div>
        <main-header></main-header>
        <router-view></router-view>
    </div>
</template>


<script>
    // @ is an alias to /src
    import MainHeader from "@/components/MainHeader";

    export default {
        name: "School",
        components: {
            MainHeader
        }
    };
</script>
