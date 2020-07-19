<template>
  <v-container fluid>
    <v-col cols="11" xs="4" sm="9" md="10" lg="11" align-self="center">
      <l-map style="height: 500px; width: 100%" :zoom="zoom" :center="center">
        <l-tile-layer :url="url" zoomOffset="-1" />
        <l-marker :lat-lng="marker1">
          <l-icon :icon-size="iconSize" :icon-url="icon"></l-icon>
        </l-marker>
        <l-marker :lat-lng="marker2">
          <l-icon :icon-size="iconSize" :icon-url="icon"></l-icon>
        </l-marker>
        <l-marker :lat-lng="marker3">
          <l-icon :icon-size="iconSize" :icon-url="icon"></l-icon>
        </l-marker>
      </l-map>
    </v-col>
  </v-container>
</template>

<script>
import { latLng } from "leaflet";
import { LMap, LTileLayer, LMarker, LIcon } from "vue2-leaflet";
import bus from "../assets/bus.png";

export default {
  name: "Map",
  components: {
    LMap,
    LTileLayer,
    LMarker,
    LIcon
  },
  data() {
    return {
      zoom: 12,
      center: latLng(12.9791198, 77.5912997),
      url:
        "https://api.mapbox.com/styles/v1/mapbox/streets-v11/tiles/{z}/{x}/{y}?access_token=pk.eyJ1Ijoic2hhbmtoYTExNyIsImEiOiJja2NmdW5uZWkwbHdzMnhwY2VpeGQybXBsIn0.yRa9ivhduFYLLZOO1RXO-Q",
      attribution:
        '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      icon: bus,
      iconSize: 50
    };
  },
  methods: {
    zoomUpdate(zoom) {
      this.currentZoom = zoom;
    },
    centerUpdate(center) {
      this.currentCenter = center;
    },
    showLongText() {
      this.showParagraph = !this.showParagraph;
    },
    innerClick() {
      alert("Click!");
    }
  },
  computed: {
    marker1() {
      return this.$store.state.map.marker1;
    },

    marker2() {
      return this.$store.state.map.marker2;
    },
    marker3() {
      return this.$store.state.map.marker3;
    }
  }
};
</script>
