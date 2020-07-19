<template>
  <div class="home">
    <v-container fluid>
      <v-row align="center" justify="center">
        <v-col cols="12" xs="4" sm="9" md="10" lg="11" align-self="center">
          <Map></Map>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import Map from "@/components/Map.vue";
export default {
  name: "Home",
  components: {
    Map
  },
  created() {
    this.setupstream();
  },
  methods: {
    setupstream() {
      let es = new EventSource("http://localhost:8081/topic/LiveBusData");

      es.addEventListener(
        "message",
        event => {
          console.log("New Incoming Message Message");
          let mark = JSON.parse(event.data);
          // call action ins Store
          console.log("this is mark", mark);

          this.$store.dispatch("updatemarker", mark);
        },
        false
      );

      es.addEventListener(
        "error",
        event => {
          if (event.readyState == EventSource.CLOSED) {
            console.log("Event Closed");
            console.log(EventSource);
          }
        },
        false
      );
    }
  }
};
</script>
