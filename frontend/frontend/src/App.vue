<template>
    <div class="test">
        <h1>Тестируем сайт по ювелирке</h1>
    </div>
    <button @click="request_database">ПОЛУЧИТЬ ДАННЫЕ</button>
    <div>
        {{items}}
    </div>
    <div class="cards">
        <div v-for="item in items" v-bind:key="item.id" class="card">
            <img v-bind:src="item.image" alt="Не работает">
            <p class="name">{{item.name}}</p>
            <p class="price">{{item.price}}</p>
        </div>
    </div>

</template>

<script>

    import axios from "axios";

    export default {
        name: 'App',
        data() {
            return {
                items: [],
            }
        },
        methods: {
            async request_database() {
                (await axios({
                    method: 'get',
                    url: 'http://127.0.0.1:8000/api/Jewelery/'
                })).data.forEach(item => {
                    this.items.push(item)
                })
            }
        }

    }
</script>

<style>
    /*.cards {*/
    /*    display: flex;*/
    /*    flex-wrap: wrap;*/
    /*    justify-content: center;*/
    /*}*/
    /*.card img {*/
    /*    width: 30%;*/
    /*}*/

    .cards {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
    }

    .card {
        flex: 0 1 calc(100%/3 - 20px*2);
        margin: 20px;
    }

    .card img {
        width: 90%;
    }
</style>
